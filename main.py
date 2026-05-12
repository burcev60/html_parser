"""
Скачивает документацию рекурсивным обходом ссылок (BFS) и сохраняет
каждую страницу как .md.

Особенности:
  • Универсальный парсер навигации: имена файлов и папок с числовыми
    префиксами в порядке сайдбара (01_get-started/01_welcome.md).
    Работает для MkDocs, Docusaurus, Starlight, VuePress и др.
  • Slug-имена (нижний регистр, дефисы): 01_welcome-to-pydantic.md
  • Fallback на URL-структуру, если навигацию извлечь не удалось.
  • Перелинковка: ссылки на скачанные страницы получают рядом
    локальную ссылку. Якоря внутри той же страницы становятся #anchor.
  • Два бэкенда: requests / curl_cffi (для Cloudflare).

Установка:
    pip install requests beautifulsoup4 html2text brotli
    pip install curl_cffi   # опционально, для Cloudflare

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
import unicodedata
from collections import deque
from pathlib import Path
from urllib.parse import urlparse, urljoin, urldefrag

import html2text
import requests
from bs4 import BeautifulSoup, Tag
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

try:
    from curl_cffi import requests as cffi_requests  # type: ignore
    HAS_CURL_CFFI = True
except ImportError:
    HAS_CURL_CFFI = False

try:
    from playwright.sync_api import sync_playwright  # type: ignore
    HAS_PLAYWRIGHT = True
except ImportError:
    HAS_PLAYWRIGHT = False


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
        sys.exit(f"Нет TCP-соединения с {host}:443 — {e}")


def make_requests_session() -> requests.Session:
    s = requests.Session()
    retry = Retry(total=5, connect=5, read=5, backoff_factor=1.0,
                  status_forcelist=(429, 500, 502, 503, 504),
                  allowed_methods=frozenset(["GET"]),
                  respect_retry_after_header=True)
    adapter = HTTPAdapter(max_retries=retry, pool_connections=20, pool_maxsize=20)
    s.mount("https://", adapter)
    s.mount("http://", adapter)
    s.headers.update(DEFAULT_HEADERS)
    return s


class _FakeResponse:
    """Минимальный аналог requests.Response для Playwright-бэкенда."""
    def __init__(self, text: str, status: int, content_type: str = "text/html"):
        self.text = text
        self.status_code = status
        self.headers = {"Content-Type": content_type}


class Fetcher:
    def __init__(self, backend: str):
        self.backend = backend
        self._pw = None  # ссылка на playwright, если используется

        if backend == "requests":
            self.session = make_requests_session()
        elif backend == "curl_cffi":
            if not HAS_CURL_CFFI:
                sys.exit("curl_cffi не установлен. pip install curl_cffi")
            self.session = cffi_requests.Session(impersonate="chrome124")
            self.session.headers.update(DEFAULT_HEADERS)
        elif backend == "playwright":
            if not HAS_PLAYWRIGHT:
                sys.exit("playwright не установлен. pip install playwright && "
                         "playwright install chromium")
            self._pw = sync_playwright().start()
            self._browser = self._pw.chromium.launch(headless=True)
            self._context = self._browser.new_context(
                user_agent=DEFAULT_HEADERS["User-Agent"],
                viewport={"width": 1280, "height": 900},
                locale="en-US",
            )
            # Блокируем тяжёлые ресурсы и трекинг — это ускоряет загрузку и
            # помогает странице "стабилизироваться" быстрее. Нам нужен HTML
            # и навигационные ссылки, картинки/шрифты/видео не нужны.
            BLOCKED_RESOURCE_TYPES = {"image", "media", "font"}
            BLOCKED_HOSTS = (
                "google-analytics.com", "googletagmanager.com",
                "doubleclick.net", "facebook.com", "facebook.net",
                "hotjar.com", "segment.io", "segment.com",
                "mixpanel.com", "amplitude.com", "fullstory.com",
                "intercom.io", "intercom.com", "sentry.io",
                "datadoghq.com", "plausible.io", "posthog.com",
            )

            def _route(route):  # type: ignore
                req = route.request
                if req.resource_type in BLOCKED_RESOURCE_TYPES:
                    return route.abort()
                if any(h in req.url for h in BLOCKED_HOSTS):
                    return route.abort()
                return route.continue_()

            self._context.route("**/*", _route)
        else:
            sys.exit(f"Неизвестный backend: {backend}")

    def close(self) -> None:
        if self.backend == "playwright" and self._pw is not None:
            try:
                self._context.close()
                self._browser.close()
                self._pw.stop()
            except Exception:
                pass

    def get(self, url: str, referer: str | None = None, timeout: int = 30):
        if self.backend == "playwright":
            page = self._context.new_page()
            try:
                extra_headers = {"Accept-Language": "en-US,en;q=0.9,ru;q=0.8"}
                if referer:
                    extra_headers["Referer"] = referer
                page.set_extra_http_headers(extra_headers)

                # NB: НЕ используем wait_until="networkidle" — на современных
                # SPA сайтах с аналитикой/телеметрией сеть никогда не стихает
                # полностью, и goto падает по таймауту. Стратегия:
                #   1) ждём domcontentloaded — это быстро и надёжно
                #   2) пробуем дождаться контентного селектора (h1/main/article)
                #   3) если не пришёл — даём короткое доп-время и всё равно
                #      берём что есть
                resp = page.goto(url, wait_until="domcontentloaded",
                                 timeout=timeout * 1000)
                status = resp.status if resp else 200

                # Ждём появления реального контента. Перебираем селекторы:
                # сначала самые специфичные, потом общие.
                content_appeared = False
                for sel in ["article", "main h1", "main", "h1",
                            "[class*=markdown]", "[class*=prose]"]:
                    try:
                        page.wait_for_selector(sel, timeout=3000, state="visible")
                        content_appeared = True
                        break
                    except Exception:
                        continue

                if not content_appeared:
                    # последняя попытка — просто подождать чуть-чуть, может JS успеет
                    try:
                        page.wait_for_timeout(2000)
                    except Exception:
                        pass

                html = page.content()
                return _FakeResponse(html, status, "text/html")
            finally:
                page.close()

        headers = {}
        if referer:
            headers["Referer"] = referer
            headers["Sec-Fetch-Site"] = "same-origin"
        return self.session.get(url, headers=headers, timeout=timeout)


# --------------------------------------------------------------------------- #
# URL и имена файлов
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


def slugify(text: str, max_len: int = 60) -> str:
    """
    Превращает заголовок в slug, пригодный для имени файла.
    Сохраняет Unicode-буквы (кириллицу и т.п.), так что 'Ресурсы' → 'ресурсы',
    а не пустота. Пробелы и пунктуация → дефис.
    """
    # NFKC, а не NFKD: NFKD разлагает 'ё' на 'е'+'¨' и теряет смысл.
    # NFKC компонует обратно и нормализует совместимые символы (полноширинные и т.п.).
    text = unicodedata.normalize("NFKC", text).lower()
    # Оставляем любые "буквы" (\w в Python с re.UNICODE по умолчанию) и цифры.
    # Всё остальное (пробелы, пунктуация, эмодзи) → дефис.
    text = re.sub(r"[^\w\d]+", "-", text, flags=re.UNICODE)
    # подчёркивания превратим в дефисы, чтобы префикс `01_` остался единственным разделителем
    text = text.replace("_", "-").strip("-")
    return text[:max_len] or "page"


def url_fallback_segments(url: str, root: str) -> list[str]:
    """Если URL нет в навигации — формируем сегменты из URL-пути."""
    rel = url[len(root):].strip("/")
    if not rel:
        return ["index"]
    segs = [slugify(s) for s in rel.split("/") if s]
    return segs or ["index"]


# --------------------------------------------------------------------------- #
# Универсальный парсер навигации
# --------------------------------------------------------------------------- #
NAV_CANDIDATES = [
    "nav",
    "aside",
    "[role=navigation]",
    "[class*=sidebar]",
    "[class*=menu]",
    "[class*=toc]",
    "[class*=navigation]",
]


def find_nav_container(soup: BeautifulSoup, root: str) -> Tag | None:
    """
    Находит контейнер навигации, перебирая стратегии от более точной к
    более общей:
      1) Несколько элементов с одинаковым id (Mintlify-подобные сайты, где
         каждая группа сайдбара — <ul id="sidebar-group">) → их общий родитель.
      2) Стандартные кандидаты: <nav>, <aside>, или класс содержит
         sidebar/menu/toc/navigation. Выбирается тот, что с максимумом doc-ссылок.
      3) Самый плотный по doc-ссылкам контейнер вообще (последний fallback).
    """
    def tag_priority(t: Tag) -> int:
        if t.name == "nav":
            return 3
        if t.name == "aside":
            return 2
        return 1

    def count_doc_links(el: Tag) -> int:
        n = 0
        for a in el.find_all("a", href=True):
            href = a["href"].strip()
            if not href or href.startswith("#") or href.startswith("javascript:"):
                continue
            absurl = normalize(urljoin(root, href))
            if absurl.startswith(root) and "#" not in href:
                n += 1
        return n

    # === Стратегия 1: повторяющийся id-шаблон ===
    # Mintlify / некоторые другие движки делают сайдбар из нескольких <ul>
    # или <div> с одинаковым id (что валидно нарушает HTML-стандарт, но
    # повсеместно встречается). Это очень сильный сигнал.
    id_groups: dict[str, list[Tag]] = {}
    for el in soup.find_all(["ul", "ol", "div", "section"]):
        eid = el.get("id", "")
        if eid:
            id_groups.setdefault(eid, []).append(el)

    def find_common_parent(elements: list[Tag]) -> Tag | None:
        if len(elements) < 2:
            return None
        rest = elements[1:]
        for p in elements[0].parents:
            if p.name in ("body", "html"):
                return None
            if all(p in el.parents for el in rest):
                return p
        return None

    id_candidates: list[tuple[int, int, Tag]] = []  # (doc_links, depth, parent)
    for key, els in id_groups.items():
        if len(els) < 2:
            continue
        group_links = sum(count_doc_links(e) for e in els)
        if group_links < 5:
            continue
        parent = find_common_parent(els)
        if parent is None:
            continue
        parent_links = count_doc_links(parent)
        depth = len(list(parent.parents))
        id_candidates.append((parent_links, depth, parent))

    if id_candidates:
        id_candidates.sort(key=lambda p: (p[0], p[1]), reverse=True)
        return id_candidates[0][2]

    # === Стратегия 2: стандартные семантические кандидаты ===
    best: Tag | None = None
    best_count = 0
    seen_elements: set[int] = set()

    for sel in NAV_CANDIDATES:
        for el in soup.select(sel):
            if id(el) in seen_elements:
                continue
            seen_elements.add(id(el))
            if el.name in ("body", "html"):
                continue
            n = count_doc_links(el)
            if n < 3:
                continue

            replace = False
            if n > best_count:
                replace = True
            elif n == best_count and best is not None:
                if tag_priority(el) > tag_priority(best):
                    replace = True
                elif tag_priority(el) == tag_priority(best):
                    if len(list(el.parents)) < len(list(best.parents)):
                        replace = True
            if replace:
                best = el
                best_count = n

    if best is not None:
        return best

    # === Стратегия 3: самый плотный по doc-ссылкам контейнер ===
    candidate: Tag | None = None
    candidate_count = 0
    for el in soup.find_all(["div", "section", "ul"]):
        if el.name in ("body", "html"):
            continue
        n = count_doc_links(el)
        if n < 5:
            continue
        if n > candidate_count:
            candidate = el
            candidate_count = n
        elif n == candidate_count and candidate is not None:
            if len(list(el.parents)) > len(list(candidate.parents)):
                candidate = el

    return candidate


def parse_nav_order(soup: BeautifulSoup, root: str
                    ) -> dict[str, list[str]]:
    """
    Извлекает иерархию навигации в виде {url: [сегмент_пути, ...]}.

    Каждый сегмент — "NN_slug" (порядковый номер + slug заголовка).
    Возвращает пустой dict, если навигация не найдена.

    Стратегия: идём по DOM nav-контейнера в порядке появления.
    Узлы делим на три типа:
      • ссылка-страница: <a href=...> ведёт на нашу документацию,
        и у неё нет вложенного <ul> на её уровне
      • групповой заголовок: текстовый узел (<a>, <span>, <summary>,
        <button>, <h*>), у которого рядом или внутри ближайшего родителя
        есть <ul>/<ol> с дочерними элементами
      • прочее: игнорируем
    """
    nav = find_nav_container(soup, root)
    if nav is None:
        return {}

    def link_depth(tag: Tag) -> int:
        depth = 0
        parent = tag.parent
        while parent is not None and parent is not nav:
            if parent.name in ("ul", "ol", "details"):
                depth += 1
            parent = parent.parent
        return depth

    def has_nested_list(tag: Tag) -> bool:
        """У этого узла или его ближайшего сиблинга есть вложенный <ul>/<ol>?"""
        # внутри самого тега
        if tag.find(["ul", "ol"], recursive=True):
            return True
        # сиблинги в том же родителе (например <span> + <ul> в <li>)
        if tag.parent:
            for sib in tag.parent.find_all(["ul", "ol"], recursive=False):
                if sib is not tag:
                    return True
        return False

    entries: list[tuple[int, str, str | None]] = []

    for el in nav.descendants:
        if not isinstance(el, Tag):
            continue

        # сам nav-контейнер и вложенные nav/aside — это структурные обёртки,
        # они не дают текстового заголовка для группы
        if el is nav or el.name in ("nav", "aside"):
            continue

        text = el.get_text(" ", strip=True)
        if not text:
            continue

        # Ссылка
        if el.name == "a" and el.has_attr("href"):
            href = el["href"].strip()
            if not href or href.startswith("#") or href.startswith("javascript:"):
                if has_nested_list(el):
                    entries.append((link_depth(el), text, None))
                continue
            absurl = normalize(urljoin(root, href))
            if not absurl.startswith(root):
                continue
            entries.append((link_depth(el), text, absurl))
            continue

        # Группирующие заголовки. Берём узкий набор:
        #   - <summary> в <details>
        #   - <label> с классом md-nav__title или подобным (MkDocs Material:
        #     label служит "кликабельным" заголовком свёрнутого раздела,
        #     внутри <li class*=nested> рядом с <input type=checkbox> и <nav>)
        #   - заголовки h2..h6
        #   - <span>/<button> с признаками заголовка (label/title/heading/group в классе/role)
        #   - <span>/<button>/<label>, прямой ребёнок <li>, рядом — вложенный список или nav
        if el.name in ("summary", "h2", "h3", "h4", "h5", "h6"):
            entries.append((link_depth(el), text, None))
            continue

        if el.name == "label":
            classes = " ".join(el.get("class", []))
            # либо явный класс заголовка, либо label рядом с вложенным nav/ul
            is_nav_title = re.search(r"title|nav__link|label|heading", classes, re.I)
            is_li_label = (el.parent and el.parent.name == "li"
                           and el.parent.find(["ul", "ol", "nav"], recursive=False))
            if is_nav_title or is_li_label:
                entries.append((link_depth(el), text, None))
            continue

        if el.name in ("span", "button"):
            classes = " ".join(el.get("class", []))
            role = el.get("role", "")
            looks_like_heading = (
                re.search(r"label|title|heading|group|section", classes, re.I)
                or role in ("heading", "group")
            )
            # либо это прямой ребёнок <li>, рядом с которым есть вложенный список или nav
            is_li_label = (el.parent and el.parent.name == "li"
                           and el.parent.find(["ul", "ol", "nav"], recursive=False))
            if looks_like_heading or is_li_label:
                inner_a = el.find("a")
                if inner_a is None or inner_a.get_text(" ", strip=True) != text:
                    entries.append((link_depth(el), text, None))

    if not entries:
        return {}

    # Дедупликация подряд идущих одинаковых записей (когда групповой заголовок
    # обёрнут в несколько контейнеров и матчится несколько раз)
    deduped: list[tuple[int, str, str | None]] = []
    for e in entries:
        if not deduped or deduped[-1] != e:
            deduped.append(e)
    entries = deduped

    counters: dict[int, int] = {}
    headers: dict[int, str] = {}

    def use_counter(depth: int) -> int:
        counters[depth] = counters.get(depth, 0) + 1
        return counters[depth]

    def reset_below(depth: int) -> None:
        for d in list(counters.keys()):
            if d > depth:
                del counters[d]
        for d in list(headers.keys()):
            if d > depth:
                del headers[d]

    result: dict[str, list[str]] = {}

    for depth, text, url in entries:
        if url is None:
            reset_below(depth)
            idx = use_counter(depth)
            headers[depth] = f"{idx:02d}_{slugify(text)}"
        else:
            reset_below(depth)
            idx = use_counter(depth)
            page_segment = f"{idx:02d}_{slugify(text)}"
            path = [headers[d] for d in sorted(headers) if d < depth]
            path.append(page_segment)
            result.setdefault(url, path)

    return result


# --------------------------------------------------------------------------- #
# url_to_path с учётом nav
# --------------------------------------------------------------------------- #
def url_to_path(url: str, root: str, output_dir: Path,
                nav_map: dict[str, list[str]] | None) -> Path:
    """
    Если URL есть в nav_map — путь по навигации (01_get-started/02_why.md).
    Иначе — fallback на URL-структуру (api/base_model.md).
    """
    rel = url[len(root):].strip("/")
    if not rel:
        return output_dir / "index.md"

    # Пробуем найти в nav_map с учётом разных форм URL
    nav_path = None
    for candidate in (url, url.rstrip("/"), url + "/"):
        if nav_map and candidate in nav_map:
            nav_path = nav_map[candidate]
            break

    if nav_path is not None:
        # последний сегмент → имя файла .md, остальные → папки
        if len(nav_path) == 1:
            return output_dir / f"{nav_path[0]}.md"
        return output_dir / Path(*nav_path[:-1]) / f"{nav_path[-1]}.md"

    # fallback: URL-структура
    segs = url_fallback_segments(url, root)
    if len(segs) == 1:
        return output_dir / "_unsorted" / f"{segs[0]}.md"
    return output_dir / "_unsorted" / Path(*segs[:-1]) / f"{segs[-1]}.md"


# --------------------------------------------------------------------------- #
# Парсинг страницы
# --------------------------------------------------------------------------- #
def extract(html: str, page_url: str) -> tuple[str, str, list[str]]:
    soup = BeautifulSoup(html, "html.parser")

    content = (
        soup.select_one(".sl-markdown-content")        # Astro Starlight
        or soup.select_one(".md-content__inner")       # MkDocs Material
        or soup.select_one(".md-content")
        or soup.select_one("article")
        or soup.select_one("#content-area")            # Mintlify
        or soup.select_one("#body-content")            # Mintlify (внешний)
        or soup.select_one("[id*=content-area]")
        or soup.select_one(".prose")
        or soup.find("main")
        or soup.body
    )

    for a in content.find_all("a", href=True):
        a["href"] = urljoin(page_url, a["href"])
    for img in content.find_all("img", src=True):
        img["src"] = urljoin(page_url, img["src"])

    for sel in [".md-source-file", ".md-feedback", ".headerlink",
                ".md-content__button", "nav.md-tags",
                ".annotation-popover-content", ".sl-link-button"]:
        for tag in content.select(sel):
            tag.decompose()

    title_tag = soup.find("h1")
    title = title_tag.get_text(strip=True) if title_tag else page_url

    links = []
    for a in soup.find_all("a", href=True):
        links.append(normalize(urljoin(page_url, a["href"])))

    return title, str(content), links


def to_markdown(html_fragment: str) -> str:
    h = html2text.HTML2Text()
    h.body_width = 0
    h.ignore_images = False
    h.protect_links = False
    h.mark_code = True
    md = h.handle(html_fragment)
    md = re.sub(r"\[code\]", "\n```\n", md)
    md = re.sub(r"\[/code\]", "\n```\n", md)
    md = re.sub(r"\n{3,}", "\n\n", md)
    return md.strip() + "\n"


# --------------------------------------------------------------------------- #
# Перелинковка
# --------------------------------------------------------------------------- #
MD_LINK_RE = re.compile(
    r"(?<!\!)\[([^\]]*)\]"
    r"\(<?(https?://[^)>\s]+)>?"
    r"(?:\s+\"[^\"]*\")?\)"
)
AUTOLINK_RE = re.compile(r"<(https?://[^>\s]+)>")
DUP_LOCAL_RE = re.compile(r"(\s*\(\[local\]\([^)]+\)\))\1+")


def _lookup_local(url: str, url_to_local: dict[str, Path]) -> Path | None:
    for c in (url, url.rstrip("/"), url + "/"):
        if c in url_to_local:
            return url_to_local[c]
    return None


def relink_markdown(md: str, current_file: Path, current_url: str,
                    url_to_local: dict[str, Path]) -> tuple[str, int, int]:
    found = 0
    replaced = 0
    current_norm = normalize(urldefrag(current_url)[0]) if current_url else ""

    def is_self_link(url: str) -> bool:
        if not current_norm:
            return False
        target = normalize(urldefrag(url)[0])
        return target == current_norm or target.rstrip("/") == current_norm.rstrip("/")

    def make_local(url: str) -> tuple[str, str] | None:
        url_no_frag, frag = urldefrag(url)
        local = _lookup_local(normalize(url_no_frag), url_to_local)
        if local is None:
            return None
        rel = os.path.relpath(local, start=current_file.parent).replace(os.sep, "/")
        if frag:
            rel = f"{rel}#{frag}"
        return url, f"./{rel}"

    def repl_md(m: re.Match) -> str:
        nonlocal found, replaced
        text, url = m.group(1), m.group(2)
        if is_self_link(url):
            _, frag = urldefrag(url)
            anchor = f"#{frag}" if frag else ""
            if not text.strip():
                return anchor or ""
            return f"[{text}]({anchor})" if anchor else text
        found += 1
        result = make_local(url)
        if result is None:
            return f"<{url}>" if not text.strip() else f"[{text}]({url})"
        replaced += 1
        clean_url, local = result
        if not text.strip():
            return f"<{clean_url}> ([local]({local}))"
        return f"[{text}]({clean_url}) ([local]({local}))"

    def repl_auto(m: re.Match) -> str:
        nonlocal found, replaced
        url = m.group(1)
        if is_self_link(url):
            _, frag = urldefrag(url)
            return f"#{frag}" if frag else ""
        found += 1
        result = make_local(url)
        if result is None:
            return m.group(0)
        replaced += 1
        _, local = result
        return f"<{url}> ([local]({local}))"

    md = MD_LINK_RE.sub(repl_md, md)
    md = AUTOLINK_RE.sub(repl_auto, md)
    return md, found, replaced


def cleanup_duplicates(md: str) -> str:
    return DUP_LOCAL_RE.sub(r"\1", md)


# --------------------------------------------------------------------------- #
# Обход
# --------------------------------------------------------------------------- #
def crawl(start: str, output_dir: Path, max_pages: int,
          delay: float, backend: str, resume: bool) -> None:
    fetcher = Fetcher(backend)
    try:
        _crawl_impl(fetcher, start, output_dir, max_pages, delay, resume)
    finally:
        fetcher.close()


def _crawl_impl(fetcher: Fetcher, start: str, output_dir: Path,
                max_pages: int, delay: float, resume: bool) -> None:
    root = start if start.endswith("/") else start + "/"

    # Сначала качаем стартовую страницу и извлекаем навигацию для всего сайта.
    # Эту карту используем для именования файлов всех остальных страниц.
    print("→ загружаю стартовую страницу для построения навигации...")
    start_resp = fetcher.get(normalize(root))
    if start_resp.status_code != 200:
        sys.exit(f"Стартовая страница вернула HTTP {start_resp.status_code}")
    start_soup = BeautifulSoup(start_resp.text, "html.parser")
    nav_map = parse_nav_order(start_soup, root)
    if nav_map:
        print(f"  навигация найдена: {len(nav_map)} страниц")
    else:
        print(f"  навигация НЕ найдена — fallback на URL-структуру")

    queue: deque[tuple[str, str | None]] = deque([(normalize(root), None)])
    seen: set[str] = {normalize(root)}
    saved, failed = 0, []
    url_to_local: dict[str, Path] = {}
    saved_pages: list[tuple[str, Path]] = []

    # Сохраним уже загруженную стартовую, чтобы не качать второй раз.
    cached_start = start_resp

    print("\n=== Проход 1: скачивание ===")
    while queue and saved < max_pages:
        url, referer = queue.popleft()
        target = url_to_path(url, root, output_dir, nav_map)

        if resume and target.exists():
            url_to_local[url] = target
            saved += 1
            print(f"  [{saved}] · уже есть: {target.relative_to(output_dir)}")
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
            # стартовую страницу не качаем заново
            if cached_start is not None and url == normalize(root):
                resp = cached_start
                cached_start = None
            else:
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

            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_text(header + md, encoding="utf-8")

            url_to_local[url] = target
            saved_pages.append((url, target))
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

    # Проход 2: перелинковка
    print(f"\n=== Проход 2: перелинковка ===")
    print(f"  в карте URL→путь: {len(url_to_local)} записей")
    local_to_url = {v: k for k, v in url_to_local.items()}
    all_md = list(output_dir.rglob("*.md"))
    relinked, total_found, total_replaced = 0, 0, 0
    for path in all_md:
        try:
            raw = path.read_text(encoding="utf-8")
        except OSError:
            continue
        current_url = local_to_url.get(path)
        if current_url is None:
            m = re.search(r"^source:\s*(\S+)", raw, flags=re.MULTILINE)
            current_url = m.group(1) if m else ""
        new, f, r = relink_markdown(raw, path, current_url, url_to_local)
        new = cleanup_duplicates(new)
        total_found += f
        total_replaced += r
        if new != raw:
            path.write_text(new, encoding="utf-8")
            relinked += 1
    print(f"  внешних ссылок найдено: {total_found}")
    print(f"  заменено: {total_replaced}")
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
    p.add_argument("--backend",
                   choices=("requests", "curl_cffi", "playwright"),
                   default="requests",
                   help="HTTP-бэкенд. playwright — рендеринг JS (для SPA)")
    p.add_argument("--resume", action="store_true")
    args = p.parse_args()

    out = Path(args.output).resolve()
    out.mkdir(parents=True, exist_ok=True)

    backends_available = []
    backends_available.append("requests")
    if HAS_CURL_CFFI:
        backends_available.append("curl_cffi")
    if HAS_PLAYWRIGHT:
        backends_available.append("playwright")
    print(f"→ корень обхода: {args.start}")
    print(f"→ сохраняю в:    {out}")
    print(f"→ бэкенд:        {args.backend}  "
          f"(доступны: {', '.join(backends_available)})")
    if args.resume:
        print(f"→ режим resume")

    preflight(args.start)
    crawl(args.start, out, args.max_pages, args.delay, args.backend, args.resume)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())