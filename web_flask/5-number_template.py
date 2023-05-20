#!/usr/bin/python3
"""Module contains a script that starts a Flask web application"""


from flask import Flask
from flask import render_template


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def display(text):
    safe_text = text.replace('_', ' ')
    return "C " + safe_text


@app.route('/python', strict_slashes=False)
@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def display_python(text="is cool"):
    safe_text = text.replace('_', ' ')
    return "Python " + safe_text


@app.route('/number/<int:n>', strict_slashes=False)
def display_number(n):
    return "{} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def display_number_template(n):
    return render_template('5-number.html', n=n)


if __name__ == '__main__':
    app.run()
