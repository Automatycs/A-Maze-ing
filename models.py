from sqlalchemy import *
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base
import os

Base = declarative_base()

class Map(Base):
    __tablename__ = "maps"
    map_id = Column(Integer, primary_key=True)
    map_name = Column(String)
    map_creator = Column(String)
    map_create = Column(Date)
    map_update = Column(Date)
    map_layout = Column(String)

class Test(Base):
    __tablename__ = "tests"
    test_id = Column(Integer, primary_key=True)
    test_date = Column(Date)
    test_result = Column(Boolean)
    map_id = Column(Integer, ForeignKey("maps.map_id"))

class Tile(Base):
    __tablename__ = "tiles"
    tile_id = Column(Integer, primary_key=True)
    tile_cross = Column(Boolean)
    tile_effect = Column(String)
    tile_name = Column(String)
    tile_image = Column(String)
    tile_min = Column(Integer)
    tile_max = Column(Integer)