#!/usr/bin/env python3

"""
This test module contains several unittest test cases on Place class
that inherit from BaseModel class.

"""
from models.place import Place
from models.base_model import BaseModel
import os
import pep8
import unittest
from datetime import datetime


class TestPlace(unittest.TestCase):
    """This class perform several test cases on the
    class Place"""

    def test_pep8(self):
        """Test code conformity to pep8 style"""
        style = pep8.StyleGuide()
        num_err = 0
        files = ["models/place.py", "tests/test_models/test_place.py"]
        num_err += style.check_files(files).total_errors
        self.assertEqual(num_err, 0, "Wrong pep8 style, adjust your code!")

    def setUp(self):
        """Create default instance before each test case"""
        self.place = Place()
        self.place.name = "Manchester"
        self.obj_dict = self.place.to_dict()
        self.obj_str = str(self.place)

    def tearDown(self):
        """Delete instance and file after each test case"""
        del self.place
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_class(self):
        """Test instance class"""
        self.assertTrue(isinstance(self.place, Place))

    def test_to_dict(self):
        """Test instance conversion to dictionary"""
        self.assertTrue(isinstance(self.obj_dict, dict))
        self.assertTrue("__class__" in self.obj_dict)
        self.assertTrue(self.obj_dict["__class__"] == "Place")

    def test_to_str(self):
        """Test instance conversion to string"""
        self.assertTrue(isinstance(self.obj_str, str))
        self.assertTrue(len(self.obj_str) > 1)

    def test_save(self):
        """Test if instance has been modified or updated"""
        self.place.save()
        self.assertTrue(self.place.created_at != self.place.updated_at)

    def test_fields(self):
        self.assertTrue(self.place.id != '')
        self.assertTrue(self.place.created_at != '')
        self.assertTrue(self.place.updated_at != '')
        self.assertTrue(self.place.city_id == '')
        self.assertTrue(self.place.user_id == '')
        self.assertTrue(self.place.name == "Manchester")
        self.assertTrue(self.place.description == '')
        self.assertTrue(self.place.number_rooms == 0)
        self.assertTrue(self.place.number_bathrooms == 0)
        self.assertTrue(self.place.max_guest == 0)
        self.assertTrue(self.place.price_by_night == 0)
        self.assertTrue(self.place.latitude == 0.0)
        self.assertTrue(self.place.longitude == 0.0)
        self.assertTrue(self.place.amenity_ids == [])

    def test_fields_type(self):
        self.assertTrue(isinstance(self.place.id, str))
        self.assertTrue(isinstance(self.place.created_at, datetime))
        self.assertTrue(isinstance(self.place.updated_at, datetime))
        self.assertTrue(isinstance(self.place.city_id, str))
        self.assertTrue(isinstance(self.place.user_id, str))
        self.assertTrue(isinstance(self.place.name, str))
        self.assertTrue(isinstance(self.place.description, str))
        self.assertTrue(isinstance(self.place.number_rooms, int))
        self.assertTrue(isinstance(self.place.number_bathrooms, int))
        self.assertTrue(isinstance(self.place.max_guest, int))
        self.assertTrue(isinstance(self.place.price_by_night, int))
        self.assertTrue(isinstance(self.place.latitude, float))
        self.assertTrue(isinstance(self.place.longitude, float))
        self.assertTrue(isinstance(self.place.amenity_ids, list))
