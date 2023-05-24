#!/usr/bin/python3
""" State Module for HBNB project """


import models
from os import getenv
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    if getenv("HBNB_TYPE_STORAGE") == "db":
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="state",
                              cascade="delete")
    else:
        name = ""

        @property
        def cities(self):
            """Return the list of City objects from storage linked to the
            current State"""
            cities_list = []
            for city in models.storage.all('City').values():
                if city.state_id == self.id:
                    print("{}: {}", self.id, city.stated_id)
                    cities_list.append(city)
            return cities_list
