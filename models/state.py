#!/usr/bin/python3
'''
    Implementation of the State class
'''
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base
from models.city import City
import models
from os import getenv


class State(BaseModel, Base):
    '''
        Implementation for the State.
    '''

    __tablename__ = "states"

#  changed placement

    if getenv("HBNB_TYPE_STORAGE") == "db":
        print("db mode")
        name = Column(String(128), nullable=False)
        cities = relationship('City', backref='State',
                              cascade='all, delete-orphan')

#    if getenv("HBNB_TYPE_STORAGE") == "db":
#        print("db mode")
    else:
        print("FileStorage mode")
        name = ""

        @property
        def cities(self):
            '''Getter for cities'''

            get_all = models.storage.all('City')
            return [obj for obj in get_all if obj.state_id == self.id]

#    def __str__(self):
#        print(type(models.storage))

#  if __name__ == "__main__":
#    x = State()
#    print(x)
