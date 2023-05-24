#!/usr/bin/python3
"""
Module contains a script that starts a Flask web application
"""


import models
from flask import Flask
from flask import render_template
from os import getenv

app = Flask(__name__)


@app.route('/hbnb_filters', strict_slashes=False)
def all_data():
    states = models.storage.all('State').values()
    cities = models.storage.all('City').values()
    amenities = models.storage.all('Amenity').values()
    return render_template('10-hbnb_filters.html', states=states, cities=cities,
                           amenities=amenities)


@app.teardown_appcontext
def teardown_appcontext(self):
    models.storage.close()


if __name__ == '__main__':
    app.run()
