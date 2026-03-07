from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

def get_db():
    conn = sqlite3.connect("database.db")
    conn.row_factory = sqlite3.Row
    return conn


# Create table if not exists
def create_table():
    conn = get_db()
    conn.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            email TEXT
        )
    """)
    conn.commit()
    conn.close()


# View records
@app.route("/")
def index():
    conn = get_db()
    students = conn.execute("SELECT * FROM students").fetchall()
    conn.close()
    return render_template("index.html", students=students)


# Add record
@app.route("/add", methods=["POST"])
def add():
    name = request.form["name"]
    email = request.form["email"]

    conn = get_db()
    conn.execute(
        "INSERT INTO students (name,email) VALUES (?,?)",
        (name, email)
    )
    conn.commit()
    conn.close()

    return redirect("/")


# Delete record
@app.route("/delete/<int:id>")
def delete(id):
    conn = get_db()
    conn.execute("DELETE FROM students WHERE id=?", (id,))
    conn.commit()
    conn.close()

    return redirect("/")


# Edit page
@app.route("/edit/<int:id>")
def edit(id):
    conn = get_db()
    student = conn.execute(
        "SELECT * FROM students WHERE id=?", (id,)
    ).fetchone()
    conn.close()

    return render_template("edit.html", student=student)


# Update record
@app.route("/update/<int:id>", methods=["POST"])
def update(id):
    name = request.form["name"]
    email = request.form["email"]

    conn = get_db()
    conn.execute(
        "UPDATE students SET name=?, email=? WHERE id=?",
        (name, email, id)
    )
    conn.commit()
    conn.close()

    return redirect("/")


if __name__ == "__main__":
    create_table()
    app.run(debug=True)