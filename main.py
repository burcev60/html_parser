"""
Скачивает документацию рекурсивным обходом ссылок (BFS) и сохраняет
каждую страницу как .md.

Особенности:
  • Человеческие имена файлов: /api/base_model/ → api/base_model.md
    (а не api/base_model/index.md)
  • Перелинковка: ссылки на другие страницы документации заменяются
    относительными путями к локальным .md. Оригинальный URL остаётся рядом.
  • Два бэкенда: requests / curl_cffi (для Cloudflare).
  • IPv4-only, retry, Referer, preflight-проверка сети.

Установка:
    pip install requests beautifulsoup4 html2text brotli
    # опционально для Cloudflare:
    pip install curl_cffi

Запуск:
    python scrape_by_crawl.py --start https://pydantic.dev/docs/ \
                              --output ./pydantic_docs --backend curl_cffi
"""

from __future__ import annotations

# Принудительно IPv4 — ДО import requests
import urllib3.util.connection
urllib3.util.connection.HAS_IPV6 = False

import argparse
import os
import re
import socket
import sys
import time
from collections import deque
from pathlib import Path
from urllib.parse import urlparse, urljoin, urldefrag

import html2text
import requests
from bs4 import BeautifulSoup
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

try:
    from curl_cffi import requests as cffi_requests  # type: ignore
    HAS_CURL_CFFI = True
except ImportError:
    HAS_CURL_CFFI = False


DEFAULT_HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (X11; Linux x86_64; rv:124.0) "
        "Gecko/20100101 Firefox/124.0"
    ),
    "Accept": (
        "text/html,application/xhtml+xml,application/xml;q=0.9,"
        "image/avif,image/webp,*/*;q=0.8"
    ),
    "Accept-Language": "en-US,en;q=0.9,ru;q=0.8",
    "Accept-Encoding": "gzip, deflate, br",
    "DNT": "1",
    "Upgrade-Insecure-Requests": "1",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "none",
    "Sec-Fetch-User": "?1",
    "Connection": "keep-alive",
}

SKIP_EXT = {".png", ".jpg", ".jpeg", ".gif", ".svg", ".ico", ".webp",
            ".pdf", ".zip", ".tar", ".gz", ".css", ".js", ".woff",
            ".woff2", ".ttf", ".mp4", ".webm", ".xml", ".json"}


# --------------------------------------------------------------------------- #
# Сеть
# --------------------------------------------------------------------------- #
def preflight(url: str) -> None:
    host = urlparse(url).hostname
    try:
        socket.getaddrinfo(host, 443, proto=socket.IPPROTO_TCP)
    except socket.gaierror as e:
        sys.exit(f"DNS не резолвит {host}: {e}")
    try:
        with socket.create_connection((host, 443), timeout=10):
            pass
    except OSError as e:
        sys.exit(
            f"Нет TCP-соединения с {host}:443 — {e}\n"
            f"Проверьте сеть/VPN/прокси/IPv6."
        )


def make_requests_session() -> requests.Session:
    s = requests.Session()
    retry = Retry(
        total=5, connect=5, read=5, backoff_factor=1.0,
        status_forcelist=(429, 500, 502, 503, 504),
        allowed_methods=frozenset(["GET"]),
        respect_retry_after_header=True,
    )
    adapter = HTTPAdapter(max_retries=retry, pool_connections=20, pool_maxsize=20)
    s.mount("https://", adapter)
    s.mount("http://", adapter)
    s.headers.update(DEFAULT_HEADERS)
    return s


class Fetcher:
    def __init__(self, backend: str):
        self.backend = backend
        if backend == "requests":
            self.session = make_requests_session()
        elif backend == "curl_cffi":
            if not HAS_CURL_CFFI:
                sys.exit("curl_cffi не установлен. pip install curl_cffi")
            self.session = cffi_requests.Session(impersonate="chrome124")
            self.session.headers.update(DEFAULT_HEADERS)
        else:
            sys.exit(f"Неизвестный backend: {backend}")

    def get(self, url: str, referer: str | None = None, timeout: int = 30):
        headers = {}
        if referer:
            headers["Referer"] = referer
            headers["Sec-Fetch-Site"] = "same-origin"
        return self.session.get(url, headers=headers, timeout=timeout)


