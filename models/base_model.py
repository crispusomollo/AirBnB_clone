#!/usr/bin/python3

from datetime import datetime
from uuid import uuid4

import models

"""
Module BaseModel - Parent of all classes
"""

class BaseModel():
    """The Base class for Airbnb clone project
    Methods:
        __init__(self, *args, **kwargs)
        __save(self)
        __str__(self)
        __repr__(self)
        to_dict(self)
    """

    def __init__(self, *args, **kwargs):
        """
        Initialize attributes random uuid, dates created or updated
        """
        if kwargs:
            for key, val in kwargs.items():
                if "created_at" == key:
                    self.created_at = datetime.strptime(kwargs["created_at"],
                                                        "%Y-%m-%dT%H:%M:%S.%f")
                elif "updated_at" == key:
                    self.updated_at = datetime.strptime(kwargs["updated_at"],
                                                        "%Y-%m-%dT%H:%M:%S.%f")
                elif "__class__" == key:
                    pass
                else:
                    setattr(self, key, val)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """
        Returns a string of information about the model
        """
        return ('[{}] ({}) {}'.
                format(self.__class__.__name__, self.id, self.__dict__))

    def __repr__(self):
        """
        returns a string representation
        """
        return (self.__str__())

    def save(self):
        """
        Update an instance with updated time and save to serialized file
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        Return dictionary with string formats of times
        """
        dicn = {}
        dicn["__class__"] = self.__class__.__name__
        for k, v in self.__dict__.items():
            if isinstance(v, (datetime, )):
                dicn[k] = v.isoformat()
            else:
                dicn[k] = v
        return dicn
