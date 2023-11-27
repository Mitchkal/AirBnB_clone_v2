#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import Base
from models.base_model import BaseModel
from os import getenv
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

# from models.review import Review
# from models.place import Place
# from models.user import User


class User(BaseModel, Base):
    """This class defines a user by various attributes"""
    __tablename__ = "users"
    if getenv("HBNB_TYPE_STORAGE", "fs") == "db":
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128), nullable=True)
        last_name = Column(String(128), nullable=True)
        places = relationship("Place", backref="user",
                              cascade="delete")
        reviews = relationship("Review", backref="user",
                               cascade="delete")
    else:
        email = ''
        password = ''
        first_name = ''
        last_name = ''