# --------------------------------------------------------------------------- #
# URL-утилиты
# --------------------------------------------------------------------------- #
def normalize(url: str) -> str:
    url, _ = urldefrag(url)
    if url.endswith("/index.html"):
        url = url[: -len("index.html")]
    return url


def in_scope(url: str, root: str) -> bool:
    if not url.startswith(root):
        return False
    path = urlparse(url).path.lower()
    return not any(path.endswith(ext) for ext in SKIP_EXT)


SAFE_NAME_RE = re.compile(r"[^a-zA-Z0-9._-]+")


def _safe_segment(name: str) -> str:
    """Чистим сегмент пути для использования в имени файла/папки."""
    name = SAFE_NAME_RE.sub("-", name).strip("-")
    return name or "index"


def url_to_path(url: str, root: str, output_dir: Path) -> Path:
    """
    Превращает URL в путь к .md файлу. Человеческие имена:
      /                        → index.md
      /features/               → features.md
      /api/base_model/         → api/base_model.md
      /api/base_model.html     → api/base_model.md
      /api/base_model/intro/   → api/base_model/intro.md
    """
    rel = url[len(root):].strip("/")
    if not rel:
        return output_dir / "index.md"

    parts = [_safe_segment(p) for p in rel.split("/") if p]
    if not parts:
        return output_dir / "index.md"

    # последний сегмент — имя файла; если на нём уже есть .html — снимаем
    last = parts[-1]
    if last.lower().endswith(".html"):
        last = last[:-5]
    parents = parts[:-1]

    return output_dir / Path(*parents) / f"{last}.md"


# --------------------------------------------------------------------------- #
# Парсинг
# --------------------------------------------------------------------------- #
def extract(html: str, page_url: str) -> tuple[str, str, list[str]]:
    """(title, html-фрагмент основного контента, все найденные ссылки)"""
    soup = BeautifulSoup(html, "html.parser")

    # Контентный контейнер: пробуем по убыванию специфичности.
    # .sl-markdown-content — Astro Starlight (pydantic.dev), .md-content - MkDocs Material,
    # .prose — Tailwind/Next.js, дальше общий fallback.
    content = (
        soup.select_one(".sl-markdown-content")
        or soup.select_one(".md-content__inner")
        or soup.select_one(".md-content")
        or soup.select_one("article")
        or soup.select_one(".prose")
        or soup.find("main")
        or soup.body
    )

    # Абсолютизируем ссылки и картинки В КОНТЕНТЕ — чтобы регулярка перелинковки
    # видела полные URL, а не /docs/...
    for a in content.find_all("a", href=True):
        a["href"] = urljoin(page_url, a["href"])
    for img in content.find_all("img", src=True):
        img["src"] = urljoin(page_url, img["src"])

    # Чистим шум: иконки якорей, кнопки фидбэка, мета-блоки.
    for sel in [".md-source-file", ".md-feedback", ".headerlink",
                ".md-content__button", "nav.md-tags",
                # Starlight-specific: всплывающие подсказки, кнопки "edit",
                ".annotation-popover-content", ".sl-link-button"]:
        for tag in content.select(sel):
            tag.decompose()

    title_tag = soup.find("h1")
    title = title_tag.get_text(strip=True) if title_tag else page_url

    # Ссылки для обхода — со всей страницы (включая сайдбар), чтобы найти все
    # доступные страницы документации. Для дедупликации потом разберёт seen.
    links = []
    for a in soup.find_all("a", href=True):
        links.append(normalize(urljoin(page_url, a["href"])))

    return title, str(content), links


