import os
import sqlite3
from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


def get_db():
    conn = sqlite3.connect("board.db")
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    conn = get_db()
    conn.execute(
        """CREATE TABLE IF NOT EXISTS posts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            content TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )"""
    )
    conn.commit()
    conn.close()


@app.route("/")
def list_posts():
    page_size = 10
    page = request.args.get("page", default=1, type=int) or 1
    page = max(page, 1)
    q = (request.args.get("q", "") or "").strip()
    sort = (request.args.get("sort", "latest") or "latest").strip()

    order_by_map = {
        "latest": "id DESC",
        "oldest": "id ASC",
        "title": "title COLLATE NOCASE ASC, id DESC",
    }
    if sort not in order_by_map:
        sort = "latest"
    order_by = order_by_map[sort]

    conn = get_db()

    if q:
        like_q = f"%{q}%"
        total_posts = conn.execute(
            "SELECT COUNT(*) FROM posts WHERE title LIKE ? OR content LIKE ?",
            (like_q, like_q),
        ).fetchone()[0]
    else:
        total_posts = conn.execute("SELECT COUNT(*) FROM posts").fetchone()[0]

    total_pages = max((total_posts + page_size - 1) // page_size, 1)
    if page > total_pages:
        page = total_pages

    offset = (page - 1) * page_size
    if q:
        like_q = f"%{q}%"
        posts = conn.execute(
            f"SELECT * FROM posts WHERE title LIKE ? OR content LIKE ? ORDER BY {order_by} LIMIT ? OFFSET ?",
            (like_q, like_q, page_size, offset),
        ).fetchall()
    else:
        posts = conn.execute(
            f"SELECT * FROM posts ORDER BY {order_by} LIMIT ? OFFSET ?",
            (page_size, offset),
        ).fetchall()

    conn.close()

    return render_template(
        "list.html",
        posts=posts,
        page=page,
        total_pages=total_pages,
        q=q,
        sort=sort,
    )


@app.route("/post/<int:post_id>")
def detail_post(post_id):
    conn = get_db()
    post = conn.execute("SELECT * FROM posts WHERE id = ?", (post_id,)).fetchone()
    conn.close()
    return render_template("detail.html", post=post)


@app.route("/write", methods=["GET", "POST"])
def write_post():
    if request.method == "POST":
        title = request.form["title"]
        content = request.form["content"]
        conn = get_db()
        conn.execute(
            "INSERT INTO posts (title, content) VALUES (?, ?)", (title, content)
        )
        conn.commit()
        conn.close()
        return redirect(url_for("list_posts"))
    return render_template("write.html", post=None)


@app.route("/post/<int:post_id>/edit", methods=["GET", "POST"])
def edit_post(post_id):
    conn = get_db()
    post = conn.execute("SELECT * FROM posts WHERE id = ?", (post_id,)).fetchone()
    if request.method == "POST":
        conn.execute(
            "UPDATE posts SET title=?, content=? WHERE id=?",
            (request.form["title"], request.form["content"], post_id),
        )
        conn.commit()
        conn.close()
        return redirect(url_for("detail_post", post_id=post_id))
    conn.close()
    return render_template("write.html", post=post)


@app.route("/post/<int:post_id>/delete", methods=["POST"])
def delete_post(post_id):
    conn = get_db()
    conn.execute("DELETE FROM posts WHERE id=?", (post_id,))
    conn.commit()
    conn.close()
    return redirect(url_for("list_posts"))


with app.app_context():
    init_db()

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
