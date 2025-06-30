from flask import Flask, request, render_template
import mysql.connector
import os

app = Flask(__name__)

db = mysql.connector.connect(
    host=os.environ['DB_HOST'],
    user=os.environ['DB_USER'],
    password=os.environ['DB_PASS'],
    database='competition'
)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['POST'])
def register():
    name = request.form['name']
    email = request.form['email']
    cursor = db.cursor()
    cursor.execute("INSERT INTO registrations (name, email) VALUES (%s, %s)", (name, email))
    db.commit()
    return "<h2>Registration successful</h2>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
