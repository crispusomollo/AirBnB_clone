#!/usr/bin/python3
"""
Review class Module
"""
from models.base_model import BaseModel

class Review(BaseModel):
    """
    Inherits from the BaseModel
    Public class attributes:
        place_id:           (str) will be Place.id
        user_id:            (str) will be User.id
        message:            (str)
    """
    place_id = ""
    user_id = ""
    message = ""
