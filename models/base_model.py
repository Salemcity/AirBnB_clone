#!/usr/bin/python3
"""A Python script that describes the base model"""

import uuid
from models import storage
from datetime import datetime


class BaseModel:
    """
    This is the BaseModel class

    Attributes:
        id (str): id of the instance
        created_at (datetime): creation date
        updated_at (datetime): update date

    Methods:
        __init__(self, *args, **kwargs)
        __str__(self)
        save(self)
        to_dict(self)
    """

    def __init__(self, *args, **kwargs):
        """
        Constructor of the BaseModel class

        Args:
            *args: Unused
            **kwargs: Dictionary containing attribute names and values
        """

        if kwargs:
            for key, value in kwargs.items():
                if key != '__class__':
                    setattr(self, key, value)
            self.created_at = datetime.strptime(
                self.created_at, "%Y-%m-%dT%H:%M:%S.%f")
            self.updated_at = datetime.strptime(
                self.updated_at, "%Y-%m-%dT%H:%M:%S.%f")
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """
        Prints the BaseModel attributes
        """
        class_name = self.__class__.__name__
        return f"[{class_name}] ({self.id}) {self.__dict__}"

    def save(self):
        """
        Updates the public instance attribute updated_at
        with the current datetime and saves the instance to storage
        """
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """
        Returns a dictionary containing all keys/values
        of the __dict__ of the instance
        """
        new_dict = vars(self).copy()
        new_dict["__class__"] = self.__class__.__name__
        new_dict["created_at"] = self.created_at.isoformat()
        new_dict["updated_at"] = self.updated_at.isoformat()
        return new_dict