def to_markdown(html_fragment: str) -> str:
    h = html2text.HTML2Text()
    h.body_width = 0
    h.ignore_images = False
    h.protect_links = True
    h.mark_code = True
    md = h.handle(html_fragment)
    md = re.sub(r"\[code\]", "\n```\n", md)
    md = re.sub(r"\[/code\]", "\n```\n", md)
    md = re.sub(r"\n{3,}", "\n\n", md)
    return md.strip() + "\n"


# --------------------------------------------------------------------------- #
# Перелинковка
# --------------------------------------------------------------------------- #
# Три формата ссылок, которые может породить html2text:
#   1) [text](https://url)               — обычная
#   2) [text](https://url "title")       — с title
#   3) <https://url>                     — автоссылка
# Картинки ![...](...) исключаются через (?<!\!).
MD_LINK_RE = re.compile(
    r"(?<!\!)\[([^\]]+)\]\((https?://[^)\s]+)(?:\s+\"[^\"]*\")?\)"
)
AUTOLINK_RE = re.compile(r"<(https?://[^>\s]+)>")


def _lookup_local(url: str, url_to_local: dict[str, Path]) -> Path | None:
    """
    Ищет URL в карте, пробуя варианты со слешом и без — потому что в md
    URL может быть https://x/a, а в карте https://x/a/ (или наоборот).
    """
    candidates = [url]
    if url.endswith("/"):
        candidates.append(url.rstrip("/"))
    else:
        candidates.append(url + "/")
    for c in candidates:
        if c in url_to_local:
            return url_to_local[c]
    return None


def relink_markdown(md: str, current_file: Path, url_to_local: dict[str, Path]
                    ) -> tuple[str, int, int]:
    """
    Возвращает (новый_md, число_найденных_внешних_ссылок, число_замен).
    """
    found = 0
    replaced = 0

    def make_local_link(url: str) -> str | None:
        url_no_frag, frag = urldefrag(url)
        url_no_frag = normalize(url_no_frag)
        local = _lookup_local(url_no_frag, url_to_local)
        if local is None:
            return None
        rel = os.path.relpath(local, start=current_file.parent).replace(os.sep, "/")
        if frag:
            rel = f"{rel}#{frag}"
        return f"./{rel}"

    def repl_md_link(m: re.Match) -> str:
        nonlocal found, replaced
        found += 1
        text, url = m.group(1), m.group(2)
        local = make_local_link(url)
        if local is None:
            return m.group(0)
        replaced += 1
        return f"[{text}]({url}) ([local]({local}))"

    def repl_autolink(m: re.Match) -> str:
        nonlocal found, replaced
        found += 1
        url = m.group(1)
        local = make_local_link(url)
        if local is None:
            return m.group(0)
        replaced += 1
        return f"<{url}> ([local]({local}))"

    md = MD_LINK_RE.sub(repl_md_link, md)
    md = AUTOLINK_RE.sub(repl_autolink, md)
    return md, found, replaced


