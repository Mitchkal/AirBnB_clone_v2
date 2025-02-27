#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import Base
from models.base_model import BaseModel
# from models.amenity import Amenity
# from models.review import Review
from os import getenv
from sqlalchemy import Column, String, Integer, Float, ForeignKey, Table
from sqlalchemy.orm import relationship


place_amenity = Table(
    'place_amenity', Base.metadata,
    Column('place_id', String(60), ForeignKey('places.id'),
           primary_key=True, nullable=False),
    Column('amenity_id', String(60), ForeignKey('amenities.id'),
           primary_key=True, nullable=False)
)


class Place(BaseModel, Base):
    """ A place to stay """

    __tablename__ = "places"
    if getenv("HBNB_TYPE_STORAGE", "fs") == "db":
        city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
        user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024), nullable=True)
        number_rooms = Column(Integer, default=0, nullable=False)
        number_bathrooms = Column(Integer, default=0, nullable=False)
        max_guest = Column(Integer, default=0, nullable=False)
        price_by_night = Column(Integer, default=0, nullable=False)
        latitude = Column(Float, nullable=True)
        longitude = Column(Float, nullable=True)

        # user = relationship("User", backref="places")
        # city = relationship("City", backref="places")
        reviews = relationship("Review", cascade="all, delete, delete-orphan",
                               backref="place")
        amenities = relationship("Amenity", secondary=place_amenity,
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
            """getter implementation for revieews in Filestorage"""
            review_list = []
            from models import storage
            for review in storage.all("Review").values():
                if review.place_id == self.id:
                    review_list.append(review)
            return review_list

        @property
        def amenities(self):
            """Getter for amenities in file storage"""

            amenities_list = []
            for amenity in models.storage.all(Amenity).values():
                if amenity.place_id == self.id:
                    amenities_list.append(amenity)
                return amenities_list

        @amenities.setter
        def amenities(self, amenity=None):
            """sets the amenities"""
            if amenity:
                for amenity in models.storage.all(Amenity).values():
                    if amenity.place_id == self.id:
                        self.amenity_ids.append(amenity.id)
