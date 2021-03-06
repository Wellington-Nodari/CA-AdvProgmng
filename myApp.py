from flask import Flask, request, render_template, redirect, url_for, session, flash, g
from functools import wraps
import sqlite3
import datetime

app = Flask(__name__)
app.secret_key = "diamond"
app.database = "myschool.db"
now = datetime.datetime.now()

def connect_db():
    return sqlite3.connect(app.database)

@app.route('/')
def home():
    return render_template("/html/index.html")

def login_required(f): #taken from https://www.youtube.com/watch?v=_pzMDIi5BuI
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash('Please login first.')
            return redirect(url_for('/'))
    return wrap

@app.route('/main', methods=['GET','POST'])
@login_required
def main():
    user_email = session['email']
    if session is None:
        error = 'Access denied. Login required!'
        return render_template("/html/index.html", error=error)
    else:
        g.db = connect_db()
        cur = g.db.execute("SELECT * FROM std_enroll")
        fetchCN = f"SELECT courseName FROM std_enroll WHERE email='{user_email}'"
        cur.execute(fetchCN)
        x = cur.fetchall()
        subjName = x[0][0]

        g.db = connect_db()
        cur = g.db.execute("SELECT * FROM students")
        fetchFN = f"SELECT fname FROM students WHERE email='{user_email}'"
        cur.execute(fetchFN)
        y = cur.fetchall()
        studentName = y[0][0]

        g.db = connect_db()
        cur = g.db.execute("SELECT * FROM courses")
        fetchID = f"SELECT courseId FROM courses C INNER JOIN std_enroll SE ON C.courseName = SE.courseName WHERE email='{user_email}'"
        cur.execute(fetchID)
        z = cur.fetchall()
        courseId = z[0][0]
        print(courseId)

        g.db.close()
        return render_template('/html/main.html', subjName=subjName, studentName=studentName, courseId=courseId)

@app.route('/datascience')
def dataSc():
    return render_template("/html/dataSc.html")

@app.route('/1')
@login_required
def dataScience():

    user_email = session['email']
    if session is None:
        print('session is none')
    else:
        g.db = connect_db()
        cur = g.db.execute("SELECT * FROM std_enroll")
        fetchCN = f"SELECT courseName FROM std_enroll WHERE email='{user_email}'"
        cur.execute(fetchCN)
        x = cur.fetchall()
        subjName = x[0][0]

        if subjName == 'Data Science':
            return render_template("/html/dataScience_content.html")
        else:
            error = 'You are not enrolled to this course! Access denied.'
            return render_template("/html/index.html", error=error)

@app.route('/softdev')
def softdev():
    return render_template("/html/softDev.html")

@app.route('/2')
@login_required
def softwareDevelopment():
    user_email = session['email']
    if session is None:
        print('session is none')
    else:
        g.db = connect_db()
        cur = g.db.execute("SELECT * FROM std_enroll")
        fetchCN = f"SELECT courseName FROM std_enroll WHERE email='{user_email}'"
        cur.execute(fetchCN)
        x = cur.fetchall()
        subjName = x[0][0]
        print(subjName)

        if subjName == 'Software Development':
            return render_template("/html/softwareDev_content.html")
        else:
            error = 'You are not enrolled to this course! Access denied.'
            return render_template("/html/index.html", error=error)

@app.route('/devops')
def devops():
    return render_template("/html/devops.html")

@app.route('/3')
@login_required
def devOps():
    user_email = session['email']
    if session is None:
        print('session is none')
    else:
        g.db = connect_db()
        cur = g.db.execute("SELECT * FROM std_enroll")
        fetchCN = f"SELECT courseName FROM std_enroll WHERE email='{user_email}'"
        cur.execute(fetchCN)
        x = cur.fetchall()
        subjName = x[0][0]

        if subjName == 'DevOps':
            return render_template("/html/devOps_content.html")
        else:
            error = 'You are not enrolled to this course! Access denied.'
            return render_template("/html/index.html", error=error)

@app.route('/ixdesign')
def ixdesign():
    return render_template("/html/ixdesign.html")

@app.route('/4')
@login_required
def uiUxDesign():
    user_email = session['email']
    if session is None:
        print('session is none')
    else:
        g.db = connect_db()
        cur = g.db.execute("SELECT * FROM std_enroll")
        fetchCN = f"SELECT courseName FROM std_enroll WHERE email='{user_email}'"
        cur.execute(fetchCN)
        x = cur.fetchall()
        subjName = x[0][0]

        if subjName == 'UI/UX Design':
            return render_template("/html/uiUxDesign_content.html")
        else:
            error = 'You are not enrolled to this course! Access denied.'
            return render_template("/html/index.html", error=error)

@app.route('/bchain')
def bchain():
    return render_template("/html/blockchain.html")

@app.route('/5')
@login_required
def blockChain():
    user_email = session['email']
    if session is None:
        print('session is none')
    else:
        g.db = connect_db()
        cur = g.db.execute("SELECT * FROM std_enroll")
        fetchCN = f"SELECT courseName FROM std_enroll WHERE email='{user_email}'"
        cur.execute(fetchCN)
        x = cur.fetchall()
        subjName = x[0][0]

        if subjName == 'Blockchain':
            return render_template("/html/blockChain_content.html")
        else:
            error = 'You are not enrolled to this course! Access denied.'
            return render_template("/html/index.html", error=error)

@app.route('/cybersec')
def cybersec():
    return render_template("/html/cybersec.html")

@app.route('/6')
@login_required
def cyberSecurity():
    user_email = session['email']
    if session is None:
        print('session is none')
    else:
        g.db = connect_db()
        cur = g.db.execute("SELECT * FROM std_enroll")
        fetchCN = f"SELECT courseName FROM std_enroll WHERE email='{user_email}'"
        cur.execute(fetchCN)
        x = cur.fetchall()
        subjName = x[0][0]

        if subjName == 'Cybersecurity':
            return render_template("/html/cyberSec_content.html")
        else:
            error = 'You are not enrolled to this course! Access denied.'
            return render_template("/html/index.html", error=error)

@app.route("/login", methods=['POST', 'GET'])
def login():
    email = str(request.form["email"])
    pwd = str(request.form["password"])
    g.db = connect_db()
    cur = g.db.execute('select * from loginCred')
    st = f"SELECT * FROM loginCred WHERE email='{email}' AND password='{pwd}';"
    cur.execute(st)
    e = cur.fetchall()

    try:
        if e[0][1] == email and e[0][2] == pwd:
            session['logged_in'] = True
            g.db.close()
            session['email'] = email
            return redirect(url_for('main'))

    except:
        error = 'Invalid credentials. Please try again'
        return render_template('/html/index.html', error=error)

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    return redirect(url_for('home'))


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

# @app.errorhandler(404)
# def not_found(e):
#     return render_template("404.html")

if __name__ == '__main__':
    app.run(debug=True)