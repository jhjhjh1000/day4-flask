import sqlite3
import sys
from pathlib import Path

from crawler import MAX_ITEMS, RSS_URL, fetch_rss, parse_items

DB_PATH = Path(__file__).resolve().parent / "board.db"


def get_conn() -> sqlite3.Connection:
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def ensure_posts_table(conn: sqlite3.Connection) -> None:
    conn.execute(
        """CREATE TABLE IF NOT EXISTS posts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            content TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )"""
    )


def build_post_content(item: dict[str, str]) -> str:
    parts = []

    if item.get("summary"):
        parts.append(f"요약: {item['summary']}")
    if item.get("published"):
        parts.append(f"발행: {item['published']}")
    if item.get("link"):
        parts.append(f"링크: {item['link']}")
    if item.get("content"):
        parts.append("")
        parts.append(item["content"])

    return "\n".join(parts).strip()


def seed_posts() -> int:
    xml_content = fetch_rss(RSS_URL)
    items = parse_items(xml_content, limit=MAX_ITEMS)

    conn = get_conn()
    ensure_posts_table(conn)

    existing_titles = {
        row["title"] for row in conn.execute("SELECT title FROM posts").fetchall()
    }

    added_count = 0
    for item in items:
        title = item.get("title", "").strip()
        if not title or title in existing_titles:
            continue

        content = build_post_content(item)
        conn.execute("INSERT INTO posts (title, content) VALUES (?, ?)", (title, content))
        existing_titles.add(title)
        added_count += 1

    conn.commit()
    conn.close()
    return added_count


def main() -> None:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")

    added_count = seed_posts()
    print(f"{added_count}건 추가됨")


if __name__ == "__main__":
    main()
