import sqlite3

# Connect database (creates new DB)
conn = sqlite3.connect("database.db")
cursor = conn.cursor()

print("\n===== DATABASE CONNECTED =====")

# Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS Students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    age INTEGER,
    course TEXT
)
""")

# ---------------- CREATE ----------------
cursor.execute("""
INSERT INTO Students (name, age, course)
VALUES ('Ajeefa', 22, 'AIML')
""")
conn.commit()
print("\nRecord Inserted Successfully!")

# ---------------- READ ----------------
print("\n===== STUDENT RECORDS =====")
cursor.execute("SELECT * FROM Students")
for row in cursor.fetchall():
    print(row)

# ---------------- UPDATE ----------------
cursor.execute("""
UPDATE Students
SET age = 23
WHERE name='Ajeefa'
""")
conn.commit()
print("\nRecord Updated Successfully!")

cursor.execute("SELECT * FROM Students WHERE name='Ajeefa'")
print("Updated Record:", cursor.fetchall())

# ---------------- DELETE ----------------
cursor.execute("""
DELETE FROM Students
WHERE name='Ajeefa'
""")
conn.commit()
print("\nRecord Deleted Successfully!")

# ---------------- FINAL DATA ----------------
print("\n===== FINAL TABLE =====")
cursor.execute("SELECT * FROM Students")
print(cursor.fetchall())

conn.close()