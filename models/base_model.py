#!usr/bin/python3
"""Base Model class"""
from uuid import uuid4
from datetime import datetime
import models


class BaseModel:
    """Define Base Model"""

    def __init__(self, *args, **kwargs):
        """method to initialize base model"""

        if len(kwargs):
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    self.__dict__[key] = datetime.strptime(
                            value, "%Y-%m-%dT%H:%M:%S.%f")
                else:
                    self.__dict__[key] = value
            del self.__dict__['__class__']

        else:
            self.id = str(uuid4())
            self.created_at = datetime.today()
            self.updated_at = datetime.today()
            models.storage.new(self)

    def __str__(self):
        """print the representation of instance"""
        return "[{}] ({}) {}".format(
                self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """update the public instance updated_at with the current datetime"""
        self.updated_at = datetime.today()
        models.storage.save()

    def to_dict(self):
        """fucntion that returns a dictionary
        containing all keys/values of __dict__"""
        Dict = self.__dict__.copy()
        Dict["__class__"] = self.__class__.__name__
        Dict["created_at"] = self.created_at.isoformat()
        Dict["updated_at"] = self.updated_at.isoformat()
        return Dict
