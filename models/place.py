#!/usr/bin/python3
""" Place Module for HBNB project """
import models
from models.base_model import BaseModel, Base
from os import getenv
from sqlalchemy import (
    Column,
    Integer,
    String,
    ForeignKey,
    Float,
    Table,
)
from sqlalchemy.orm import relationship

place_amenity = Table(
    "place_amenity", Base.metadata,
    Column("place_id", String(60),
           ForeignKey("places.id"),
           primary_key=True, nullable=False),
    Column("amenity_id", String(60),
           ForeignKey("amenities.id"),
           primary_key=True, nullable=False),
)


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = "places"
    if getenv("HBNB_TYPE_STORAGE") == "db":
        city_id = Column(String(60), ForeignKey("cities.id"), nullable=False,
                         unique=True)
        user_id = Column(String(60), ForeignKey("users.id"), nullable=False,
                         unique=True)
        name = Column(String(128), nullable=False)
        description = Column(String(1024), nullable=True)
        number_rooms = Column(Integer, default=0, nullable=False)
        number_bathrooms = Column(Integer, default=0, nullable=False)
        max_guest = Column(Integer, default=0, nullable=False)
        price_by_night = Column(Integer, default=0, nullable=False)
        latitude = Column(Float, default=0, nullable=True)
        longitude = Column(Float, default=0, nullable=True)
        amenity_ids = []
        reviews = relationship("Review", backref="place",
                               cascade="all, delete, delete-orphan")
        amenities = relationship("Amenity", secondary=place_amenity,
                                 back_populates="place_amenities",
                                 viewonly=False)
    else:
        city_id = ""
        user_id = ""
        name = ""
        description = ""
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0
        amenity_ids = []

        @property
        def reviews(self):
            """Returns a list if Review Instances matching place_id"""
            reviews = []
            for reviews in list(models.storage.all(Review).values()):
                if review.place_id == self.id:
                    reviews.append(review)
            return reviews

        @property
        def amenities(self):
            """Returns a list of Amenities matching amenities id."""
            amenities_list = []
            for amenity in list(models.storage.all(Amenity).values()):
                if amenity.id in self.amenity_ids:
                    amenities_list.append(amenity)
            return amenities

        @amenities.setter
        def amenities(self, value):
            if type(value) == Amenity:
                self.amenity_ids.append(value.id)
