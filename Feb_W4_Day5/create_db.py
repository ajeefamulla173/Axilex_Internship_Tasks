import sqlite3

conn = sqlite3.connect("database.db")
cursor = conn.cursor()

# Create Users table
cursor.execute("""
CREATE TABLE IF NOT EXISTS Users(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT,
    password TEXT
)
""")

# Insert sample user
cursor.execute("""
INSERT INTO Users (username, password)
VALUES ('azifa', '1234')
""")

conn.commit()
conn.close()

print("Database and User Created Successfully!")