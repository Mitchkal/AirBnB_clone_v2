#!/usr/bin/python3
"""
module db_storage
"""

import models
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker, scoped_session
import models
from models.city import City
from models.state import State
from models.base_model import Base
from os import getenv


class DBStorage:
    """manages SQLAlchemy with MySQL"""

    __engine = None
    __session = None

    def __init__(self):
        """initializes instance of DBStorage"""
        user = getenv('HBNB_MYSQL_USER')
        pwd = getenv('HBNB_MYSQL_PWD')
        host = getenv('HBNB_MYSQL_HOST')
        db = getenv('HBNB_MYSQL_DB')
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
            user, pwd, host, db), pool_pre_ping=True)

        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Queries all objects depending on classs name"""
        from models import classes

        obj_dict = {}
        if cls:
            query_objs = self.__session.query(classes[cls]).all()
        else:
            query_objs = []
            for k in classes.values():
                query_objs.extend(self.__session.query(k).all())

        for obj in query_objs:
            key = '{}.{}'.format(obj.__class__.__name__, obj.id)
            obj_dict[key] = obj

        return obj_dict

    def new(self, obj):
        """adds new object to current database session"""
        self.__session.add(obj)

    def save(self):
        """commits changes to current session"""
        self.__session.commit()

    def delete(self, obj=None):
        """deletes current DB session"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """creates all tables in DB and created DB session"""
        Base.metadata.create_all(self.__engine)
        Session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(Session)

    def close(self):
        """close current session"""
        self.__session.remove()
