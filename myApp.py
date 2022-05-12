from flask import Flask, request, render_template

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
            return render_template('/booking/booking.html', name=name1)


if __name__ == '__main__':
    app.run(debug=True)
