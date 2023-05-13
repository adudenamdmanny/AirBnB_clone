#!/usr/bin/env python3

"""
This test module contains several unittest test cases on State class
that inherit from BaseModel class.

"""
from models.state import State
from models.base_model import BaseModel
import os
import pep8
import unittest


class TestState(unittest.TestCase):
    """This class perform several test cases on the
    class State"""

    def test_pep8(self):
        """Test code conformity to pep8 style"""
        style = pep8.StyleGuide()
        num_err = 0
        files = ["models/state.py", "tests/test_models/test_state.py"]
        num_err += style.check_files(files).total_errors
        self.assertEqual(num_err, 0, "Wrong pep8 style, adjust your code!")

    def setUp(self):
        """Create default instance before each test case"""
        self.state = State()
        self.state.name = "United state"
        self.obj_dict = self.state.to_dict()
        self.obj_str = str(self.state)

    def tearDown(self):
        """Delete instance and file after each test case"""
        del self.state
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_class(self):
        """Test instance class"""
        self.assertTrue(isinstance(self.state, State))

    def test_to_dict(self):
        """Test instance conversion to dictionary"""
        self.assertTrue(isinstance(self.obj_dict, dict))
        self.assertTrue("__class__" in self.obj_dict)
        self.assertTrue(self.obj_dict["__class__"] == "State")

    def test_to_str(self):
        """Test instance conversion to string"""
        self.assertTrue(isinstance(self.obj_str, str))
        self.assertTrue(len(self.obj_str) > 1)

    def test_save(self):
        """Test if instance has been modified or updated"""
        self.state.save()
        self.assertTrue(self.state.created_at != self.state.updated_at)

    def test_fields(self):
        self.assertTrue(self.state.id != '')
        self.assertTrue(self.state.created_at != '')
        self.assertTrue(self.state.updated_at != '')
        self.assertTrue(self.state.name == "United state")
