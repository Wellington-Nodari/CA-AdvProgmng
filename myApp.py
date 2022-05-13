from flask import Flask, request, render_template
from flask_mysqldb import MySQL
from flask_cors import CORS
import json

app = Flask(__name__)
mysql = MySQL(app)
CORS(app)

app.config['MYSQL_USER'] = 'well'
app.config['MYSQL_PASSWORD'] = 'M@nowell0508'
app.config['MYSQL_DB'] = 'login'
app.config['MYSQL_HOST'] = 'localhost' #for now
mysql.init_app(app)

@app.route('/')
def hello():
    cur = mysql.connection.cursor()
    cur.execute('''SELECT * FROM login;''')
    results = cur.fetchall()
    #print(results)
    return results[0]['name'] #render_template("/html/index.html")

# database = {'well@pp.ie': '123', 'tha': 'qwert', 'neusa': 'bere'}
#
#
# @app.route('/form_login', methods=['POST', 'GET'])
# def login():
#     #name1 = request.form['username']
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


if __name__ == '__main__':
    app.run(debug=True)
