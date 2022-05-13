import pygame
import pygame.locals
from pymysql import NULL
import jeu
import map_editor
import models

## Fonction permettant de créer une map vierge à l'aide de dimensions données
## IN:
## text_height:     String contenant l'entrée utilisateur représentant la hauteur de la map
## text_width:      String contenant l'entrée utilisateur représentant la largeur de la map
##
## OUT:
## new_map:         map vierge crée par la fonction
def create_map(text_height, text_width):
    height = int(text_height)
    width = int(text_width)
    new_map = []
    txt = ""

    for x in range(width):
        for y in range(height):
            txt += "3"
        new_map.append(txt)
        txt = ""

    return(new_map)


## Fonction vérifiant que les données passées par l'utilisateur sont valides
## IN:
## height:          String contenant l'entrée utilisateur représentant la hauteur de la map
## width:           String contenant l'entrée utilisateur représentant la largeur de la map
##
## OUT:
## False:           les valeurs entrées ne sont pas valides
## True:            les valeurs entrées sont valides
def check_values(height, width):
    check_height = 0
    check_width = 0

    if not height.isdigit() or not width.isdigit():
        return False
    check_height = int(height)
    check_width = int(width)

    if check_height <= 1 or check_height > 35:
        return False
    
    if check_width <= 1 or check_width > 18:
        return False

    return True

## Fonction contenant la boucle de selection des dimensions de la map
## IN:
## screen:          écran sur lequel on affiche nos différentes images
##
## OUT:
## False:           il y'a eu une erreur, ou la fenêtre a été fermée
## True:            l'utilsateur a fini de créer sa map
def size_select(screen, session, creator):
    screen.fill((255, 255, 255))

    map = models.Map()
    map.map_creator = creator
    map.map_name = ""

    width_selected = False
    height_selected = False

    input_tile = jeu.load_tiles("sprites/Input_Space.png", 300, 100)

    my_font = pygame.font.SysFont('arial', 70)

    height_text = ""
    width_text = ""

    rules_height = my_font.render("Largeur (max 35)", False, (255, 255, 255))
    rules_width = my_font.render("Hauteur (max 18)", False, (255, 255, 255))
    height_surface = my_font.render(height_text, False, (0, 0, 0))
    width_surface = my_font.render(width_text, False, (0, 0, 0))

    run = True

    menu_font = jeu.load_tiles("sprites/Menu.jpg", 1920, 1080)
    butt_quit = jeu.load_tiles("sprites/Boutton_Quitter.jpg", 600, 100)
    butt_create = jeu.load_tiles("sprites/Boutton_Créer.jpg", 600, 100)

    mouse = None
    pos = (0, 0)

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.KEYDOWN:
                if height_selected:
                    if event.key == pygame.K_BACKSPACE:
                        height_text = height_text[:-1]
                    elif event.key == pygame.K_RETURN:
                        if height_text != "":
                            height_selected = False
                            width_selected = True
                    else:
                        height_text += event.unicode
                height_surface = my_font.render(height_text, False, (0, 0, 0))
                if width_selected:
                    if event.key == pygame.K_BACKSPACE:
                        width_text = width_text[:-1]
                    elif event.key == pygame.K_RETURN:
                        if width_text != "" and check_values(height_text, width_text):
                            map.map_layout = map_editor.to_string(create_map(height_text, width_text))
                            run = map_editor.map_editor(screen, session, map, True)
                    else:
                        width_text += event.unicode
                width_surface = my_font.render(width_text, False, (0, 0, 0))
        
        mouse = pygame.mouse.get_pressed()
        pos = pygame.mouse.get_pos()

        if (mouse[0]):
            if (pos[0] >= 890 and pos[0] <= 1190 and pos[1] >= 400 and pos[1] <= 500):
                height_selected = True
                width_selected = False
            elif (pos[0] >= 890 and pos[0] <= 1190 and pos[1] >= 600 and pos[1] <= 700):
                height_selected = False
                width_selected = True
            else:
                height_selected = False
                width_selected = False

        screen.blit(menu_font[0], (0, 0))

        if pos[0] >= 50 and pos[0] <= 650 and pos[1] >= 930 and pos[1] <= 1030:
            if mouse[0]:
                run = False
            screen.blit(butt_quit[1], (50, 930))
        else:
            screen.blit(butt_quit[0], (50, 930))
        if pos[0] >= 1270 and pos[0] <= 1870 and pos[1] >= 930 and pos[1] <= 1030:
            if mouse[0] and check_values(height_text, width_text):
                run = map_editor.map_editor(screen, session, create_map(height_text, width_text), (int(height_text), int(width_text)), creator)
            screen.blit(butt_create[1], (1270, 930))
        else:
            screen.blit(butt_create[0], (1270, 930))

        if (height_selected):
            screen.blit(input_tile[1], (890, 400))
        else:
            screen.blit(input_tile[0], (890, 400))
        if (width_selected):
            screen.blit(input_tile[1], (890, 600))
        else:
            screen.blit(input_tile[0], (890, 600))
        
        screen.blit(height_surface, (900, 410))
        screen.blit(width_surface, (900, 610))

        screen.blit(rules_height, (900, 330))
        screen.blit(rules_width, (900, 530))
        
        pygame.display.flip()
    return True