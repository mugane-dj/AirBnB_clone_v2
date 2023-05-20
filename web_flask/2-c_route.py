#!/usr/bin/python3
"""Module contains a script that starts a Flask web application"""


from flask import Flask


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def index():
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def display(text):
    text = text.replace('_', ' ')
    return f"C {text}"


if __name__ == '__main__':
    app.run()
