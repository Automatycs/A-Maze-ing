import sqlite3
from sqlite3 import Error

def sql_connect():
    try:
        con = sqlite3.connect('amazeing.db')
        return con
    except Error:
        print(Error)

def map_table(con):
    my_cursor = con.cursor()

    my_cursor.execute("CREATE TABLE IF NOT EXISTS maps(map_id INTEGER PRIMARY KEY, map_name TEXT NOT NULL, map_creator TEXT NOT NULL, map_create DATE, map_update DATE, map_layout TEXT NOT NULL)")
    con.commit()

def tile_table(con):
    my_cursor = con.cursor()

    my_cursor.execute("CREATE TABLE IF NOT EXISTS tiles(tile_id INTEGER PRIMARY KEY, tile_cross BOOLEAN NOT NULL, tile_effect TEXT NOT NULL, tile_name TEXT NOT NULL, tile_image STRING NOT NULL, tile_min INTEGER, tile_max INTEGER)")
    con.commit()

    my_cursor.execute("INSERT INTO tiles(tile_id, tile_cross, tile_effect, tile_name, tile_image, tile_min, tile_max) VALUES (1, 0, 'None', 'Mur', 'sprites/Mur.png', 1, 700), (2, 1, 'None', 'Entrée', 'sprites/Entrée.png', 1, 1), (3, 1, 'Win', 'Sortie', 'sprites/Sortie.png', 1, 1), (4, 1, 'None', 'Sol', 'sprites/Sol.png', 1, 700), (5, 1, 'Slow', 'Boue', 'sprites/Boue.png', 0, 700), (6, 1, 'Kill', 'Piège', 'sprites/Piège.png', 0, 700)")
    con.commit()

def test_table(con):
    my_cursor = con.cursor()
    my_cursor.execute("CREATE TABLE IF NOT EXISTS tests(test_id INTEGER PRIMARY KEY, test_date DATE, test_result BOOLEAN NOT NULL, map_id INTEGER NOT NULL, FOREIGN KEY(map_id) REFERENCES map(map_id))")

    con.commit()

con = sql_connect()
map_table(con)
tile_table(con)
test_table(con)