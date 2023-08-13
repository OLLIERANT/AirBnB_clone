#!/usr/bin/python3
"""Writes a class BaseModel that defines all common attributes/methods
for other classes"""


import uuid
from datetime import datetime
import models
import json


class BaseModel():
    '''class BaseModel'''
    def __init__(self, *args, **kwargs):
        '''class constructor for class BaseModel'''
        if kwargs:
            kwargs['created_at'] = datetime.strptime(kwargs['created_at'],
                                                     '%Y-%m-%dT%H:%M:%S.%f')
            kwargs['updated_at'] = datetime.strptime(kwargs['updated_at'],
                                                     '%Y-%m-%dT%H:%M:%S.%f')

            for key, value in kwargs.items():
                if key != '__class__':
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        '''string of BaseModel instance'''
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def save(self):
        '''updates 'updated_at' instance with current datetime'''
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        '''dictionary representation of instance'''
        new_dict = dict(self.__dict__)
        new_dict['created_at'] = self.__dict__['created_at'].isoformat()
        new_dict['updated_at'] = self.__dict__['updated_at'].isoformat()
        new_dict['__class__'] = self.__class__.__name__
        return (new_dict)

    """Display BaseModel attributes"""
    print("[BaseModel] ({}) {}".format(my_model.id, vars(my_model)))

    """Convert BaseModel to a dictionary"""
    model_dict = {
            'id': my_model.id,
            'created_at': my_model.created_at.isoformat(),
            'updated_at': my_model.updated_at.isoformat(),
            'name': my_model.name,
            'my_number': my_model.my_number,
            '__class__': my_model.__class__.__name__
            }

    """Display BaseModel dictionary"""
    print("{}".format(json.dumps(model_dict, indent=4)))

    """Display JSON serialization of my_model"""
    print("JSON of my_model:\n{}".format(json.dumps(model_dict, indent=4)))
