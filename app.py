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
    conn = get_db()
    posts = conn.execute("SELECT * FROM posts ORDER BY id DESC").fetchall()
    conn.close()
    return render_template("list.html", posts=posts)


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


if __name__ == "__main__":
    init_db()
    app.run(debug=True)
