#!/usr/bin/python3
""" user class """

from models.base_model import BaseModel
import json


class User(BaseModel):
    ''' The Base Model class'''

    email = ""
    password = ""
    firstname = ""
    lastname = ""
