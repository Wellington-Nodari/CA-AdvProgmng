from flask import Flask, request, render_template, redirect, url_for, session, flash, g
from functools import wraps
import sqlite3
import json

app = Flask(__name__)

app.secret_key = "diamond" #check this!!!
app.database = "myschool.db"

def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash('Please login first.')
            return redirect(url_for('login'))
    return wrap

@app.route('/test')
@login_required
def test():
    g.db = connect_db()
    cur = g.db.execute('select * from students')
    students = [dict(studentId=row[0], username=row[1], email=row[2]) for row in cur.fetchall()]
    g.db.close()
    return render_template('/html/booking/booking.html', students=students)

@app.route('/')
def home():
    return render_template("/html/index.html")

@app.route("/login", methods=['POST', 'GET'])
def login():
    error = None
    email = str(request.form["email"])
    pwd = str(request.form["password"])
    g.db = connect_db()
    cur = g.db.execute('select * from students')
    st = f"SELECT email, password FROM students WHERE email='{email}' AND password='{pwd}';"
    cur.execute(st)
    e = cur.fetchall()

    if e[0][0] == email and e[0][1] == pwd:
        session['logged_in'] = True
        g.db.close()
        flash("You were just logged in!")
        return redirect(url_for('test'))
    else:
        error = 'Invalid credentials. Please try again'
        return render_template('/html/index.html', error=error)

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    return redirect(url_for('home'))

def connect_db():
    return sqlite3.connect(app.database)

# @app.route('/signup', methods=['POST', 'GET'])
# def signup():
#     name = request.form['username']
#     email = request.form['email']
#     pwd = request.form['pwd']
#     pwdc = request.form['pwd']
#
#     if name in mysql:
#         return render_template('/html/index.html', info='User name already in use. Choose another one.')
#     if email in mysql:
#         return render_template('/html/index.html', info='Email already in use. Choose another one.')
#     if pwdc != pwd:
#         return render_template('/html/index.html', info='The passwords must match.')
#
#     else:
#         if mysql[email] != pwd:
#             return render_template('/html/index.html', info='Invalid Password')
#         else:
#             return render_template('/html/booking/booking.html', name=name)


if __name__ == '__main__':
    app.run(debug=True)