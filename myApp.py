from flask import Flask, request, render_template
###from flask_mysqldb import MySQL
from flask_cors import CORS
import mysql.connector
import json

app = Flask(__name__)
###mysql = MySQL(app)
CORS(app)
mysql = mysql.connector.connect(
    host='localhost',
    user='root',
    password='P21m38f77*',
    port='3306',
    database='mycadbs'
)
mycursor = mysql.cursor()
mycursor.execute('SELECT * FROM login;')
users = mycursor.fetchall()

####
# app.config['MYSQL_USER'] = 'root'
# app.config['MYSQL_PASSWORD'] = 'P21m38f77*'
# app.config['MYSQL_DB'] = 'mycadbs'
# app.config['MYSQL_HOST'] = 'localhost' #for now
# mysql.init_app(app)
####

@app.route('/')
def hello():
    return print(users) #results[0]['name'] #render_template("/html/index.html")

# database = {'well@pp.ie': '123', 'tha': 'qwert', 'neusa': 'bere'}


# @app.route('/form_login', methods=['POST', 'GET'])
# def login():
#     #username = request.form['username']
#     email = request.form['email']
#     pwd = request.form['password']
#
#     if email is not None:
#         if email not in database:
#             return render_template('/html/index.html', info='Invalid Email')
#
#         else:
#             if database[email] != pwd:
#                 return render_template('/html/index.html', info='Invalid Password')
#             else:
#                 return render_template('/html/booking/booking.html', name=email) #request.form['username'])
#     else:
#         return render_template('/html/index.html', info='')
#
# @app.route('/form_signup', methods=['POST', 'GET'])
# def signup():
#     name1 = request.form['username']
#     email = request.form['email']
#     pwd = request.form['password']
#     cpwd = request.form['password']
#
#     if name1 in database:
#         return render_template('/html/index.html', info='User name already in use. Choose another one.')
#     if email in database:
#         return render_template('/html/index.html', info='Email already in use. Choose another one.')
#     if pwd != cpwd:
#         return render_template('/html/index.html', info='The passwords must match.')
#
#     else:
#         if database[email] != pwd:
#             return render_template('/html/index.html', info='Invalid Password')
#         else:
#             return render_template('/html/booking/booking.html', name=name1)
#

if __name__ == '__main__':
    app.run(debug=True)
