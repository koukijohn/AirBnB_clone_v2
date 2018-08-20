#!/usr/bin/python3
'''
    Define the class Place.
'''
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Float, Table
import models
from sqlalchemy.orm import relationship
from os import getenv

place_amenity = Table('place_amenity', Base.metadata,
    Column('place_id', String(60), ForeignKey('places.id'),
            primary_key=True, nullable=False),
    Column('amenity_id', String(60), ForeignKey('amenities.id'),
           primary_key=True, nullable=False))

class Place(BaseModel, Base):
    '''
        Define the class Place that inherits from BaseModel.
    '''
    __tablename__ = 'places'
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    amenity_ids = []
    reviews = relationship('Review', backref='place', cascade='all, delete-orphan')
    amenities = relationship('Amenity', secondary=place_amenity, viewonly=False)

    @property
    def reviews(self):
        ''' getter for reviews '''
        review_items = models.storage.all('Reviews').values()
        return [obj for obj in review_items if obj.place_id == self.id]

    if getenv('HBNB_TYPE_STORAGE') == 'FileStorage':
        @property
        def reviews(self):
            ''' getter for amenities '''
            amenity_items = models.storage.all('Amenities').values()
            return [obj for obj in amenity_items if obj.amenity_id == self.id]

        @amenities.setter
        def amenities(self, obj):
            ''' setter for amenities '''
            if isinstance(obj, Amenity):
                self.amenity_ids.append(obj.id)
