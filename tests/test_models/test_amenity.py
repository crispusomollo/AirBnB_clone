#!/usr/bin/python3

import unittest
import pep8
import os

from models.amenity import Amenity
from models.base_model import BaseModel


class TestAmenity(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.ameniti = Amenity()
        cls.ameniti.name = "Hot Tub"

    @classmethod
    def tearDownClass(cls):
        del cls.ameniti
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_style_check(self):
        """
        Tests pep8 style
        """
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/amenity.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_is_subclass(self):
        self.assertTrue(issubclass(self.ameniti.__class__, BaseModel), True)

    def test_checking_for_functions(self):
        self.assertIsNotNone(Amenity.__doc__)

    def test_has_attributes(self):
        self.assertTrue('id' in self.ameniti.__dict__)
        self.assertTrue('created_at' in self.ameniti.__dict__)
        self.assertTrue('updated_at' in self.ameniti.__dict__)
        self.assertTrue('name' in self.ameniti.__dict__)

    def test_attributes_are_strings(self):
        self.assertEqual(type(self.ameniti.name), str)

    def test_save(self):
        self.ameniti.save()
        self.assertNotEqual(self.ameniti.created_at, self.ameniti.updated_at)

    def test_to_dict(self):
        self.assertEqual('to_dict' in dir(self.ameniti), True)


if __name__ == "__main__":
    unittest.main()
