#!/usr/bin/python3
"""
Unit test for the BaseModel class
"""
import unittest
import pep8
import os

from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.baze = BaseModel()
        cls.baze.name = "Greg"
        cls.baze.my_number = 29

    @classmethod
    def tearDownClass(cls):
        del cls.baze
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_style_check(self):
        """
        Tests pep8 style
        """
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/base_model.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_checking_for_functions(self):
        self.assertIsNotNone(BaseModel.__doc__)
        self.assertIsNotNone(BaseModel.save.__doc__)
        self.assertIsNotNone(BaseModel.to_dict.__doc__)

    def test_attributes(self):
        self.assertTrue(hasattr(BaseModel, "__init__"))
        self.assertTrue(hasattr(BaseModel, "save"))
        self.assertTrue(hasattr(BaseModel, "to_dict"))

    def test_init(self):
        self.assertTrue(isinstance(self.baze, BaseModel))

    def test_save(self):
        self.baze.save()
        self.assertNotEqual(self.baze.created_at, self.baze.updated_at)

    def test_to_dict(self):
        base1_dict = self.baze.to_dict()
        self.assertEqual(self.baze.__class__.__name__, 'BaseModel')
        self.assertIsInstance(baze_dict['created_at'], str)
        self.assertIsInstance(baze_dict['updated_at'], str)


if __name__ == "__main__":
    unittest.main()
