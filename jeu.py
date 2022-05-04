from nbformat import read
import pygame
import pygame.locals

## Fonction permettant de créer une TileMap à partir d'une image
## IN:
## filename:    nom du fichier image
## width:       épaisseur d'une tile de la TileMap
## height:      hauteur d'une tile de la TileMap
##
## OUT:
## tile_table:  TileMap créer par la fonction
def load_tiles(filename, width: int, height: int):
    image = pygame.image.load(filename).convert()
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
def draw_map(screen, tile_table, map):
    player_pos = [0, 0]

    for x, row in enumerate(map):
        for y in enumerate(row):
            if int(y[1]) == 0:
                player_pos = [y[0]*100, x*100]
            screen.blit(tile_table[int(y[1])], (y[0]*100, x*100))
    return player_pos

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

if __name__=='__main__':
    pygame.init()
    screen = pygame.display.set_mode((1600, 1000))
    screen.fill((255, 255, 255))

    run = True

    map = open("map.txt", 'r').read().split('\n')
    if (check_map(map)):
        run = False
    
    last_moved = pygame.time.get_ticks()

    map_table = load_tiles("Tiles.png", 100, 100)
    player_table = load_tiles("Perso.png", 100, 100)

    player_pos = draw_map(screen, map_table, map)

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
        keys = pygame.key.get_pressed()
        if pygame.time.get_ticks() - last_moved >= 250:
            if (keys[pygame.K_RIGHT] and map[int(player_pos[1] / 100)][int(player_pos[0] / 100 + 1)] != '2'):
                player_pos[0] += 100
                last_moved = pygame.time.get_ticks()
            elif (keys[pygame.K_LEFT] and map[int(player_pos[1] / 100)][int(player_pos[0] / 100 - 1)] != '2'):
                player_pos[0] -= 100
                last_moved = pygame.time.get_ticks()
            elif (keys[pygame.K_DOWN] and map[int(player_pos[1] / 100 + 1)][int(player_pos[0] / 100)] != '2'):
                player_pos[1] += 100
                last_moved = pygame.time.get_ticks()
            elif (keys[pygame.K_UP] and map[int(player_pos[1] / 100 - 1)][int(player_pos[0] / 100)] != '2'):
                player_pos[1] -= 100
                last_moved = pygame.time.get_ticks()

        if map[int(player_pos[1] / 100)][int(player_pos[0] / 100)] == '1':
            run = False
            print("VICTOIRE")

        draw_map(screen, map_table, map)
        screen.blit(player_table[0], player_pos)
        pygame.display.flip()