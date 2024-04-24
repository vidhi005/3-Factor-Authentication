import csv
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Load existing users from CSV file
users = {}

def load_users():
    with open('users.csv', mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            username, password = row
            users[username] = password

load_users()

def save_user_to_csv(username, password):
    with open('users.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([username, password])

@app.route('/')
def login_page():
    return render_template('login.html')

@app.route('/hello')
def login2_page():
    return render_template('signup.html')

@app.route('/form/login', methods=['POST'])
def process_login():
    username = request.form.get('username')
    password = request.form.get('password')

    if username in users and users[username] == password:
        return "Authentication Successful. Access granted!"
    else:
        return "Authentication Failed. Access denied."

@app.route('/form/signup', methods=['POST'])
def process_signup():
    username = request.form.get('username')
    password = request.form.get('password')

    if username in users:
        return "Username already exists. Try a different one."

    save_user_to_csv(username, password)
    return "User account created successfully."

if __name__ == "__main__":
    app.run(debug=True)
