from flask import Flask, request, render_template, redirect, url_for, session, flash, g
from functools import wraps
import sqlite3
import datetime
import json

app = Flask(__name__)
app.secret_key = "diamond" #check this!!!
app.database = "myschool.db"
now = datetime.datetime.now()

@app.route('/')
def home():
    return render_template("/html/index.html")

def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash('Please login first.')
            return redirect(url_for('/'))
    return wrap

@app.route('/main')
@login_required
def main():

    g.db = connect_db()
    cur = g.db.execute('select * from students')
    students = [dict(studentId=row[0], fname=row[1], lname=row[2], email=row[3]) for row in cur.fetchall()]
    g.db.close()
    return render_template('/html/booking/booking.html', students=students)

@app.route('/datascience')
def dataSc():
    return render_template("/dataSc.html")

@app.route("/login", methods=['POST', 'GET'])
def login():
    error = None
    email = str(request.form["email"])
    pwd = str(request.form["password"])
    g.db = connect_db()
    cur = g.db.execute('select * from loginCred')
    st = f"SELECT * FROM loginCred WHERE email='{email}' AND password='{pwd}';"
    cur.execute(st)
    e = cur.fetchall()
    # nameLogin = e[0][1]
    print(e)
    try:
        if e[0][1] == email and e[0][2] == pwd:
            session['logged_in'] = True
            g.db.close()
            flash("You were just logged in!")
            return redirect(url_for('main'))
    except:
        error = 'Invalid credentials. Please try again'
        return render_template('/html/index.html', error=error)

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    return redirect(url_for('home'))

def connect_db():
    return sqlite3.connect(app.database)

@app.route('/enroll', methods=['POST', 'GET'])
def enroll():
    fname = str(request.form['fname'])
    lname = str(request.form['lname'])
    email = str(request.form['email'])
    course = str(request.form['course'])
    pwd = str(request.form['password'])
    pwdc = str(request.form['pwdC'])

    g.db = connect_db()
    cur = g.db.execute("INSERT INTO students (fname, lname, email) VALUES ('{}','{}','{}');".format(fname, lname, email))
    cur1 = g.db.execute("INSERT INTO loginCred (email, password) VALUES ('{}','{}');".format(email, pwd))
    cur2 = g.db.execute("INSERT INTO std_enroll (email, courseName, enrlDate) VALUES ('{}','{}','{}');".format(email, course, now))
    add = cur.fetchall(), cur1.fetchall(), cur2.fetchall()

    if pwd != pwdc:
        return render_template('/html/index.html', error='The passwords much match.')

    g.db.commit()
    print(add)
    g.db.close()

    return redirect(url_for('home'))


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