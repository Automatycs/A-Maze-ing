import pygame
import pygame.locals
import jeu
import size_select
import select_map

## Fonction contenant la boucle principale du menu
def menu(screen, session,  name="John Doe"):
    screen.fill((255, 255, 255))

    run = True

    mouse = None

    pos = (0, 0)

    menu_font = jeu.load_tiles("sprites/Menu.jpg", 1920, 1080)
    butt_quit = jeu.load_tiles("sprites/Boutton_Quitter.jpg", 600, 100)
    butt_play = jeu.load_tiles("sprites/Boutton_Jouer.jpg", 600, 100)
    butt_create = jeu.load_tiles("sprites/Boutton_Créer.jpg", 600, 100)

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        pos = pygame.mouse.get_pos()

        screen.blit(menu_font[0], (0, 0))

        mouse = pygame.mouse.get_pressed()
        if pos[0] >= 740 and pos[1] >= 350 and pos[0] <= 1340 and pos[1] <= 450:
            if mouse[0]:
                select_map.select_map(screen)
                run = jeu.game(screen, "./maps/abc.txt")
            screen.blit(butt_play[1], (740, 350))
        else:
            screen.blit(butt_play[0], (740, 350))
        if pos[0] >= 740 and pos[1] >= 550 and pos[0] <= 1340 and pos[1] <= 650:
            if mouse[0]:
                run = select_map.select_map_edit(screen, session, name)
            screen.blit(butt_create[1], (740, 550))
        else:
            screen.blit(butt_create[0], (740, 550))
        if pos[0] >= 740 and pos[1] >= 750 and pos[0] <= 1340 and pos[1] <= 850:
            if mouse[0]:
                return False
            screen.blit(butt_quit[1], (740, 750))
        else:
            screen.blit(butt_quit[0], (740, 750))

        if (run):
            pygame.display.flip()

