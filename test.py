from re import X
from nbformat import read
import pygame
import pygame.locals

def load_tiles(filename, width: int, height: int):
    image = pygame.image.load(filename).convert()
    image_width, = image.get_size()
    tile_table = []
    for tile_x in range(0, int(image_width/width)):
        rect = (tile_x*width, 0, width, height)
        tile_table.append(image.subsurface(rect))
    return tile_table

def draw_map(screen, tile_table, map):
    for x, row in enumerate(map):
        for y in enumerate(row):
            if int(y[1]) == 0:
                player_pos = [y[0]*100, x*100]
            screen.blit(tile_table[int(y[1])], (y[0]*100, x*100))
    return player_pos


if __name__=='__main__':
    pygame.init()
    map = open("map.txt", 'r').read().split('\n')
    screen = pygame.display.set_mode((1600, 1000))
    screen.fill((255, 255, 255))
    map_table = load_tiles("Tiles.png", 100, 100)
    player_table = load_tiles("Perso.png", 100, 100)
    player_pos = draw_map(screen, map_table, map)
    last_moved = pygame.time.get_ticks()
    screen.blit(player_table[0], player_pos)
    pygame.display.flip()
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                print(pygame.key.name(event.key))
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

        draw_map(screen, map_table, map)
        screen.blit(player_table[0], player_pos)

        pygame.display.flip()