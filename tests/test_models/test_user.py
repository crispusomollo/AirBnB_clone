#!/usr/bin/python3

import unittest
import pep8
import os

from models.user import User
from models.base_model import BaseModel


class TestUser(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.user1 = User()
        cls.user1.first_name = "Betty"
        cls.user1.last_name = "Holberton"
        cls.user1.email = "airbnb@holbertonshool.com"
        cls.user1.password = "root"

    @classmethod
    def tearDownClass(cls):
        del cls.user1
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_style_check(self):
        """
        Tests pep8 style
        """
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/user.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_is_subclass(self):
        self.assertTrue(issubclass(self.user1.__class__, BaseModel), True)

    def test_checking_for_functions(self):
        self.assertIsNotNone(User.__doc__)

    def test_has_attributes(self):
        self.assertTrue('email' in self.user1.__dict__)
        self.assertTrue('id' in self.user1.__dict__)
        self.assertTrue('created_at' in self.user1.__dict__)
        self.assertTrue('updated_at' in self.user1.__dict__)
        self.assertTrue('password' in self.user1.__dict__)
        self.assertTrue('first_name' in self.user1.__dict__)
        self.assertTrue('last_name' in self.user1.__dict__)

    def test_attributes_are_strings(self):
        self.assertEqual(type(self.user1.email), str)
        self.assertEqual(type(self.user1.password), str)
        self.assertEqual(type(self.user1.first_name), str)
        self.assertEqual(type(self.user1.first_name), str)

    def test_save(self):
        self.user1.save()
        self.assertNotEqual(self.user1.created_at, self.user1.updated_at)

    def test_to_dict(self):
        self.assertEqual('to_dict' in dir(self.user1), True)


if __name__ == "__main__":
    unittest.main()

