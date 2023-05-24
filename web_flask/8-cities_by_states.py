#!/usr/bin/python3
"""
Module contains a script that starts a Flask web application
"""


import models
from flask import Flask
from flask import render_template


app = Flask(__name__)


@app.route('/cities_by_states', strict_slashes=False)
def states_list():
    states = models.storage.all('State').values()
    cities = models.storage.all('City').values()
    return render_template('8-cities_by_states.html', states=states,
                           cities=cities)


@app.teardown_appcontext
def teardown_appcontext(self):
    models.storage.close()


if __name__ == '__main__':
    app.run()
