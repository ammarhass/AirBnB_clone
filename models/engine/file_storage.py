#!/usr/bin/python3
"""FileStorage class"""
import json
import os
from models.base_model import BaseModel
from models.state import State
from models.amenity import Amenity
from models.city import City
from models.user import User
from models.review import Review
from models.place import Place


class FileStorage:
    """define a FileStorage class"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary of __objects"""
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        if obj:
            key = f"{obj.__class__.__name__}.{obj.id}"
            self.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file(path:__file_path)"""
        Dict = {}
        for key, value in self.__objects.items():
            Dict[key] = value.to_dict()

        with open(self.__file_path, "w") as f:
            json.dump(Dict, f)

    def reload(self):
        """deserializes the JSON file to __objects"""
        if not os.path.exists(self.__file_path):
            return

        with open(self.__file_path, 'r') as f:
            objs = json.load(f)
            self.__objects = {}
            for key, value in objs.items():
                class_name = value["__class__"]
                self.__objects[key] = eval(class_name)(**objs[key])
