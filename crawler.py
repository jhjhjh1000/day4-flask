import html
import sys
from email.utils import parsedate_to_datetime

import requests
from bs4 import BeautifulSoup

RSS_URL = "https://www.yna.co.kr/rss/news.xml"
MAX_ITEMS = 10
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
}


def fetch_rss(url: str) -> bytes:
    response = requests.get(url, timeout=10, headers=HEADERS)
    response.raise_for_status()
    return response.content


def fetch_article_content(url: str) -> str:
    try:
        response = requests.get(url, timeout=10, headers=HEADERS)
        response.raise_for_status()
    except Exception:
        return "본문을 가져오지 못했습니다."

    soup = BeautifulSoup(response.content, "html.parser")

    for tag in soup(["script", "style", "noscript", "header", "footer", "nav", "aside"]):
        tag.decompose()

    candidates = []
    for selector in [
        "#articleWrap",
        "article",
        "main",
        "#articleBodyContents",
        ".article-body",
        ".article_body",
        ".newsct_article",
        "#dic_area",
    ]:
        selected = soup.select(selector)
        candidates.extend(selected)

    paragraphs = []

    if candidates:
        best = max(candidates, key=lambda tag: len(tag.get_text(" ", strip=True)))
        paragraphs = [p.get_text(" ", strip=True) for p in best.find_all("p")]
        paragraphs = [p for p in paragraphs if len(p) > 20]

    if not paragraphs:
        paragraphs = [p.get_text(" ", strip=True) for p in soup.find_all("p")]
        paragraphs = [p for p in paragraphs if len(p) > 40]

    if not paragraphs:
        text = soup.get_text(" ", strip=True)
        return (text[:1200] + "...") if len(text) > 1200 else text

    content = "\n".join(paragraphs[:12])
    return (content[:4000] + "...") if len(content) > 4000 else content


def parse_items(xml_content: bytes, limit: int = 10) -> list[dict[str, str]]:
    soup = BeautifulSoup(xml_content, "xml")
    items = soup.find_all("item")[:limit]

    parsed = []
    for item in items:
        title = (item.title.text if item.title else "").strip()
        summary_raw = (item.description.text if item.description else "").strip()
        summary_text = BeautifulSoup(summary_raw, "html.parser").get_text(" ", strip=True)
        summary = html.unescape(summary_text)
        summary = summary.replace("(서울=연합뉴스)", "").strip()
        link = (item.link.text if item.link else "").strip()
        pub_date_raw = (item.pubDate.text if item.pubDate else "").strip()

        if pub_date_raw:
            try:
                pub_date = parsedate_to_datetime(pub_date_raw).strftime("%Y-%m-%d %H:%M:%S %z")
            except Exception:
                pub_date = pub_date_raw
        else:
            pub_date = ""

        content = fetch_article_content(link) if link else "본문 링크가 없습니다."

        parsed.append(
            {
                "title": title,
                "summary": summary,
                "link": link,
                "published": pub_date,
                "content": content,
            }
        )

    return parsed


def print_news(items: list[dict[str, str]]) -> None:
    print("=" * 80)
    print(f"Korean RSS News Top {len(items)}")
    print("=" * 80)

    for idx, news in enumerate(items, start=1):
        print(f"[{idx}] {news['title']}")
        print(f"요약: {news['summary']}")
        print(f"링크: {news['link']}")
        print(f"발행: {news['published']}")
        print("본문:")
        print(news["content"])
        print("-" * 80)


def main() -> None:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")

    xml_content = fetch_rss(RSS_URL)
    items = parse_items(xml_content, limit=MAX_ITEMS)
    print_news(items)


if __name__ == "__main__":
    main()
