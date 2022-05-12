from flask import Flask, request, render_template
#from flask.ext.mysql import MySQL

#mysql = MySQL()

app = Flask(__name__)


@app.route('/')
def hello():
    return render_template("/html/index.html")

database = {'well': '123', 'tha': 'qwert', 'neusa': 'bere'}


@app.route('/form_login', methods=['POST', 'GET'])
def login():
    name1 = request.form['username']
    pwd = request.form['password']

    if name1 not in database:
        return render_template('/html/index.html', info='Invalid User')

    else:
        if database[name1] != pwd:
            return render_template('/html/index.html', info='Invalid Password')
        else:
            return render_template('/html/booking/booking.html', name=name1)

@app.route('/form_signup', methods=['POST', 'GET'])
def signup():
    name1 = request.form['username']
    email = request.form['email']
    pwd = request.form['password']
    cpwd = request.form['password']

    if name1 in database:
        return render_template('/html/index.html', info='User name already in use. Choose another one.')
    if email in database:
        return render_template('/html/index.html', info='Email already in use. Choose another one.')
    if pwd != cpwd:
        return render_template('/html/index.html', info='The passwords must match.')

    else:
        if database[email] != pwd:
            return render_template('/html/index.html', info='Invalid Password')
        else:
            return render_template('/html/booking/booking.html', name=name1)


if __name__ == '__main__':
    app.run(debug=True)
