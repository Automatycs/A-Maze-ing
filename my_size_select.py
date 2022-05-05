from tabnanny import check
import pygame
import pygame.locals
import jeu

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

def size_select(screen):
    screen.fill((255, 255, 255))

    width_selected = False
    height_selected = False

    input_tile = jeu.load_tiles("Input_Space.png", 300, 100)

    my_font = pygame.font.SysFont('arial', 70)

    height_text = ""
    width_text = ""

    rules_height = my_font.render("Hauteur (max 35)", False, (255, 255, 255))
    rules_width = my_font.render("Largeur (max 18)", False, (255 ,255, 255))
    height_surface = my_font.render(height_text, False, (0, 0, 0))
    width_surface = my_font.render(width_text, False, (0, 0, 0))

    run = True

    menu_font = jeu.load_tiles("Menu.jpg", 1920, 1080)
    butt_quit = jeu.load_tiles("Boutton_Quitter.jpg", 600, 100)
    butt_create = jeu.load_tiles("Boutton_Créer.jpg", 600, 100)

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
                    else:
                        height_text += event.unicode
                height_surface = my_font.render(height_text, False, (0, 0, 0))
                if width_selected:
                    if event.key == pygame.K_BACKSPACE:
                        width_text = width_text[:-1]
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
                print("SBOUER")
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
        
        pygame.display.flip()
    return True