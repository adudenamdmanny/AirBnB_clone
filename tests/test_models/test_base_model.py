#!/usr/bin/python3

"""
This module contains several unittest test cases of the base class of our
AirBnB project i.e BaseModel class.

The tests can be run using these commands:
    python3 -m unittest tests/test_models/test_base_model.py
    python3 -m unittest discover tests

"""

import unittest
from datetime import datetime
import os
import pep8
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):

    def setUp(self):
        self.obj = BaseModel()
        self.obj.name = "Temmy"
        self.obj.age = 26
        self.obj_dict = self.obj.to_dict()
        self.obj_str = str(self.obj)

    def tearDown(self):
        del self.obj
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_pep8(self):
        """Test to validate PEP 8"""
        style = pep8.StyleGuide()
        num_err = 0
        files = [
                "models/base_model.py",
                "tests/test_models/test_base_model.py"]
        num_err += style.check_files(files).total_errors
        self.assertEqual(num_err, 0, "Wrong Pep8 style, adjust your code !")

    def test_attributes(self):
        """Test for class methods"""
        self.assertTrue(hasattr(BaseModel, "__init__"))
        self.assertTrue(hasattr(BaseModel, "to_dict"))
        self.assertTrue(hasattr(BaseModel, "save"))
        self.assertTrue(hasattr(BaseModel, "__str__"))

    def test_fields_type(self):
        self.assertTrue(type(self.obj.id) == str)
        self.assertTrue(type(self.obj.created_at) == datetime)
        self.assertTrue(type(self.obj.updated_at) == datetime)
        self.assertTrue(len(self.obj.id) > 3)
        self.assertTrue(self.obj.name == "Temmy")
        self.assertTrue(self.obj.age == 26)

    def test_class(self):
        """Test if object is of BaseModel class"""
        self.assertTrue(isinstance(self.obj, BaseModel))

    def test_to_dictionary(self):
        """Test if object returns a dictionary"""
        self.assertTrue(isinstance(self.obj_dict, dict))
        self.assertTrue("__class__" in self.obj_dict)
        self.assertTrue(self.obj_dict["__class__"] == "BaseModel")

    def test_to_string(self):
        """Test if object is a string and also its length"""
        self.assertTrue(isinstance(self.obj_str, str))
        self.assertTrue(len(self.obj_str) > 0)

    def test_save(self):
        """Test if correctly saved and time changed"""
        self.obj.save()
        self.assertFalse(self.obj.created_at == self.obj.updated_at)

    def test_fields(self):
        """Test class fields"""
        self.assertTrue(self.obj.id != '')
        self.assertTrue(self.obj.created_at != '')
        self.assertTrue(self.obj.updated_at != '')
