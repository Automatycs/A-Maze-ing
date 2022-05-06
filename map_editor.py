import pygame
import pygame.locals
import jeu

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
def map_editor(screen, map, map_size):
    screen.fill((255, 255, 255))

    file = open("map.txt", "r+")

    mouse = None
    pos = (0, 0)

    selected = ''

    butt_set = jeu.load_tiles("Boutton_Créer.jpg", 600, 100)
    select_set = jeu.load_tiles("Select.png", 50, 50)
    tile_set = jeu.load_tiles("Tiles.png", 50, 50)

    run = True

    shift = (100, 100)

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
        
        mouse = pygame.mouse.get_pressed()
        pos = pygame.mouse.get_pos()

        if (mouse[0]):
            if (pos[0] >= 50 and pos[0] <= 100 and pos[1] >= 25 and pos[1] <= 75):
                selected = '0'
            elif (pos[0] >= 150 and pos[0] <= 200 and pos[1] >= 25 and pos[1] <= 75):
                selected = '1'
            elif (pos[0] >= 250 and pos[0] <= 300 and pos[1] >= 25 and pos[1] <= 75):
                selected = '2'
            elif (pos[0] >= 350 and pos[0] <= 400 and pos[1] >= 25 and pos[1] <= 75):
                selected = '3'
            elif (pos[0] >= 0 and pos[0] <= 1920 and pos[1] >= 0 and pos[1] <= 100):
                selected = ''
        
        if pos[0] >= 1320 and pos[0] <= 1920 and pos[1] >= 0 and pos[1] <= 100:
            if mouse[0] and not jeu.check_map(map):
                file.truncate(0)
                file.write(to_string(map))
                file.close
                return False
            screen.blit(butt_set[1], (1320, 0))
        else:
            screen.blit(butt_set[0], (1320, 0))

        screen.blit(tile_set[0], (50, 25))
        screen.blit(tile_set[1], (150, 25))
        screen.blit(tile_set[2], (250, 25))
        screen.blit(tile_set[3], (350, 25))

        if selected == '0':
            screen.blit(select_set[0], (50, 25))
        if selected == '1':
            screen.blit(select_set[1], (150, 25))
        if selected == '2':
            screen.blit(select_set[2], (250, 25))
        if selected == '3':
            screen.blit(select_set[3], (350, 25))

        if selected != '':
            if mouse[0] and pos[0] >= 100  and pos[1] >= 100 and pos[0] <= 100 + map_size[0] * 50 and pos[1] <= 100 + map_size[1] * 50:
                map[int((pos[1] - 100) / 50)][int((pos[0] - 100) / 50)] = selected

        jeu.draw_map(screen, tile_set, map, (100, 100))

        pygame.display.flip()
    return False