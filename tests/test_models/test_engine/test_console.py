#!/usr/bin/python3
''' Test suite for the console'''


import sys
import models
import unittest
from unittest.mock import create_autospec
from io import StringIO
from console import HBNBCommand
from models import State
from models import storage
from models.engine.db_storage import DBStorage
from os import getenv

db = getenv("HBNB_TYPE_STORAGE", "fs")


class test_console(unittest.TestCase):
    ''' console test '''
    def setUp(self):
        '''setup '''
        self.capt_out = StringIO()
        sys.stdout = self.capt_out
        self.backup = sys.stdout

    def tearDown(self):
        ''' terdown '''
        sys.stdout = self.backup

    def create(self):
        ''' create HBNBCommand class instance '''
        return HBNBCommand()

    def test_quit(self):
        ''' Test console quit '''
        console = self.create()
        self.assertTrue(console.onecmd("quit"))

    def test_EOF(self):
        ''' Tests console EOF '''
        console = self.create()
        self.assertTrue(console.onecmd("EOF"))

    def test_all(self):
        ''' Test console all '''
        console = self.create()
        console.onecmd("all")
        self.assertTrue(isinstance(self.capt_out.getvalue(), str))

    @unittest.skipIf(db == "db", "Testing database storage only")
    def test_show_func(self):
        '''
            Tests show exists in database funcs
        '''
        console = self.create()
        console.onecmd("create User")
        user_id = self.capt_out.getvalue()
        sys.stdout = self.backup
        self.capt_out.close()
        self.capt_out = StringIO()
        sys.stdout = self.capt_out
        console.onecmd("show User " + user_id)
        x = (self.capt_out.getvalue())
        sys.stdout = self.backup
        self.assertTrue(str is type(x))

    @unittest.skipIf(db == "db", "Testing database storage only")
    def test_missing_class_name(self):
        '''
            Testing missing class name '''
        console = self.create()
        console.onecmd("create User")
        user_id = self.capt_out.getvalue()
        sys.stdout = self.backup
        self.capt_out.close()
        self.capt_out = StringIO()
        sys.stdout = self.capt_out
        console.onecmd("show")
        x = (self.capt_out.getvalue())
        sys.stdout = self.backup
        self.assertEqual("** class name missing **\n", x)

    def test_missing_id(self):
        ''' Tests missing id '''
        console = self.create()
        console.onecmd("create User")
        user_id = self.capt_out.getvalue()
        sys.stdout = self.backup
        self.capt_out.close()
        self.capt_out = StringIO()
        sys.stdout = self.capt_out
        console.onecmd("show User")
        x = (self.capt_out.getvalue())
        sys.stdout = self.backup
        self.assertEqual("** instance id missing **\n", x)

    @unittest.skipIf(db == "db", "Testing database storage only")
    def test_missing_id_message(self):
        ''' Tests missing id message '''
        console = self.create()
        console.onecmd("create User")
        user_id = self.capt_out.getvalue()
        sys.stdout = self.backup
        self.capt_out.close()
        self.capt_out = StringIO()
        sys.stdout = self.capt_out
        console.onecmd("show User " + "102361049")
        x = (self.capt_out.getvalue())
        sys.stdout = self.backup
        self.assertEqual("** no instance found **\n", x)

    def test_create_func(self):
        ''' Tests create func '''
        console = self.create()
        console.onecmd("create User email=lamprey@gmail.com password=a1b")
        self.assertTrue(isinstance(self.capt_out.getvalue(), str))

    def test_missing_class_name(self):
        ''' Test misssing classname message '''
        console = self.create()
        console.onecmd("create")
        x = (self.capt_out.getvalue())
        self.assertEqual("** class name missing **\n", x)

    def test_no_exist_class_name(self):
        '''
            Tests non existent class name message.
        '''
        console = self.create()
        console.onecmd("create Binita")
        x = (self.capt_out.getvalue())
        self.assertEqual("** class doesn't exist **\n", x)

    @unittest.skipIf(db != 'db', "Testing DBstorage only")
    def test_create_db(self):
        ''' tests create db '''
        console = self.create()
        console.onecmd("create State name=California")
        result = storage.all("State")
        self.assertTrue(len(result) > 0)
