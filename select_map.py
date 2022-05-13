import pygame
import pygame.locals
import jeu
import glob
import orm
import models
import size_select
import map_editor
from numpy import size

def select_map_edit(screen, session, creator):
    screen.fill((255, 255, 255))
    
    maps = orm.get_map_by_creator(session, creator)
    map_size = size(maps)
    if map_size == 0:
        size_select.size_select(screen, session, creator)
        return True
    map_selected = 0

    arrow_right = jeu.load_tiles("./sprites/Arrow_Right.png", 100, 100, True)
    arrow_left = jeu.load_tiles("./sprites/Arrow_Left.png", 100, 100, True)
    butt_edit = jeu.load_tiles("./sprites/Boutton_Jouer.jpg", 600, 100)
    butt_create = jeu.load_tiles("./sprites/Boutton_Créer.jpg", 600, 100)

    my_font = pygame.font.SysFont('arial', 70)
    creator_text = "Créer par: " + creator
    name_text = "Nom: " + maps[map_selected].map_name
    create_text = "Créer le: " + str(maps[map_selected].map_create)
    update_text = "Editer la dernière fois le: " + str(maps[map_selected].map_update)
    notable_text = "Blocs notables: "

    creator_surface = my_font.render(creator_text, False, (0, 0, 0))
    name_surface = my_font.render(name_text, False, (0, 0, 0))
    create_surface = my_font.render(create_text, False, (0, 0, 0))
    update_surface = my_font.render(update_text, False, (0, 0, 0))
    notable_surface = my_font.render(notable_text, False, (0, 0, 0))

    delay = pygame.time.get_ticks()

    mouse = None
    pos = (0, 0)

    run = True

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False

        mouse = pygame.mouse.get_pressed()
        pos = pygame.mouse.get_pos()

        if mouse[0] and pygame.time.get_ticks() - delay >= 250:
            delay = pygame.time.get_ticks()
            if (pos[0] <= 550 and pos [0] >= 650 and pos[1] >= 980):
                map_selected -= 1
                if (map_selected == -1):
                    map_selected = map_size - 1
                name_text = "Nom: " + map[map_selected].map_name
                create_text = "Créer le: " + map[map_selected].map_create
                update_text = "Editer la dernière fois le: " + map[map_selected].map_update
                name_surface = my_font.render(name_text, False, (0, 0, 0))
                create_surface = my_font.render(create_text, False, (0, 0, 0))
                update_surface = my_font.render(update_text, False, (0, 0, 0))
            if (pos[0] <= 1270 and pos [0] >= 1370 and pos[1] >= 980):
                map_selected += 1
                if (map_selected == map_size):
                    map_selected = 0
                name_text = "Nom: " + map[map_selected].map_name
                create_text = "Créer le: " + map[map_selected].map_create
                update_text = "Editer la dernière fois le: " + map[map_selected].map_update
                name_surface = my_font.render(name_text, False, (0, 0, 0))
                create_surface = my_font.render(create_text, False, (0, 0, 0))
                update_surface = my_font.render(update_text, False, (0, 0, 0))
            if (pos[0] >= 660 and pos [0] <= 1260 and pos[1] >= 880):
                map_editor.map_editor(screen, session, maps[map_selected])

        screen.fill((255, 255, 255))

        if (pos[0] >= 550 and pos[0] <= 650 and pos[1] >= 880):
            screen.blit(arrow_left[1], (550, 880))
        else:
            screen.blit(arrow_left[0], (550, 880))
        if (pos[0] >= 1270 and pos[0] <= 1370 and pos[1] >= 880):
            screen.blit(arrow_right[1], (1270, 880))
        else:
            screen.blit(arrow_right[0], (1270, 880))
        if (pos[0] >= 660 and pos[0] <= 1260 and pos[1] >= 880):
            screen.blit(butt_edit[1], (660, 880))
        else:
            screen.blit(butt_edit[0], (660, 880))

        screen.blit(creator_surface, (100, 100))
        screen.blit(name_surface, (100, 210))
        screen.blit(create_surface, (100, 320))
        screen.blit(update_surface, (100, 430))
        screen.blit(notable_surface, (100, 540))

        pygame.display.flip()
    
    return False
