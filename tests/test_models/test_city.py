#!/usr/bin/python3

"""
This test module contains several unittest test cases on City class
that inherit from BaseModel class.

"""
from models.city import City
from models.base_model import BaseModel
import os
import pep8
import unittest


class TestCity(unittest.TestCase):
    """This class perform several test cases on the
    class City"""

    def test_pep8(self):
        """Test code conformity to pep8 style"""
        style = pep8.StyleGuide()
        num_err = 0
        files = ["models/city.py", "tests/test_models/test_city.py"]
        num_err += style.check_files(files).total_errors
        self.assertEqual(num_err, 0, "Wrong pep8 style, adjust your code!")

    def setUp(self):
        """Create default instance before each test case"""
        self.city = City()
        self.city.name = "Manchester"
        self.obj_dict = self.city.to_dict()
        self.obj_str = str(self.city)

    def tearDown(self):
        """Delete instance and file after each test case"""
        del self.city
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_class(self):
        """Test instance class"""
        self.assertTrue(isinstance(self.city, City))

    def test_to_dict(self):
        """Test instance conversion to dictionary"""
        self.assertTrue(isinstance(self.obj_dict, dict))
        self.assertTrue("__class__" in self.obj_dict)
        self.assertTrue(self.obj_dict["__class__"] == "City")

    def test_to_str(self):
        """Test instance conversion to string"""
        self.assertTrue(isinstance(self.obj_str, str))
        self.assertTrue(len(self.obj_str) > 1)

    def test_save(self):
        """Test if instance has been modified or updated"""
        self.city.save()
        self.assertTrue(self.city.created_at != self.city.updated_at)

    def test_fields(self):
        self.assertTrue(self.city.id != '')
        self.assertTrue(self.city.created_at != '')
        self.assertTrue(self.city.updated_at != '')
        self.assertTrue(self.city.state_id == '')
        self.assertTrue(self.city.name == "Manchester")
