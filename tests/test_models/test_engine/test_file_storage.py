#!/usr/bin/python3

"""
This test module contains several unittest test cases of
class FileStorage which is used to save all other objects.

"""

import os
import unittest
import pep8
import json
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.state import State
from models.review import Review
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """Test file storage class"""

    def test_pep8(self):
        """Test code style conformity to pep8 style"""
        style = pep8.StyleGuide()
        num_err = 0
        files = [
                "models/engine/file_storage.py",
                "tests/test_models/test_engine/test_file_storage.py"]
        num_err += style.check_files(files).total_errors
        self.assertEqual(num_err, 0, "Wrong pep8 style, adjust your code!")

    def setUp(self):
        """Create instances before every test case"""
        pass

    def tearDown(self):
        """Delete instances after each test case"""
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_all(self):
        """Test all command"""
        user = User()
        storage = FileStorage()
        store_obj = storage.all()
        self.assertTrue(len(store_obj) >= 1)
        self.assertTrue(isinstance(store_obj, dict))
        self.assertIsNotNone(store_obj)
        del user, storage

    def test_save(self):
        """Test the save"""
        storage = FileStorage()
        store_obj = storage.all()
        storage.save()
        with open("file.json", 'r', encoding="utf-8") as f:
            obj_str = f.read()
            self.assertTrue(isinstance(obj_str, str))
            self.assertIsNotNone(obj_str)
            self.assertTrue(isinstance(eval(obj_str), dict))
        del storage

    def test_new(self):
        """Test the new method"""
        storage = FileStorage()
        store_obj = storage.all()
        review = Review()
        key = "{}.{}".format(
                review.__class__.__name__,
                review.id)
        self.assertTrue(key in store_obj)
        self.assertTrue(len(store_obj) >= 2)
        del review, storage

    def test_reload(self):
        """Test storage reload"""
        storage = FileStorage()

        with open("file.json", "w") as my_file:
            my_file.write("{}")
        with open("file.json", "r") as text:
            for text in text:
                self.assertEqual(text, "{}")
        self.assertIs(storage.reload(), None)
        del storage
