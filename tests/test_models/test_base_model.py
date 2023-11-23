#!/usr/bin/python3
""" """
from models.base_model import BaseModel
import unittest
import datetime
from uuid import UUID
import json
import os


class test_basemodel(unittest.TestCase):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = 'BaseModel'
        self.value = BaseModel

    def setUp(self):
        """ """
        self.the_model = BaseModel()
        self.the_model.name = "nameless"
        self.new = BaseModel()

    def test_type_id(self):
        """verifies id type"""
        self.assertEqual("<class 'str'>", str(type(self.the_model.id)))

    def tearDown(self):
        """teardown"""
        del self.the_model

    def test_default(self):
        """ """
        i = self.value()
        self.assertEqual(type(i), self.value)

    def test_kwargs(self):
        """ """
        i = self.value()
        copy = i.to_dict()
        new = BaseModel(**copy)
        self.assertFalse(new is i)

    def test_kwargs_int(self):
        """ """
        i = self.value()
        copy = i.to_dict()
        copy.update({1: 2})
        with self.assertRaises(TypeError):
            new = BaseModel(**copy)

    @unittest.skipIf(storage == "db", "Testing database storage only")
    def test_save(self):
        """Checks that the dates differ with updated at"""
        old_update = self.new.updated_at
        self.new.save()
        self.assertNotEqual(self.new.updated_at, old_update)

    """def test_save(self):
        """ """
        i = self.value()
        i.save()
        key = self.name + "." + i.id
        with open('file.json', 'r') as f:
            j = json.load(f)
            self.assertEqual(j[key], i.to_dict())"""

    @unittest.skipIf(storage != "db", "Testing if using DBStorage")
    def test_basemodel_attrtype(self):
        """verifies attributes types"""
        new2 = BaseModel
        self.assertFalse(isinstance(news.id, str))
        self.assertFalse(isinstance(news.created_at, str))
        self.assertFalse(isinstance(news.updated_at, str))

    @unittest.skipIf(storage != "db", "Testing if using DBStorage")
    def test_basemodel_hasattr(self):
        """verifies Class attributes"""
        self.assertTrue(hasattr(self.new, "id"))
        self.assertTrue(hasattr(self.new, "created_at"))
        self.assertTrue(hasattr(self.new, "updated_at"))

    def test_str(self):
        """ """
        i = self.value()
        self.assertEqual(str(i), '[{}] ({}) {}'.format(self.name, i.id,
                         i.__dict__))

    def test_todict(self):
        """ """
        i = self.value()
        n = i.to_dict()
        self.assertEqual(i.to_dict(), n)

    def test_kwargs_none(self):
        """ """
        n = {None: None}
        with self.assertRaises(TypeError):
            new = self.value(**n)

    def test_kwargs_one(self):
        """ """
        n = {'Name': 'test'}
        with self.assertRaises(KeyError):
            new = self.value(**n)

    def test_id(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.id), str)

    def test_created_at(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.created_at), datetime.datetime)

    def test_updated_at(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.updated_at), datetime.datetime)
        n = new.to_dict()
        new = BaseModel(**n)
        self.assertFalse(new.created_at == new.updated_at)
