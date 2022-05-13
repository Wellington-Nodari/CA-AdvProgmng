from flask import Flask, request, render_template
from flask_mysqldb import MySQL
from flask_cors import CORS
import mysql.connector
import json

app = Flask(__name__)
mysql = MySQL()
CORS(app)


app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'P21m38f77*'
app.config['MYSQL_DB'] = 'mycadbs'
app.config['MYSQL_HOST'] = 'localhost'
mysql.init_app(app)


@app.route('/')
def hello():
    return render_template("/html/index.html")

# database = {'well@pp.ie': '123', 'tha': 'qwert', 'neusa': 'bere'}


@app.route('/form_login', methods=['POST', 'GET'])
def login():
    email = request.args.get('email')
    pwd = request.args.get('pwd')

    cur = mysql.connection.cursor()  # create a connection to the SQL instance
    cur.execute('''SELECT * FROM students''')  # execute an SQL statment
    rv = cur.fetchall()
    results = []

    for row in rv:
        if email is not None:
            if email not in row:
                return render_template('/html/index.html', info='Invalid Email')

            else:
                if results[email] != pwd:
                    return render_template('/html/index.html', info='Invalid Password')
                else:
                    return render_template('/html/booking/booking.html', name=email) #request.form['username'])
        else:
            return render_template('/html/index.html', info='')

@app.route('/form_signup', methods=['POST', 'GET'])
def signup():
    name = request.args.get('username')
    email = request.args.get('email')
    pwd = request.args.get('pwd')
    pwdC = request.args.get['pwd']

    cur = mysql.connection.cursor()
    s = '''INSERT INTO login(username, email, pwd) VALUES('{}','{}','{}');'''.format(name, email, pwd)
    cur.execute(s)

    if name in mysql:
        return render_template('/html/index.html', info='User name already in use. Choose another one.')
    if email in mysql:
        return render_template('/html/index.html', info='Email already in use. Choose another one.')
    if pwdC != pwd:
        return render_template('/html/index.html', info='The passwords must match.')

    else:
        if mysql[email] != pwd:
            return render_template('/html/index.html', info='Invalid Password')
        else:
            mysql.connection.commit()
            return render_template('/html/booking/booking.html', name=name)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
