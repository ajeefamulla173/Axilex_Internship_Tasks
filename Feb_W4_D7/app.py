from flask import Flask, render_template, request, redirect, session
import sqlite3

app = Flask(__name__)
app.secret_key = "secret_key_for_sessions"

# Database connection
def get_db():
    conn = sqlite3.connect("database.db")
    conn.row_factory = sqlite3.Row
    return conn

# Create tables
def create_tables():
    conn = get_db()
    conn.execute("""CREATE TABLE IF NOT EXISTS users (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        username TEXT UNIQUE,
                        password TEXT
                    )""")
    conn.execute("""CREATE TABLE IF NOT EXISTS students (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT,
                        email TEXT
                    )""")
    conn.commit()
    conn.close()

# Home route
@app.route("/")
def index():
    return render_template("index.html")

# Registration
@app.route("/register", methods=["GET","POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        conn = get_db()
        try:
            conn.execute("INSERT INTO users (username,password) VALUES (?,?)", (username,password))
            conn.commit()
        except sqlite3.IntegrityError:
            return "Username already exists!"
        finally:
            conn.close()
        return redirect("/login")
    return render_template("register.html")

# Login
@app.route("/login", methods=["GET","POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        conn = get_db()
        user = conn.execute("SELECT * FROM users WHERE username=? AND password=?", (username,password)).fetchone()
        conn.close()
        if user:
            session["user"] = username
            return redirect("/dashboard")
        else:
            return "Invalid credentials!"
    return render_template("login.html")

# Dashboard (CRUD)
@app.route("/dashboard")
def dashboard():
    if "user" not in session:
        return redirect("/login")
    conn = get_db()
    students = conn.execute("SELECT * FROM students").fetchall()
    conn.close()
    return render_template("dashboard.html", students=students)

# Add student
@app.route("/add", methods=["POST"])
def add():
    if "user" not in session:
        return redirect("/login")
    name = request.form["name"]
    email = request.form["email"]
    conn = get_db()
    conn.execute("INSERT INTO students (name,email) VALUES (?,?)", (name,email))
    conn.commit()
    conn.close()
    return redirect("/dashboard")

# Edit student
@app.route("/edit/<int:id>")
def edit(id):
    if "user" not in session:
        return redirect("/login")
    conn = get_db()
    student = conn.execute("SELECT * FROM students WHERE id=?", (id,)).fetchone()
    conn.close()
    return render_template("edit.html", student=student)

# Update student
@app.route("/update/<int:id>", methods=["POST"])
def update(id):
    if "user" not in session:
        return redirect("/login")
    name = request.form["name"]
    email = request.form["email"]
    conn = get_db()
    conn.execute("UPDATE students SET name=?,email=? WHERE id=?", (name,email,id))
    conn.commit()
    conn.close()
    return redirect("/dashboard")

# Delete student
@app.route("/delete/<int:id>")
def delete(id):
    if "user" not in session:
        return redirect("/login")
    conn = get_db()
    conn.execute("DELETE FROM students WHERE id=?", (id,))
    conn.commit()
    conn.close()
    return redirect("/dashboard")

# Logout
@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect("/login")

if __name__ == "__main__":
    create_tables()
    app.run(debug=True)