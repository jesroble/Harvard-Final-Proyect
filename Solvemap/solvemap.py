import random
import pygame
import sys
from colorama import Fore, init

from Solvemap.maps import maps
from Solvemap.check import check_map
from Solvemap.solve_text import messages
from Solvemap.sources import init_sprites, init_pos, handle_input, draw_game
from Solvemap.enemies import move_enemies

init()

def get_map(lan): #select the map

    level = input(messages[lan]["choose_level"])
    while level not in maps:
        level = input(messages[lan]["wrong_level"])
    return maps[level]

def setup_screen(game_map, tile_size):

    width = len(game_map[0]) * tile_size
    height = len(game_map) * tile_size
    screen = pygame.display.set_mode((width, height), pygame.RESIZABLE)
    pygame.display.set_caption("Solve Map")
    return screen

def solvemap(lan):
    tile_size = 48
    game_map = get_map(lan)
    pygame.init()
    pos = init_pos(game_map)
    if not check_map(lan, game_map, pos):
        pygame.quit()
        sys.exit()
    screen = setup_screen(game_map, tile_size)
    sprites = init_sprites(lan)
    
    clock = pygame.time.Clock()
    running = True
    gate_open = False
    enemies_moveset = 1
    i = 0

    while running:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        dx, dy = handle_input()
        new_x, new_y = pos["player"]

        if dx != 0 or dy != 0:
            new_x = pos["player"][0] + dx
            new_y = pos["player"][1] + dy

            if 0 <= new_x < len(game_map[0]) and 0 <= new_y < len(game_map):
                if game_map[new_y][new_x] != 'W':
                    temp = pos["player"]
                    pos["player"] = [new_x, new_y]

                    if [new_x, new_y] in pos["enemies"]:
                        print(messages[lan]["enemy"])
                        pygame.quit()
                        sys.exit()
                    if [new_x, new_y] in pos["coin"]:
                        pos["coin"].remove([new_x, new_y])
                    if pos["lever"] == [new_x, new_y]:
                        gate_open = True
                    if [new_x, new_y] in pos["gate"] and not gate_open:
                        pos["player"] = temp
                    if pos["exit"] == [new_x, new_y]:
                        if len(pos["coin"]) == 0:
                            print(messages[lan]["win"])
                            running = False
                        else:
                            print(messages[lan]["pick_coins"])
                            pos["player"] = temp

                pos["enemies"] = move_enemies(game_map, pos["enemies"])
            pygame.time.delay(100)

        draw_game(game_map, tile_size, screen, sprites, gate_open, pos["coin"], pos["player"], pos["enemies"])
    pygame.quit()
    sys.exit()

            