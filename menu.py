import pygame
import pygame.locals
import jeu
import my_size_select

if __name__=='__main__':
    pygame.init()
    pygame.font.init()
    
    screen = pygame.display.set_mode((1920, 1080))
    screen.fill((255, 255, 255))

    run = True

    mouse = None

    pos = (0, 0)

    menu_font = jeu.load_tiles("Menu.jpg", 1920, 1080)
    butt_quit = jeu.load_tiles("Boutton_Quitter.jpg", 600, 100)
    butt_play = jeu.load_tiles("Boutton_Jouer.jpg", 600, 100)
    butt_create = jeu.load_tiles("Boutton_Créer.jpg", 600, 100)

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        pos = pygame.mouse.get_pos()

        screen.blit(menu_font[0], (0, 0))

        mouse = pygame.mouse.get_pressed()
        if pos[0] >= 740 and pos[1] >= 350 and pos[0] <= 1340 and pos[1] <= 450:
            if mouse[0]:
                run = jeu.game(screen)
            screen.blit(butt_play[1], (740, 350))
        else:
            screen.blit(butt_play[0], (740, 350))
        if pos[0] >= 740 and pos[1] >= 550 and pos[0] <= 1340 and pos[1] <= 650:
            if mouse[0]:
                run = my_size_select.size_select(screen)
            screen.blit(butt_create[1], (740, 550))
        else:
            screen.blit(butt_create[0], (740, 550))
        if pos[0] >= 740 and pos[1] >= 750 and pos[0] <= 1340 and pos[1] <= 850:
            if mouse[0]:
                run = False
            screen.blit(butt_quit[1], (740, 750))
        else:
            screen.blit(butt_quit[0], (740, 750))

        if (run):
            pygame.display.flip()

