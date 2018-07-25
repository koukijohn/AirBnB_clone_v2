#!/usr/bin/python3
'''
    DBStorage Engine
'''

from sqlalchemy import MetaData, create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import BaseModel, Base
import os
import models
from models.city import City
from models.state import State
from models.amenity import Amenity
from models.user import User
from models.place import Place
from models.review import Review

class DBStorage:
    '''
        DBStorage Class
    '''
    __engine = None
    __session = None

    def __init__(self):
        '''
        Initializes DBStorage class
        '''
        #get values from environment variables
        user = os.getenv('HBNB_MYSQL_USER')
        password = os.getenv('HBNB_MYSQL_PWD')
        host = os.getenv('HBNB_MYSQL_HOST')
        database = os.getenv('HBNB_MYSQL_DB')
        #establish db connection
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                format(user, password, host, database), pool_pre_ping=True)
        #create tables with metadata
        Base.metadata.create_all(self.__engine)
        #special case for testing
        if os.getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)
        #start db session
        Session = sessionmaker(bind=self.__engine)
        self.__session = Session()

    def all(self, cls=None):
        '''
        Query on the current database session all objects
        depending of the class name.
        '''
        all_objects = {}
        if cls is None:
            obj_list = [City, State, User, Amenity, Review, Place]
            for cls in obj_list:
                for obj in self.__session.query(cls).all():
                    key = '{}.{}'.format(obj.__class__.__name__, obj.id)
                    all_objects[key] = obj
        else:
            for obj in self.__session.query(cls).all():
                key = '{}.{}'.format(obj.__class__.__name__, obj.id)
                all_objects[key] = obj
        return(all_objects)

    def new(self, obj):
        '''
        Add the object to the current database session.
        '''
        self.__session.add(obj)

    def save(self):
        '''
        Commit all changes of the current database session.
        '''
        self.__session.commit()

    def delete(self, obj=None):
        '''
        Deletes obj from db.
        '''
        if obj is not None:
            self.__session.delete(obj)
            self.save()

    def reload(self):
        '''
        Create all tables in the database and
        create the current database session.
        '''
        Base.metadata.create_all(self.__engine)
        Session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(Session)
        self.__session = Session
