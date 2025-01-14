#!/usr/bin/python3
""" City Module for HBNB project """
import models
from models.base_model import Base
from models.base_model import BaseModel
from os import getenv
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
# from models.state import State


class City(BaseModel, Base):
    """ The city class, contains state ID and name """
    __tablename__ = "cities"
    if getenv("HBNB_TYPE_STORAGE") == "db":
        # __tablename__ = "cities"

        name = Column(String(128), nullable=False)
        state_id = Column(String(60), ForeignKey("states.id"), nullable=False)
        places = relationship("Place", backref="cities",
                              cascade="all, delete, delete-orphan")
        # states = relationship('State', back_populates='cities')
    else:
        state_id = ""
        name = ""

    def __init__(self, *args, **kwargs):
        """initialize city"""
        super().__init__(*args, **kwargs)