# --------------------------------------------------------------------------- #
# Обход
# --------------------------------------------------------------------------- #
def crawl(start: str, output_dir: Path, max_pages: int,
          delay: float, backend: str, resume: bool) -> None:
    fetcher = Fetcher(backend)
    root = start if start.endswith("/") else start + "/"

    queue: deque[tuple[str, str | None]] = deque([(normalize(root), None)])
    seen: set[str] = {normalize(root)}
    saved, failed = 0, []

    # Проход 1: скачиваем всё, складываем сырой markdown и строим карту URL→путь
    url_to_local: dict[str, Path] = {}
    saved_pages: list[tuple[str, Path, str]] = []  # (url, path, raw_md)

    print("\n=== Проход 1: скачивание ===")
    while queue and saved < max_pages:
        url, referer = queue.popleft()
        target = url_to_path(url, root, output_dir)

        # resume: пропускаем уже скачанные файлы
        if resume and target.exists():
            url_to_local[url] = target
            saved += 1
            print(f"  [{saved}] · уже есть: {target.relative_to(output_dir)}")
            # ссылки из уже сохранённой страницы тоже надо учесть, чтобы продолжить обход
            try:
                existing = target.read_text(encoding="utf-8")
                for m in MD_LINK_RE.finditer(existing):
                    link = normalize(urldefrag(m.group(2))[0])
                    if link not in seen and in_scope(link, root):
                        seen.add(link)
                        queue.append((link, url))
            except OSError:
                pass
            continue

        try:
            if delay:
                time.sleep(delay)

            resp = fetcher.get(url, referer=referer)
            if resp.status_code != 200:
                raise RuntimeError(f"HTTP {resp.status_code}")
            if "html" not in resp.headers.get("Content-Type", ""):
                continue

            title, fragment, links = extract(resp.text, url)
            md = to_markdown(fragment)
            header = f"---\ntitle: {title}\nsource: {url}\n---\n\n"
            raw = header + md

            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_text(raw, encoding="utf-8")

            url_to_local[url] = target
            saved_pages.append((url, target, raw))
            saved += 1
            print(f"  [{saved}] ✓ {target.relative_to(output_dir)}  "
                  f"({len(queue)} в очереди)")

            for link in links:
                if link not in seen and in_scope(link, root):
                    seen.add(link)
                    queue.append((link, url))

        except Exception as e:
            failed.append((url, str(e)))
            print(f"  ✗ {url} — {e}", file=sys.stderr)

    # Проход 2: переписываем ссылки на локальные пути
    print(f"\n=== Проход 2: перелинковка ({len(saved_pages)} файлов) ===")
    print(f"  в карте URL→локальный путь: {len(url_to_local)} записей")
    relinked = 0
    total_found = 0
    total_replaced = 0
    # Чтобы перелинковка работала и для уже существующих файлов (resume),
    # пройдём по всем .md в output_dir, а не только по saved_pages.
    all_md = list(output_dir.rglob("*.md"))
    for path in all_md:
        try:
            raw = path.read_text(encoding="utf-8")
        except OSError:
            continue
        new, found, replaced = relink_markdown(raw, path, url_to_local)
        total_found += found
        total_replaced += replaced
        if new != raw:
            path.write_text(new, encoding="utf-8")
            relinked += 1
    print(f"  внешних ссылок найдено: {total_found}")
    print(f"  заменено (есть в карте): {total_replaced}")
    print(f"  переписано файлов: {relinked}")

    print(f"\nИтого. Сохранено: {saved}, ошибок: {len(failed)}, "
          f"в очереди осталось: {len(queue)}")
    if failed:
        print("Первые ошибки:")
        for u, e in failed[:10]:
            print(f"  - {u}: {e}")


# --------------------------------------------------------------------------- #
# CLI
# --------------------------------------------------------------------------- #
def main() -> int:
    p = argparse.ArgumentParser(description=__doc__,
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--start", required=True)
    p.add_argument("--output", default="./docs_md")
    p.add_argument("--max-pages", type=int, default=2000)
    p.add_argument("--delay", type=float, default=0.3)
    p.add_argument("--backend", choices=("requests", "curl_cffi"), default="requests")
    p.add_argument("--resume", action="store_true",
                   help="не перекачивать уже существующие файлы")
    args = p.parse_args()

    out = Path(args.output).resolve()
    out.mkdir(parents=True, exist_ok=True)

    print(f"→ корень обхода: {args.start}")
    print(f"→ сохраняю в:    {out}")
    print(f"→ бэкенд:        {args.backend}"
          f"{' (curl_cffi доступен)' if HAS_CURL_CFFI else ''}")
    if args.resume:
        print(f"→ режим resume:  пропускаю существующие файлы")

    preflight(args.start)
    crawl(args.start, out, args.max_pages, args.delay, args.backend, args.resume)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())