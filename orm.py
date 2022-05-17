
from venv import create
from sqlalchemy import *
import sqlalchemy
from sqlalchemy.orm import sessionmaker
import models

def get_tiles(session):
    return session.query(models.Tile).order_by(models.Tile.tile_id).all()

def get_maps(session):
    return session.query(models.Map).order_by(models.Map.map_id).all()

def get_tests(session):
    return session.query(models.Test).order_by(models.Test.test_id).all()

def get_map_by_id(session, id):
    return session.query(models.Map).filter(models.Map.map_id == id).all()

def get_map_by_creator(session, creator):
    return session.query(models.Map).filter(models.Map.map_creator == creator).all()

def get_tile_by_id(session, id):
    return session.query(models.Tile).filter(models.Tile.tile_id == id).all()

def create_map(session, name, creator, layout):
    map = (
        session.query(models.Map)
        .filter(and_(models.Map.map_name == name), models.Map.map_creator == creator)
        .one_or_none()
    )
    if map is not None:
        return
    else:
        map = models.Map()
    
    map.map_name = name
    map.map_creator = creator
    map.map_create = sqlalchemy.func.now()
    map.map_update = sqlalchemy.func.now()
    map.map_layout = layout

    session.add(map)
    session.commit()
    

def update_map(session, new_map):
    map = (
        session.query(models.Map)
        .filter(models.Map.map_id == new_map.map_id)
        .all()
    )
    if map is None:
        return
    
    session.query(models.Map).filter(models.Map.map_id == new_map.map_id).update({'map_name': new_map.map_name, 'map_layout': new_map.map_layout, 'map_update': sqlalchemy.func.now()})
    session.commit()

def create_test(session, map, result):
    test = models.Test()

    test.test_result = result
    test.test_date = sqlalchemy.func.now()
    test.map_id = map.map_id

    session.add(test)
    session.commit()
