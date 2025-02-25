import pygame
import sys
import os
from colorama import Fore, init

from Solvemap.solve_text import messages
from Solvemap.maps import maps

init()

def init_pos(game_map):
    
    positions = {"player": None, "lever": None, 
                 "gate": [], "coin": [], "enemies": [], "exit": None}
    
    for y, row in enumerate(game_map):
        for x, char in enumerate(row):
            if char == 'P':
                positions["player"] = [x, y]
            elif char == 'G':
                positions["gate"].append([x, y])
            elif char == 'L':
                positions["lever"] = [x, y]
            elif char == 'C':
                positions["coin"].append([x, y])
            elif char == 'e':
                positions["enemies"].append([x, y])
            elif char == 'E':
                positions["exit"] = [x, y]
    return positions


def init_sprites(lan):

    base_path = os.path.dirname(os.path.abspath(__file__))
    img_path = os.path.join(base_path, "images") #convert images path in absolute path

    try:
        return {
        "player": pygame.image.load(os.path.join(img_path, "player.png")).convert_alpha(),
       # enemie_img = pygame.image.load("./images/enemie.png").convert_alpha()
        "wall": pygame.image.load(os.path.join(img_path, "wall.png")).convert_alpha(),
        "floor": pygame.image.load(os.path.join(img_path, "floor.png")).convert_alpha(),
        "coin": pygame.image.load(os.path.join(img_path, "coin.png")).convert_alpha(),
        "lever": pygame.image.load(os.path.join(img_path, "lever.png")).convert_alpha(),
        "gate": pygame.image.load(os.path.join(img_path, "gate.png")).convert_alpha(),
        "exit_open": pygame.image.load(os.path.join(img_path, "exit_open.png")).convert_alpha(),
        "exit_closed": pygame.image.load(os.path.join(img_path, "exit_closed.png")).convert_alpha(),
        }

    except pygame.error as what:
        print(messages[lan]["sprite_error"], what)
        sys.exit()

def handle_input():
    dx, dy = 0, 0
    
    keys = pygame.key.get_pressed()  # get access to keyboard
    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        return -1, 0
    elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        return 1, 0
    elif keys[pygame.K_UP] or keys[pygame.K_w]:
        return 0, -1
    elif keys[pygame.K_DOWN] or keys[pygame.K_s]:
        return 0, 1
    elif keys[pygame.K_ESCAPE]:  # press escape to exit
        pygame.quit()
        sys.exit()

    return dx, dy  


def draw_game(game_map, tile_size, screen, sprites, gate_open, coin, player_pos):

    screen.fill((0, 0, 0)) #fills the screen in black
    for y, row in enumerate(game_map): #fills the map with sprites
            for x, char in enumerate(row):

                pos = [x * tile_size, y * tile_size]
                if char == 'W':
                    screen.blit(sprites["wall"], pos)

                elif char == ' ':
                    screen.blit(sprites["floor"], pos)

                elif char == 'L':
                    screen.blit(sprites["lever"], pos)

                elif char == 'G':   #remove the gate when the lever is pressed
                    if gate_open == False:
                        screen.blit(sprites["gate"], pos)
                    else:
                        screen.blit(sprites["floor"], pos)

                elif char == 'C':   #remove coin when its taken and fills whit floor
                    if [x, y] in coin:
                        screen.blit(sprites["coin"], pos)
                    else:
                        screen.blit(sprites["floor"], pos)

                elif char == 'E':   
                    if len(coin) == 0:
                        screen.blit(sprites["exit_open"], pos) #exit open only if all coins are taken
                    else:
                        screen.blit(sprites["exit_closed"], pos)

    screen.blit(sprites["player"], (player_pos[0] * tile_size, player_pos[1] * tile_size))
    pygame.display.flip()