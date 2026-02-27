from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

# Initialize database and table
conn = sqlite3.connect("database.db")
cursor = conn.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS Students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    age INTEGER,
    course TEXT
)
""")
conn.commit()
conn.close()

@app.route('/')
def index():
    return render_template('form.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    age = request.form['age']
    course = request.form['course']
    
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Students (name, age, course) VALUES (?, ?, ?)", (name, age, course))
    conn.commit()
    conn.close()
    
    return redirect('/students')

@app.route('/students')
def students():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Students")
    students = cursor.fetchall()
    conn.close()
    return render_template('display.html', students=students)

if __name__ == '__main__':
    app.run(debug=True)