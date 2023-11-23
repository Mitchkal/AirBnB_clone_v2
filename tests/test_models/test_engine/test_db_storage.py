#!/usr/bin/python3
"""
Testing for module file_storage
"""


import sys
import unittest
import time
from os import getenv
from io import StringIO
from console import HBNBCommand
from models.engine.db_storage import DBStorage
from models.state import State
from models.user import User
from models import storage

db = getenv("HBNB_TYPE_STORAGE")


@unittest.skipIf(db != 'db', "Testing DBstorage only")
class test_DBStorage(unittest.TestCase):
    ''' Testing DB_STORAGE '''
    @classmethod
    def setupClass(cls):
        '''Initializatio'''

        cls.dbstorage = DBStorage()
        cls.output = StringIO()
        sys.stdout = cls.output

    @classmethod
    def tearDownClass(cls):
        '''delete'''
        del cls.dbstorage
        del cls.output

    def create(self):
        '''Create HBNB'''
        return HBNBCommand()

    def test_new(self):
        '''Testnew'''
        new_obj = State(name="Texas")
        self.assertEqual(new_obj.name, "Texas")

    def test_dbstorage_method_checks(self):
        """check methods"""
        self.assertTrue(hasattr(self.dbstorage, "__init__"))
        self.assertTrue(hasattr(self.dbstorage, "new"))
        self.assertTrue(hasattr(self.dbstorage, "save"))
        self.assertTrue(hasattr(self.dbstorage, "reload"))
        self.assertTrue(hasattr(self.dbstorage, "all"))
        self.assertTrue(hasattr(self.dbstorage, "delete"))

    def test_dbstorage_user(self):
        """test attributes"""
        new = User(email="droman@gmail.com", password="passkey")
        self.assertTrue(new.email, "droman@gmail.com")

    def test_dbstorage_new_save(self):
        """tests the save method"""
        new_state = State(name="Arkansas")
        storage.new(new_state)
        save_id = new_state.id
        result = storage.all("State")
        temp = []
        for key, val in result.items():
            temp.append(key.split('.')[1])
            obj = val
        self.assertTrue(save_id in temp)
        self.assertIsInstance(obj, State)

    def test_dbstorage_all(self):
        """test function all"""
        storage.reload()
        output = storage.all("")
        self.assertIsInstance(output, dict)
        self.assertEqual(len(output), 0)
        new = User(email="haematoma@gmail.com", password="hemlock")
        console = self.create()
        console.onecmd("create State name=Oregon")
        output = storage.all("State")
        self.assertTrue(len(output) > 0)

    def test_dbstorage_delete(self):
        """Testing deletion method"""
        new_user = User(email="leprucica@gmail.com", password="ali",
                        first_name="jemini", last_name="sage")
        storage.new(new_user)
        save_id = new_user.id
        key = "User.{}".format(save_id)
        self.assertIsInstance(new_user, User)
        storage.save()
        prev_result = storage.all("User")
        del_user_obj = prev_result[key]
        storage.delete(del_user_obj)
        curr_result = storage.all("User")
        self.assertNotEqual(len(prev_result), len(curr_result))

    def test_model_storage(self):
        """tests the storage method"""
        self.assertTrue(isinstance(storage, DBStorage))
