from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template("main.html")


@app.route('/a')
def apage():  # put application's code here
    return render_template("a.html")


@app.route('/b')
def bpage():  # put application's code here
    return render_template("b.html")


@app.route('/c')
def cpage():  # put application's code here
    return render_template("c.html")


@app.route('/d')
def dpage():  # put application's code here
    return render_template("d.html")

@app.route('/e')
def epage():  # put application's code here
    return render_template("e.html")


if __name__ == '__main__':
    app.run()
