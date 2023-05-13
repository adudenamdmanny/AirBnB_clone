#!/usr/bin/env python3

"""
This module contains several unittest test cases for the
class User that inherited from BaseModel class.

"""

from models.base_model import BaseModel
import os
import pep8
import unittest
from models.user import User


class TestUser(unittest.TestCase):
    """This class perform several test cases on the
    class User"""

    def test_pep8(self):
        """Test pep8 style"""
        style = pep8.StyleGuide()
        num_err = 0
        files = ["models/user.py", "tests/test_models/test_user.py"]
        num_err += style.check_files(files).total_errors
        self.assertEqual(num_err, 0, "Wrong pep8 style, adjust your code !")

    def setUp(self):
        """Create new instance for every test case"""
        self.user = User()
        self.user.first_name = "Temitope"
        self.obj_dict = self.user.to_dict()
        self.obj_str = str(self.user)

    def tearDown(self):
        """Delete instance and file for every test case"""
        del self.user
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_class(self):
        """Test the class of instance"""
        self.assertTrue(isinstance(self.user, User))

    def test_to_dict(self):
        """Test object conversion to dictionary"""
        self.assertTrue(isinstance(self.obj_dict, dict))
        self.assertTrue("__class__" in self.obj_dict)

    def test_to_str(self):
        """Test instance conversion to string"""
        self.assertTrue(isinstance(self.obj_str, str))
        self.assertTrue(len(self.obj_str) > 1)

    def test_fields(self):
        """Test instance default fields"""
        self.assertTrue(self.user.id != '')
        self.assertTrue(self.user.created_at != '')
        self.assertTrue(self.user.updated_at != '')
        self.assertTrue(self.user.email == '')
        self.assertTrue(self.user.password == '')
        self.assertTrue(self.user.first_name == 'Temitope')
        self.assertTrue(self.user.last_name == '')

    def test_save(self):
        """Test if instance has been updated or modified"""
        self.user.save()
        self.assertTrue(self.user.created_at != self.user.updated_at)
