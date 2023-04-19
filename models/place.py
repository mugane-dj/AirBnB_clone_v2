#!/usr/bin/python3
""" Place Module for HBNB project """
import models
from models.base_model import BaseModel
from models.base_model import Base
from os import getenv
from sqlalchemy import Column, Integer, String, ForeignKey, Float
from sqlalchemy.orm import relationship


class Place(BaseModel):
    """ A place to stay """
    __tablename__ = 'places'
    city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, default=0, nullable=False)
    number_bathrooms = Column(Integer, default=0, nullable=False)
    max_guest = Column(Integer, default=0, nullable=False)
    price_by_night = Column(Integer, default=0, nullable=False)
    latitude = Column(Float, default=0, nullable=True)
    longitude = Column(Float, default=0, nullable=True)
    amenity_ids = []
    reviews = relationship("Review", backref="place", cascade="delete")

    if getenv('HBNB_TYPE_STORAGE') != 'db':
        @property
        def reviews(self):
            """Returns a list if Review Instances matching place_id"""
            reviews = []
            for reviews in list(models.storage.all(Review).values()):
                if review.place_id == self.id:
                    reviews.append(review)
            return reviews
