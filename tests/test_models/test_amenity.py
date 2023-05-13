#!/usr/bin/env python3

"""
This test module contains several unittest test cases on Amenity class
that inherit from BaseModel class.

"""
from models.amenity import Amenity
from models.base_model import BaseModel
import os
import pep8
import unittest


class TestAmenity(unittest.TestCase):
    """This class perform several test cases on the
    class Amenity"""

    def test_pep8(self):
        """Test code conformity to pep8 style"""
        style = pep8.StyleGuide()
        num_err = 0
        files = ["models/amenity.py", "tests/test_models/test_amenity.py"]
        num_err += style.check_files(files).total_errors
        self.assertEqual(num_err, 0, "Wrong pep8 style, adjust your code!")

    def setUp(self):
        """Create default instance before each test case"""
        self.amenity = Amenity()
        self.amenity.name = "Electricity"
        self.obj_dict = self.amenity.to_dict()
        self.obj_str = str(self.amenity)

    def tearDown(self):
        """Delete instance and file after each test case"""
        del self.amenity
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_class(self):
        """Test instance class"""
        self.assertTrue(isinstance(self.amenity, Amenity))

    def test_to_dict(self):
        """Test instance conversion to dictionary"""
        self.assertTrue(isinstance(self.obj_dict, dict))
        self.assertTrue("__class__" in self.obj_dict)

    def test_to_str(self):
        """Test instance conversion to string"""
        self.assertTrue(isinstance(self.obj_str, str))
        self.assertTrue(len(self.obj_str) > 1)

    def test_save(self):
        """Test if instance has been modified or updated"""
        self.amenity.save()
        self.assertTrue(self.amenity.created_at != self.amenity.updated_at)

    def test_fields(self):
        self.assertTrue(self.amenity.id != '')
        self.assertTrue(self.amenity.created_at != '')
        self.assertTrue(self.amenity.updated_at != '')
        self.assertTrue(self.amenity.name == "Electricity")
