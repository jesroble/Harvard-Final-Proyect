import pygame
import sys
from colorama import Fore, init

from Solvemap.maps import maps
from Solvemap.check import check_map
from Solvemap.solve_text import messages
from Solvemap.sources import init_sprites, init_pos, handle_input, draw_game

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

    tile_size = 64
    game_map = get_map(lan)
    check_map(lan, game_map)
    
    pygame.init()
    pos = init_pos(game_map)
    screen = setup_screen(game_map, tile_size)
    sprites = init_sprites(lan)     #load sprites into image
   
    #set clock and start running
    clock = pygame.time.Clock()
    running = True
    gate_open = False

    while running:
        clock.tick(60) #limit 60fps

        for event in pygame.event.get(): #control event
            if event.type == pygame.QUIT:
                running = False
    
        dx, dy = handle_input() #handle keyboard
        new_x, new_y = pos["player"]

        if dx != 0 or dy != 0:
            new_x = pos["player"][0] + dx
            new_y = pos["player"][1] + dy

        if 0 <= new_x < len(game_map[0]) and 0 <= new_y < len(game_map):
            if game_map[new_y][new_x] != 'W':
                temp = pos["player"]               #copy current position to go back if error
                pos["player"] = [new_x, new_y]

                if [new_x, new_y] in pos["coin"]:
                    pos["coin"].remove([new_x, new_y])

                if pos["lever"] == [new_x, new_y]:
                    gate_open = True        #open the gate

                if [new_x, new_y] in pos["gate"] and gate_open == False:
                    pos["player"] = temp       #restores the previous position if gate closed

                if pos["exit"] == [new_x, new_y]:
                    if len(pos["coin"]) == 0:
                        print(messages[lan]["win"])
                        running = False
                    else:
                        print(messages[lan]["cannot_exit"])
                        pos["player"] = temp       #restores the previous position if exit closed
            
            pygame.time.delay(100) 
        
        draw_game(game_map, tile_size, screen, sprites, gate_open,
                  pos["coin"], pos["player"])

    pygame.quit()
    sys.exit()
            