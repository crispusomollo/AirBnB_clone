#!/usr/bin/python3
'''File Storage Implementation'''

import json
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class FileStorage:
    '''JSON files Serialization and Deserialization'''

    __file_path = 'file.json'
    __objects = {}
    class_dict = {"BaseModel": BaseModel, "User": User, "Place": Place,
                  "Amenity": Amenity, "City": City, "Review": Review,
                  "State": State}

    def all(self):
        '''Return dictionary of class id object instance'''
        return self.__objects

    def new(self, obj):
        '''Add new object to an existing dictionary of instances'''
        if obj:
            key = '{}.{}'.format(obj.__class__.__name__, obj.id)
            self.__objects[key] = obj

    def save(self):
        '''Save obj dictionaries to json file'''
        dicn = {}

        for key, obj in self.__objects.items():
            '''if type(obje) is dict:
            dicn[key] = obje
            else:'''
            dicn[key] = obj.to_dict()
        with open(self.__file_path, 'w') as f:
            json.dump(dicn, f)

    def reload(self):
        '''If json file exists, convert object dicts back to instances'''
        try:
            with open(self.__file_path, 'r') as f:
                obj1 = json.load(f)
            for key, val in obj1.items():
                obj1 = self.class_dict[val['__class__']](**val)
                self.__objects[key] = obj
        except FileNotFoundError:
            pass
