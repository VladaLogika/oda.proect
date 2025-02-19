from flask import Flask, redirect, url_for, session, request, render_template
import sqlite3
app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
   return render_template("index.html")

@app.route('/firstpage')
def first():
    return render_template('firstpage.html')

@app.route('/gallery')
def gallery():
    return render_template('gallery.html')

@app.route('/about')
def about():
    return render_template('about.html')



@app.route('/login', methods=['POST'])
def login():
    if request.method == 'POST':
        login = request.form['username']
        password = request.form['password']

        with sqlite3.connect('blog.db') as conn:
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()
            user = cursor.execute('SELECT * FROM user WHERE login = ? AND password = ?', (login, password)).fetchone()

        if user is not None:
            return first()
        else:
            return 'Неправильний логін або пароль'+index()













if __name__ == '__main__':
   app.run(debug=True)