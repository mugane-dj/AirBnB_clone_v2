#!/usr/bin/python3
""" State Module for HBNB project """
from os import getenv
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey
from models import storage


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    if getenv("HBNB_TYPE_STORAGE") == "db":
        name = Column(String(128), nullable=False)
    else:
        name = ""

        @property
        def cities(self):
            """Return the list of City objects from storage linked to the
            current State"""
            city_objs = storage.all(City).values()
            return [city_obj for city_obj in city_objs
                    if city_obj.state_id == self.id]
