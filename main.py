"""
Скачивает документацию рекурсивным обходом ссылок (BFS) и сохраняет
каждую страницу как .md, повторяя структуру URL папками.

Поддерживает два HTTP-бэкенда:
  • requests (по умолчанию) — лёгкий, без лишних зависимостей
  • curl_cffi (если установлен) — имитирует TLS-отпечаток Chrome,
    проходит большинство Cloudflare-челленджей

Установка:
    pip install requests beautifulsoup4 html2text brotli
    # опционально, для обхода Cloudflare:
    pip install curl_cffi

Запуск:
    python scrape_by_crawl.py --start https://docs.pydantic.dev/latest/ \
                              --output ./pydantic_docs
    # с curl_cffi:
    python scrape_by_crawl.py --start https://docs.pydantic.dev/latest/ \
                              --output ./pydantic_docs --backend curl_cffi
"""

from __future__ import annotations

# Принудительно IPv4 (если у среды сломан IPv6) — ДО import requests
import urllib3.util.connection
urllib3.util.connection.HAS_IPV6 = False

import argparse
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

# опционально — curl_cffi для имитации TLS-отпечатка Chrome
try:
    from curl_cffi import requests as cffi_requests  # type: ignore
    HAS_CURL_CFFI = True
except ImportError:
    HAS_CURL_CFFI = False


# --------------------------------------------------------------------------- #
# Заголовки — имитируем Firefox 124 на Linux. Cloudflare смотрит на согласованность
# UA и набора заголовков, поэтому копируем именно те, что реально шлёт браузер.
# --------------------------------------------------------------------------- #
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

# Расширения, которые не страницы — пропускаем
SKIP_EXT = {".png", ".jpg", ".jpeg", ".gif", ".svg", ".ico", ".webp",
            ".pdf", ".zip", ".tar", ".gz", ".css", ".js", ".woff",
            ".woff2", ".ttf", ".mp4", ".webm", ".xml", ".json"}


# --------------------------------------------------------------------------- #
# Сеть
# --------------------------------------------------------------------------- #
def preflight(url: str) -> None:
    """Быстрая проверка, что хост достижим. Человекочитаемая ошибка вместо трейсбэка."""
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
            f"Проверьте сеть/прокси/IPv6. Если WSL — попробуйте 'wsl --shutdown'."
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
    """Унифицированный фетчер поверх requests или curl_cffi."""

    def __init__(self, backend: str):
        self.backend = backend
        if backend == "requests":
            self.session = make_requests_session()
        elif backend == "curl_cffi":
            if not HAS_CURL_CFFI:
                sys.exit("curl_cffi не установлен. Установите: pip install curl_cffi")
            # curl_cffi подделывает TLS-отпечаток Chrome 124
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


def url_to_path(url: str, root: str, output_dir: Path) -> Path:
    rel = url[len(root):].strip("/")
    if not rel:
        return output_dir / "index.md"
    if urlparse(url).path.endswith("/"):
        return output_dir / rel / "index.md"
    return output_dir / f"{rel}.md"


# --------------------------------------------------------------------------- #
# Парсинг HTML и конвертация
# --------------------------------------------------------------------------- #
def extract(html: str, page_url: str) -> tuple[str, str, list[str]]:
    """(title, html-фрагмент основного контента, все найденные ссылки)"""
    soup = BeautifulSoup(html, "html.parser")
    article = soup.find("article") or soup.find("main") or soup.body

    # абсолютизируем ссылки и картинки
    for a in article.find_all("a", href=True):
        a["href"] = urljoin(page_url, a["href"])
    for img in article.find_all("img", src=True):
        img["src"] = urljoin(page_url, img["src"])

    # вычищаем шум (специфично для MkDocs Material, но безвредно для других)
    for sel in [".md-source-file", ".md-feedback", ".headerlink",
                ".md-content__button", "nav.md-tags"]:
        for tag in article.select(sel):
            tag.decompose()

    title_tag = soup.find("h1")
    title = title_tag.get_text(strip=True) if title_tag else page_url

    # ссылки ищем со всей страницы, включая навигацию
    links = []
    for a in soup.find_all("a", href=True):
        links.append(normalize(urljoin(page_url, a["href"])))

    return title, str(article), links


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


def save(url: str, root: str, content: str, output_dir: Path) -> Path:
    path = url_to_path(url, root, output_dir)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    return path


# --------------------------------------------------------------------------- #
# Обход
# --------------------------------------------------------------------------- #
def crawl(start: str, output_dir: Path, max_pages: int,
          delay: float, backend: str) -> None:
    fetcher = Fetcher(backend)
    root = start if start.endswith("/") else start + "/"

    # очередь хранит пары (url, referer) — реальный браузер всегда шлёт Referer
    queue: deque[tuple[str, str | None]] = deque([(normalize(root), None)])
    seen: set[str] = {normalize(root)}
    saved, failed = 0, []

    while queue and saved < max_pages:
        url, referer = queue.popleft()
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
            path = save(url, root, header + md, output_dir)
            saved += 1
            print(f"  [{saved}] ✓ {path.relative_to(output_dir)}  "
                  f"({len(queue)} в очереди)")

            for link in links:
                if link not in seen and in_scope(link, root):
                    seen.add(link)
                    queue.append((link, url))  # текущий URL станет Referer

        except Exception as e:
            failed.append((url, str(e)))
            print(f"  ✗ {url} — {e}", file=sys.stderr)

    print(f"\nГотово. Сохранено: {saved}, ошибок: {len(failed)}, "
          f"в очереди: {len(queue)}")
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
    p.add_argument("--start", required=True,
                   help="стартовый URL (он же корень области обхода)")
    p.add_argument("--output", default="./docs_md", help="папка для .md файлов")
    p.add_argument("--max-pages", type=int, default=2000)
    p.add_argument("--delay", type=float, default=0.3,
                   help="задержка между запросами, сек (вежливость к серверу)")
    p.add_argument("--backend", choices=("requests", "curl_cffi"), default="requests",
                   help="HTTP-бэкенд: curl_cffi надёжнее против Cloudflare")
    args = p.parse_args()

    out = Path(args.output).resolve()
    out.mkdir(parents=True, exist_ok=True)

    print(f"→ корень обхода: {args.start}")
    print(f"→ сохраняю в:    {out}")
    print(f"→ бэкенд:        {args.backend}"
          f"{' (curl_cffi доступен)' if HAS_CURL_CFFI else ''}")

    preflight(args.start)
    crawl(args.start, out, args.max_pages, args.delay, args.backend)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())