import string
import pygame
import pygame.locals
from requests import session
import jeu
import orm
import models
from numpy import size

def to_string(array):
    string = ""

    for x, row in enumerate(array):
        for y in enumerate(row):
            string += array[x][y[0]]
        string += '\n'
    string  = string[:-1]

    print(string)
    return string

## Fonction contenant la boucle de création de la map
## IN:
## screen:          écran sur lequel on affiche nos différentes images
## map:             carte vierge que l'on va édité
##
## OUT:
## False:           il y'a eu une erreur, ou la fenêtre a été fermée
## True:            l'utilisateur à terminée sa map
def map_editor(screen, session, map, new_map=False):
    screen.fill((255, 255, 255))

    tiles = orm.get_tiles(session)
    tiles_size = size(tiles)
    selected = 0

    layout = jeu.to_map(map.map_layout)
    map_size = jeu.get_map_size(layout)

    my_font = pygame.font.SysFont('arial', 70)

    mouse = None
    pos = (0, 0)

    delay = pygame.time.get_ticks()

    name_selected = False


    name_text = my_font.render("Nom:", False, (0, 0, 0))
    input_tile = jeu.load_tiles("sprites/Input_Space.png", 300, 100)
    input_text = map.map_name
    input_surface = my_font.render(input_text, False, (0, 0, 0))

    r_arrow = jeu.load_tiles("./sprites/Arrow_Right.png", 100, 100, True)
    l_arrow = jeu.load_tiles("./sprites/Arrow_Left.png", 100, 100, True)
    butt_set = jeu.load_tiles("sprites/Boutton_Créer.jpg", 600, 100)
    
    tile_set = []

    for row in tiles:
        print(row.tile_name)
        tile_set.append(jeu.load_tiles(row.tile_image, 50, 50)[0])

    tyle_name = my_font.render(tiles[selected].tile_name, False, (0, 0, 0))

    run = True

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.KEYDOWN:
                if name_selected:
                    if event.key == pygame.K_BACKSPACE:
                        input_text = input_text[:-1]
                    else:
                        input_text += event.unicode
                    input_surface = my_font.render(input_text, False, (0, 0, 0))

        
        mouse = pygame.mouse.get_pressed()
        pos = pygame.mouse.get_pos()

        if (mouse[0] and pygame.time.get_ticks() - delay >= 250):
            delay = pygame.time.get_ticks()
            if (pos[0] >= 850 and pos[0] <= 1100 and pos[1] >= 0 and pos[1] <= 100):
                name_selected = True
            elif (pos[0] >= 0 and pos[0] <= 1920 and pos[1] >= 0 and pos[1] <= 100):
                name_selected = False
            if pos[0] >= 10 and pos[0] <= 110 and pos[1] >= 0 and pos[1] <= 100:
                selected -= 1
                if selected == -1:
                    selected = tiles_size - 1
            if pos[0] >= 510 and pos[0] <= 610 and pos[1] >= 0 and pos[1] <= 100:
                selected += 1
                if selected == tiles_size:
                    selected = 0
            if pos[0] >= 1320 and pos[0] <= 1920 and pos[1] >= 0 and pos[1] <= 100 and input_text != "":
                map.map_layout = to_string(layout)
                if new_map:
                    orm.create_map(session, input_text, map.map_creator, map.map_layout)
                else:
                    orm.update_map(session, map)
                return False
            tyle_name = my_font.render(tiles[selected].tile_name, False, (0, 0, 0))
        
        screen.fill((255, 255, 255))

        if pos[0] >= 1320 and pos[0] <= 1920 and pos[1] >= 0 and pos[1] <= 100:
            screen.blit(butt_set[1], (1320, 0))
        else:
            screen.blit(butt_set[0], (1320, 0))
        if pos[0] >= 10 and pos[0] <= 110 and pos[1] >= 0 and pos[1] <= 100:
            screen.blit(l_arrow[1], (10, 0))
        else:
            screen.blit(l_arrow[0], (10, 0))
        if pos[0] >= 510 and pos[0] <= 610 and pos[1] >= 0 and pos[1] <= 100:
            screen.blit(r_arrow[1], (510, 0))
        else:
            screen.blit(r_arrow[0], (510, 0))

        screen.blit(tyle_name, (210, 10))
        screen.blit(tile_set[selected], (135, 25))

        screen.blit(name_text, (650, 10))
        if name_selected:
            screen.blit(input_tile[1], (850, 0))
        else:
            screen.blit(input_tile[0], (850, 0))
        screen.blit(input_surface, (860, 10))

    
        if mouse[0] and pos[0] >= 100  and pos[1] >= 100 and pos[0] < 100 + map_size[0] * 50 and pos[1] < 100 + map_size[1] * 50:
            tmp = list(layout[int((pos[1] - 100) / 50)])
            tmp[int((pos[0] - 100) / 50)] = str(selected)
            layout[int((pos[1] - 100) / 50)] = "".join(tmp)
        
        jeu.draw_map(screen, tile_set, layout, (100, 100))

        pygame.display.flip()
    return False