import pygame
import pygame.locals
import jeu

## Fonction contenant la boucle de création de la map
## IN:
## screen:          écran sur lequel on affiche nos différentes images
## map:             carte vierge que l'on va édité
##
## OUT:
## False:           il y'a eu une erreur, ou la fenêtre a été fermée
## True:            l'utilisateur à terminée sa map
def map_editor(screen, map):
    screen.fill((255, 255, 255))

    mouse = None
    pos = (0, 0)

    select_in = False
    select_out = False
    select_wall = False
    select_ground = False

    select_set = jeu.load_tiles("Select.png", 50, 50)
    tile_set = jeu.load_tiles("Tiles.png", 50, 50)

    run = True

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
        
        mouse = pygame.mouse.get_pressed()
        pos = pygame.mouse.get_pos()

        if (mouse[0]):
            if (pos[0] >= 50 and pos[0] <= 100 and pos[1] >= 25 and pos[1] <= 75):
                select_in = True
                select_out = False
                select_wall = False
                select_ground = False
            elif (pos[0] >= 150 and pos[0] <= 200 and pos[1] >= 25 and pos[1] <= 75):
                select_in = False
                select_out = True
                select_wall = False
                select_ground = False
            elif (pos[0] >= 250 and pos[0] <= 300 and pos[1] >= 25 and pos[1] <= 75):
                select_in = False
                select_out = False
                select_wall = True
                select_ground = False
            elif (pos[0] >= 350 and pos[0] <= 400 and pos[1] >= 25 and pos[1] <= 75):
                select_in = False
                select_out = False
                select_wall = False
                select_ground = True
            elif (pos[0] >= 0 and pos[0] <= 1920 and pos[1] >= 0 and pos[1] <= 100):
                select_in = False
                select_out = False
                select_wall = False
                select_ground = False

        screen.blit(tile_set[0], (50, 25))
        screen.blit(tile_set[1], (150, 25))
        screen.blit(tile_set[2], (250, 25))
        screen.blit(tile_set[3], (350, 25))

        if select_in:
            screen.blit(select_set[0], (50, 25))
        if select_out:
            screen.blit(select_set[1], (150, 25))
        if select_wall:
            screen.blit(select_set[2], (250, 25))
        if select_ground:
            screen.blit(select_set[3], (350, 25))

        jeu.draw_map(screen, tile_set, map, (100, 100))

        pygame.display.flip()
    return False