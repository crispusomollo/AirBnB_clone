#!/usr/bin/python3

import unittest
import pep8
import os

from models.city import City
from models.base_model import BaseModel


class TestCity(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.citi = City()
        cls.citi.name = "Raleigh"
        cls.citi.state_id = "NC"

    @classmethod
    def tearDownClass(cls):
        del cls.citi
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_style_check(self):
        """
        Tests pep8 style
        """
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/city.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_is_subclass(self):
        self.assertTrue(issubclass(self.citi.__class__, BaseModel), True)

    def test_checking_for_functions(self):
        self.assertIsNotNone(City.__doc__)

    def test_has_attributes(self):
        self.assertTrue('id' in self.citi.__dict__)
        self.assertTrue('created_at' in self.citi.__dict__)
        self.assertTrue('updated_at' in self.citi.__dict__)
        self.assertTrue('state_id' in self.citi.__dict__)
        self.assertTrue('name' in self.citi.__dict__)

    def test_attributes_are_strings(self):
        self.assertEqual(type(self.citi.name), str)
        self.assertEqual(type(self.citi.state_id), str)

    def test_save(self):
        self.citi.save()
        self.assertNotEqual(self.citi.created_at, self.citi.updated_at)

    def test_to_dict(self):
        self.assertEqual('to_dict' in dir(self.citi), True)


if __name__ == "__main__":
    unittest.main()
