#!/usr/bin/python3
'''
    Implementation of the State class
'''
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base
import models
from os import getenv


class State(BaseModel, Base):
    '''
        Implementation for the State.
    '''

    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship('City', back_populates='State', cascade='all, delete-orphan')


    if getenv("HBNB_TYPE_STORAGE") == "db":
        print("db_mode")
    else:
        print("FileStorage_mode")
        @property
        def cities(self):
            '''Getter for cities'''
            get_all = models.storage.all('City')
            return [obj for obj in get_all if obj.state_id == self.id]

    def __str__(self):
        print(type(models.storage))



if __name__ == "__main__":
    x = State()
    print(x)
