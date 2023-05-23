#!/usr/bin/python3
"""
Module contains a script that starts a Flask web application
"""


import models
from flask import Flask
from flask import render_template


app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states_list():
    states = list(models.storage.all('State').values())
    sorted_states = sorted(states, key=lambda state: state.name)
    return render_template('7-states_list.html', states=sorted_states)


@app.teardown_appcontext
def teardown_appcontext(self):
    models.storage.close()


if __name__ == '__main__':
    app.run()
