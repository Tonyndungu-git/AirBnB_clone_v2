#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Integer
from sqlalchemy.orm import relationship
import models
import os
from models.city import City

STRG = os.environ.get('HBNB_TYPE_STORAGE')

class State(BaseModel, Base):
    """ State class """
    if STRG == 'db':
        __tablename__ = "states"
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="state", cascade="all, delete")
    else:
        name = ""

    def __init__(self, *args, **kwargs):
        """initializes state"""
        super().__init__(*args, **kwargs)

    if  STRG != "db":
        @property
        def cities(self):
            """getter for list of city instances related to the state"""
            city_list = []
            all_cities = models.storage.all(City)
            for city in all_cities.values():
                if city.state_id == self.id:
                    city_list.append(city)
            return city_list
