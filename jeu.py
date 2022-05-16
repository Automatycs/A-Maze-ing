from nbformat import read
from numpy import size
import pygame
import pygame.locals
import orm
import astar

## Fonction permettant de créer une TileMap à partir d'une image
## IN:
## filename:    nom du fichier image
## width:       épaisseur d'une tile de la TileMap
## height:      hauteur d'une tile de la TileMap
##
## OUT:
## tile_table:  TileMap créer par la fonction
def load_tiles(filename, width: int, height: int, transparency=False):
    if  not transparency:
        image = pygame.image.load(filename).convert()
    else:
        image = pygame.image.load(filename).convert_alpha()
    image_width, useless = image.get_size()
    tile_table = []

    for tile_x in range(0, int(image_width/width)):
        rect = (tile_x*width, 0, width, height)
        tile_table.append(image.subsurface(rect))
    return tile_table

## Fonction permettant d'afficher la map
## IN:
## screen:      écran sur lequel on dessine notre map
## tile_table:  TileMap utilisé pour dessiné la map
## map:         array contenant la map
##
## OUT:
## player_pos: coordonée de la case entrée de la map
def draw_map(screen, tile_table, map, shift):
    player_pos = [0, 0]

    for x, row in enumerate(map):
        for y in enumerate(row):
            if int(y[1]) == 1:
                player_pos = [y[0]*50, x*50]
            screen.blit(tile_table[int(y[1])], (y[0]*50 + shift[0], x*50 + shift[1]))
    return player_pos

def get_map_size(map):
    height = size(map)
    width = len(map[0])

    return (width, height)

def get_exit(map):
    for x, row in enumerate(map):
        for y in enumerate(row):
            if int(y[1]) == 2:
                return (x, y[0])

def get_entry(map):
    for x, row in enumerate(map):
        for y in enumerate(row):
            if int(y[1]) == 1:
                return (x, y[0])

## Fonction permettant de vérifier si la map donnée est valide
## IN:
## map:         map à vérifier
##
## OUT:
## 0:           la map est valide
## 1:           la map est invalide
def check_map(map):
    cmpt_e, cmpt_s = 0, 0

    for x, row in enumerate(map):
        for y in enumerate(row):
            if (map[x][y[0]]) == '0':
                cmpt_e += 1
            if (map[x][y[0]]) == '1':
                cmpt_s += 1
    
    if cmpt_e == 0:
        print("Map invalide: aucune entrée n'a été trouvée!")
        return 1
    elif cmpt_e > 1:
        print("Map invalide: trop d'entrées trouvées!")
        return 1
    if cmpt_s == 0:
        print("Map invalide: aucune sortie n'a été trouvées")
        return 1
    elif cmpt_s > 1:
        print("Map invalide: trop de sorties trouvées!")
        return 1
    return 0

def to_map(map_str):
    map = map_str.split('\n')

    return(map)

## Fonction contenant la boucle de jeu
## IN:
## screen:          écran sur lequel on affiche nos différentes images
##
## OUT:
## False:           il y'a eu une erreur, ou la fenêtre a été fermée
## True:            le niveau a été réussi
def game(screen, session, map):
    screen.fill((255, 255, 255))

    shift = (100, 100)
    
    run = True

    layout = to_map(map.map_layout)

    print(layout)

    path = astar.astar(layout, get_entry(layout), get_exit(layout))


    pouet_size = size(path) / 2
    pouet = 0
    print(path)
    print(pouet_size)

    last_moved = pygame.time.get_ticks()

    map_table = []

    tiles = orm.get_tiles(session)

    for row in tiles:
        map_table.append(load_tiles(row.tile_image, 50, 50)[0])

    player_table = load_tiles("sprites/Perso.png", 50, 50)

    player_pos = draw_map(screen, map_table, to_map(map.map_layout), (100, 100))

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False

        if pygame.time.get_ticks() - last_moved >= 250 and pouet != pouet_size:
            last_moved = pygame.time.get_ticks()
            player_pos = (path[pouet][1] * 50, path[pouet][0] * 50)
            pouet += 1
        
        if layout[int(player_pos[1] / 50)][int(player_pos[0] / 50)] == '2':
            run = False
            print("VICTOIRE")

        draw_map(screen, map_table, to_map(map.map_layout), shift)
        screen.blit(player_table[0], (player_pos[0] + shift[0], player_pos[1] + shift[1]))
        pygame.display.flip()
    return True