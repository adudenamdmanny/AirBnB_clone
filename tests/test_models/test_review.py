#!/usr/bin/python3

"""
This test module contains several unittest test cases on Review class
that inherit from BaseModel class.

"""
from models.review import Review
from models.base_model import BaseModel
import os
import pep8
import unittest


class TestReview(unittest.TestCase):
    """This class perform several test cases on the
    class Review"""

    def test_pep8(self):
        """Test code conformity to pep8 style"""
        style = pep8.StyleGuide()
        num_err = 0
        files = ["models/review.py", "tests/test_models/test_review.py"]
        num_err += style.check_files(files).total_errors
        self.assertEqual(num_err, 0, "Wrong pep8 style, adjust your code!")

    def setUp(self):
        """Create default instance before each test case"""
        self.review = Review()
        self.review.text = "I love this place"
        self.obj_dict = self.review.to_dict()
        self.obj_str = str(self.review)

    def tearDown(self):
        """Delete instance and file after each test case"""
        del self.review
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_class(self):
        """Test instance class"""
        self.assertTrue(isinstance(self.review, Review))

    def test_to_dict(self):
        """Test instance conversion to dictionary"""
        self.assertTrue(isinstance(self.obj_dict, dict))
        self.assertTrue("__class__" in self.obj_dict)
        self.assertTrue(self.obj_dict["__class__"] == "Review")

    def test_to_str(self):
        """Test instance conversion to string"""
        self.assertTrue(isinstance(self.obj_str, str))
        self.assertTrue(len(self.obj_str) > 1)

    def test_save(self):
        """Test if instance has been modified or updated"""
        self.review.save()
        self.assertTrue(self.review.created_at != self.review.updated_at)

    def test_fields(self):
        self.assertTrue(self.review.id != '')
        self.assertTrue(self.review.created_at != '')
        self.assertTrue(self.review.updated_at != '')
        self.assertTrue(self.review.place_id == '')
        self.assertTrue(self.review.user_id == '')
        self.assertTrue(self.review.text == "I love this place")
