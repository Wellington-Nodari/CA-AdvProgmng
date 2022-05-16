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
    st = f"SELECT * FROM students WHERE email='{email}' AND password='{pwd}';"
    cur.execute(st)
    e = cur.fetchall()
    nameLogin = e[0][1]
    print(nameLogin)
    try:
        if e[0][2] == email and e[0][3] == pwd:
            session['logged_in'] = True
            g.db.close()
            flash("You were just logged in!")
            return redirect(url_for('test'))
    except:
        error = 'Invalid credentials. Please try again'
        return render_template('/html/index.html', error=error)

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    return redirect(url_for('home'))

def connect_db():
    return sqlite3.connect(app.database)

@app.route('/signup', methods=['POST', 'GET'])
def signup():
    name = str(request.form['username'])
    email = str(request.form['email'])
    pwd = str(request.form['password'])
    pwdc = str(request.form['pwdC'])

    g.db = connect_db()
    cur = g.db.execute("INSERT INTO students (username, email, password) VALUES ('{}','{}','{}');".format(name,email,pwd))
    add = cur.fetchall()
    g.db.commit()
    print(add)
    g.db.close()

    return redirect(url_for('home'))


    # if name in add:
    #     return render_template('/html/index.html', info='User name already in use. Choose another one.')
    # if email in add:
    #     return render_template('/html/index.html', info='Email already in use. Choose another one.')
    # if pwdc != pwd:
    #     return render_template('/html/index.html', info='The passwords must match.')
    #
    # else:
    #     if add[0][2] != pwd:
    #         return render_template('/html/index.html', info='Invalid Password')
    #     else:
    #         return render_template('/html/booking/booking.html', name=name)


if __name__ == '__main__':
    app.run(debug=True)