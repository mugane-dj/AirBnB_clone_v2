#!/usr/bin/python3
"""Defines unnittests for models/engine/db_storage.py."""
import pep8
import models
import MySQLdb
import unittest
from os import getenv
from models.base_model import Base
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.engine.db_storage import DBStorage
from models.engine.file_storage import FileStorage
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from sqlalchemy.engine.base import Engine


db = getenv("HBNB_TYPE_STORAGE")


@unittest.skipIf(db != "db", "Testing FileStorage only")
class TestDBStorage(unittest.TestCase):
    """Unittests for testing the DBStorage class."""

    @classmethod
    def setUpClass(cls):
        cls.storage = DBStorage()
        Base.metadata.create_all(cls.storage._DBStorage__engine)
        Session = sessionmaker(bind=cls.storage._DBStorage__engine)
        cls.storage._DBStorage__session = Session()

    @classmethod
    def tearDownClass(cls):
        cls.storage._DBStorage__session.close()
        del cls.storage

    def test_pep8(self):
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/engine/db_storage.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_engine_attribute(self):
        self.assertTrue(isinstance(self.storage._DBStorage__engine, Engine))

    def test_session_attribute(self):
        self.assertTrue(isinstance(self.storage._DBStorage__session, Session))
    
    def test_init_with_arg(self):
        with self.assertRaises(TypeError):
            DBStorage("mysqldb")

    def test_new_instance(self):
        new_obj = DBStorage()
        self.assertTrue(isinstance(new_obj, DBStorage))

    def test_all_cls_none(self):
        all_cls = self.storage.all()
        self.assertEqual(len(all_cls, 6))

    def test_all_cls(self):
        obj = self.storage.all(Place)
        self.assertEqual(self.place, list(obj.values())[0])

    def test_new(self):
        new_state = State(name="Arizona")
        self.storage.new(new_state)
        all_states = self.storage.all(State)
        self.assertIn(new_state, all_states)
