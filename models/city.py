#!/usr/bin/python3
""" City class Module """
from models.base_model import BaseModel

class City(BaseModel):
    """
    Inherits from class BaseModel
    Public class attributes:
        state_id: (str) will be State.id
        name:     (str)
    """
    state_id = ""
    name = ""
