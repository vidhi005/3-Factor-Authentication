from flask import Flask, render_template, request, redirect, url_for
import csv

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('colorForm.html')

@app.route('/form/process', methods=['POST'])
def process_form():
    name = request.form.get('name')
    selected_colors = request.form.get('sequence').split(',')

    with open('colors.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([name] + selected_colors)

    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
