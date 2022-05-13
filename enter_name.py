import pygame
import pygame.locals
import jeu
import menu
from sqlalchemy import *
from sqlalchemy.orm import sessionmaker

def size_select():
    ## Initialisation de la connection à notre BDD
    engine = create_engine("sqlite:///amazeing.db")
    Session = sessionmaker()
    Session.configure(bind=engine)
    session = Session()

    ## Initialisation des modules Pygame
    pygame.init()
    pygame.font.init()
    
    ## Création d'un écran que l'on remplie en blanc
    screen = pygame.display.set_mode((1920, 1080))
    screen.fill((255, 255, 255))

    ## Création de la police d'écriture des divers textes
    my_font = pygame.font.SysFont('arial', 70)

    ## Création d'un texte 
    rules = my_font.render("Qui êtes-vous?", False, (255, 255, 255))

    ## Variable lié à l'entrée utilisateur
    input_selected = False
    input_tile = jeu.load_tiles("sprites/Input_Space.png", 300, 100)
    input_text = ""
    input_surface = my_font.render(input_text, False, (0, 0, 0))

    ## Load des sprites utiles à cet écran
    menu_font = jeu.load_tiles("sprites/Menu.jpg", 1920, 1080)
    butt_play = jeu.load_tiles("sprites/Boutton_Jouer.jpg", 600, 100)

    ## Variables lié à la souris
    mouse = None
    pos = (0, 0)

    ## Booléen gérant la boucle principale de l'écran
    run = True

    while run:

        ## Boucle détectant les différents events Pygame
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.KEYDOWN:
                if input_selected:
                    if event.key == pygame.K_BACKSPACE:
                        input_text = input_text[:-1]
                    elif event.key == pygame.K_RETURN:
                        if input_text != "":
                            run = menu.menu(screen, session, input_text)
                    else:
                        input_text += event.unicode
                input_surface = my_font.render(input_text, False, (0, 0, 0))
        
        mouse = pygame.mouse.get_pressed()
        pos = pygame.mouse.get_pos()

        if (mouse[0]):
            if (pos[0] >= 890 and pos[0] <= 1190 and pos[1] >= 500 and pos[1] <= 600):
                input_selected = True
            else:
                input_selected = False

        screen.blit(menu_font[0], (0, 0))

        if pos[0] >= 740 and pos[0] <= 1340 and pos[1] >= 930 and pos[1] <= 1030:
            if mouse[0] and input_text != "":
                run = menu.menu(screen, session, input_text)
            screen.blit(butt_play[1], (740, 930))
        else:
            screen.blit(butt_play[0], (740, 930))

        if (input_selected):
            screen.blit(input_tile[1], (890, 500))
        else:
            screen.blit(input_tile[0], (890, 500))
        
        screen.blit(input_surface, (900, 510))

        screen.blit(rules, (800, 400))
        if run:
            pygame.display.flip()

size_select()