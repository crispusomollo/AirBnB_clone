#!/usr/bin/python3
"""
Module for class Place
"""
from models.base_model import BaseModel


class Place(BaseModel):
    """
    Inherits from the BaseModel
    Public class attributes:
        city_id:             (str) will be City.id
        user_id:             (str) will be User.id
        amenity_ids:         (list) will be Amenity.id
        name:                (str)
        description:         (str)
        latitude:            (float) 0.0
        longitude:           (float) 0.0
        number_rooms:        (int) 0
        number_bathrooms:    (int) 0
        max_guest:           (int) 0
        price_by_night:      (int) 0
    """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
