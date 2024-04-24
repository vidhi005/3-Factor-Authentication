from flask import Flask, request, render_template, redirect, url_for
import sqlite3

app = Flask(__name__)

# Define a function to create a database connection
def get_db_connection():
    conn = sqlite3.connect('user_data.db')
    conn.row_factory = sqlite3.Row
    return conn

# Initialize the database if it doesn't exist
def init_db():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS signup (
            username TEXT NOT NULL,
            password TEXT NOT NULL
        );
    ''')
    conn.commit()
    conn.close()

init_db()  # Initialize the database

@app.route('/')
def home():
    return 'Welcome to the User Registration System <a href="/signup">Sign Up</a>'

@app.route('/signup', methods=['GET', 'POST'])
def register():
    message = ""
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO signup (username,password) VALUES (?,?)",
                       (username, password))
        conn.commit()
        conn.close()

        message = "Data inserted successfully!"

    return render_template('p2.py', message=message)

if __name__ == '__main__':
    app.run(debug=True)
