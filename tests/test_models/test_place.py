#!/usr/bin/python3

import unittest
import pep8
import os

from models.place import Place
from models.base_model import BaseModel


class TestPlace(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.plase = Place()
        cls.plase.city_id = "Somewhere in India"
        cls.plase.user_id = "Aladdin"
        cls.plase.name = "Taj Mahal"
        cls.plase.description = "Fit for a king"
        cls.plase.number_rooms = 0
        cls.plase.number_bathrooms = 0
        cls.plase.max_guest = 0
        cls.plase.price_by_night = 0
        cls.plase.latitude = 0.0
        cls.plase.longitude = 0.0
        cls.plase.amenity_ids = []

    @classmethod
    def tearDownClass(cls):
        del cls.plase
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_style_check(self):
        """
        Tests pep8 style
        """
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/place.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_is_subclass(self):
        self.assertTrue(issubclass(self.plase.__class__, BaseModel), True)

    def test_checking_for_functions(self):
        self.assertIsNotNone(Place.__doc__)

    def test_has_attributes(self):
        self.assertTrue('id' in self.plase.__dict__)
        self.assertTrue('created_at' in self.plase.__dict__)
        self.assertTrue('updated_at' in self.plase.__dict__)
        self.assertTrue('city_id' in self.plase.__dict__)
        self.assertTrue('user_id' in self.plase.__dict__)
        self.assertTrue('name' in self.plase.__dict__)
        self.assertTrue('description' in self.plase.__dict__)
        self.assertTrue('number_rooms' in self.plase.__dict__)
        self.assertTrue('number_bathrooms' in self.plase.__dict__)
        self.assertTrue('max_guest' in self.plase.__dict__)
        self.assertTrue('price_by_night' in self.plase.__dict__)
        self.assertTrue('latitude' in self.plase.__dict__)
        self.assertTrue('longitude' in self.plase.__dict__)
        self.assertTrue('amenity_ids' in self.plase.__dict__)

    def test_attributes_are_strings(self):
        self.assertEqual(type(self.plase.city_id), str)
        self.assertEqual(type(self.plase.user_id), str)
        self.assertEqual(type(self.plase.name), str)
        self.assertEqual(type(self.plase.description), str)
        self.assertEqual(type(self.plase.number_rooms), int)
        self.assertEqual(type(self.plase.number_bathrooms), int)
        self.assertEqual(type(self.plase.max_guest), int)
        self.assertEqual(type(self.plase.price_by_night), int)
        self.assertEqual(type(self.plase.latitude), float)
        self.assertEqual(type(self.plase.longitude), float)
        self.assertEqual(type(self.plase.amenity_ids), list)

    def test_save(self):
        self.plase.save()
        self.assertNotEqual(self.plase.created_at, self.plase.updated_at)

    def test_to_dict(self):
        self.assertEqual('to_dict' in dir(self.plase), True)


if __name__ == "__main__":
    unittest.main()
