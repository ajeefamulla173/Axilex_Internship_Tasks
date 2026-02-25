import sqlite3

# Connect to database (creates file if not exists)
conn = sqlite3.connect("database.db")
cursor = conn.cursor()

# Create Users table
cursor.execute("""
CREATE TABLE IF NOT EXISTS Users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    email TEXT NOT NULL,
    password TEXT NOT NULL
)
""")

# Create Students table
cursor.execute("""
CREATE TABLE IF NOT EXISTS Students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER,
    course TEXT
)
""")

# Create Tasks table
cursor.execute("""
CREATE TABLE IF NOT EXISTS Tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    task_name TEXT NOT NULL,
    status TEXT,
    due_date TEXT
)
""")

# Clear old data (so it doesn't duplicate every run)
cursor.execute("DELETE FROM Users")
cursor.execute("DELETE FROM Students")
cursor.execute("DELETE FROM Tasks")

# Insert sample data
cursor.execute("INSERT INTO Users (username, email, password) VALUES ('azifa', 'azifa@gmail.com', '1234')")
cursor.execute("INSERT INTO Students (name, age, course) VALUES ('Ajeefa Mulla', 21, 'AI & ML')")
cursor.execute("INSERT INTO Tasks (task_name, status, due_date) VALUES ('Complete Database Task', 'Pending', '2026-02-28')")

conn.commit()

# ===============================
# Structured Output Section
# ===============================

print("\n========== USERS TABLE ==========")
cursor.execute("SELECT * FROM Users")
users = cursor.fetchall()
for user in users:
    print(f"ID: {user[0]}")
    print(f"Username: {user[1]}")
    print(f"Email: {user[2]}")
    print(f"Password: {user[3]}")
    print("---------------------------------")

print("\n========== STUDENTS TABLE ==========")
cursor.execute("SELECT * FROM Students")
students = cursor.fetchall()
for student in students:
    print(f"ID: {student[0]}")
    print(f"Name: {student[1]}")
    print(f"Age: {student[2]}")
    print(f"Course: {student[3]}")
    print("---------------------------------")

print("\n========== TASKS TABLE ==========")
cursor.execute("SELECT * FROM Tasks")
tasks = cursor.fetchall()
for task in tasks:
    print(f"ID: {task[0]}")
    print(f"Task Name: {task[1]}")
    print(f"Status: {task[2]}")
    print(f"Due Date: {task[3]}")
    print("---------------------------------")

conn.close()