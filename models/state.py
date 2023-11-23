#!/usr/bin/python3
""" State Module for HBNB project """


from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base
import models
from os import getenv

class State(BaseModel, Base):
    """ State class """

    __tablename__ = 'states'

    if getenv("HBNB_TYPE_STORAGE") == "db":
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="state",
                              cascade="all, delete, delete-orphan")
    else:
        name = ""

    @property
    def cities(self):
        """getter for cities in FileStorage"""
        city_list = []
        for city in models.storage.all("City").values():
            if city.state_id == self.id:
                city_list.append(city)
        return city_list
