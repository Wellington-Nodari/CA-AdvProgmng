from flask import Flask, request, render_template

app = Flask(__name__)

mysql = {'well@pp.ie': '123', 'tha': 'qwert', 'neusa': 'bere'}

@app.route('/')
def hello():
    return render_template("/html/index.html")


@app.route('/form_login', methods=['POST', 'GET'])
def login():
    email = request.form['email']
    pwd = request.form['pwd']


    if email is not None:
        if email not in mysql:
            return render_template('/html/index.html', info='Invalid Email')

        else:
            if [email] != pwd:
                return render_template('/html/index.html', info='Invalid Password')
            else:
                return render_template('/html/booking/booking.html', name=email)
    else:
        return render_template('/html/index.html', info='')

@app.route('/form_signup', methods=['POST', 'GET'])
def signup():
    name = request.form['username']
    email = request.form['email']
    pwd = request.form['pwd']
    pwdC = request.form['pwd']

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
            return render_template('/html/booking/booking.html', name=name)


if __name__ == '__main__':
    app.run(debug=True)
