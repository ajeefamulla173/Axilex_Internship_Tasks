from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

# ---------------- LOGIN PAGE ----------------
@app.route("/", methods=["GET", "POST"])
def login():

    error = ""

    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        conn = sqlite3.connect("database.db")
        cursor = conn.cursor()

        cursor.execute(
            "SELECT * FROM Users WHERE username=? AND password=?",
            (username, password)
        )

        user = cursor.fetchone()
        conn.close()

        if user:
            return redirect(f"/dashboard/{username}")
        else:
            error = "Invalid Username or Password"

    return render_template("login.html", error=error)


# ---------------- DASHBOARD ----------------
@app.route("/dashboard/<user>")
def dashboard(user):
    return render_template("dashboard.html", user=user)


if __name__ == "__main__":
    app.run(debug=True)