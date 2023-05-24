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
    states = list(models.storage.all('State').values())
    cities = list(models.storage.all('City').values())
    sorted_states = sorted(states, key=lambda state: state.name)
    sorted_cities = sorted(cities, key=lambda city: city.name)
    return render_template('8-cities_by_states.html', states=sorted_states,
                           cities=sorted_cities)


@app.teardown_appcontext
def teardown_appcontext(self):
    models.storage.close()


if __name__ == '__main__':
    app.run()
