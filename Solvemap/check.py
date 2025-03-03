import pygame
import sys
from colorama import Fore, init

from Solvemap.solve_text import messages

init()

def check_limits(lan, game_map):

    for char in game_map[0]:
        if char != "W":
            print(messages[lan]["column"])
            return False
    for char in game_map[-1]:
        if char != "W":
            print(messages[lan]["column"])
            return False
    for row in game_map:
        if row[0] != "W" or row[-1] != "W":
            print(messages[lan]["row"])
            return False
    return True


def check_size(lan, game_map):

    expected_length = len(game_map[0])

    for i, row in enumerate(game_map):
        if len(row) != expected_length:
            print(messages[lan]["error_length"])
            return False

    return True


def check_values(lan, game_map):
    
    p_count = 0
    c_count = 0
    e_count = 0
    en_count = 0

    for y, row in enumerate(game_map):
        for x, char in enumerate(row):
            if char == "P":
                p_count += 1
            if char == "C":
                c_count += 1
            if char == "E":
                e_count += 1
            if char == "e":
                en_count += 1

    if p_count != 1:
        print(messages[lan]["error_player"])
        return False
    if c_count < 1:
        print(messages[lan]["error_coin"])
        return False
    if e_count != 1:
        print(messages[lan]["error_exit"])
        return False
    if en_count > 4:
        print(messages[lan]["max_enemies"])
        return False
    
    return True


def solvable(game_map, x, y, coins, gate_open, visited):
    # limits
    if x < 0 or x >= len(game_map[0]) or y < 0 or y >= len(game_map):
        return False
    if game_map[y][x] == "W":
        return False
    # gate closed
    if game_map[y][x] == "G" and not gate_open:
        return False

    # exit whit coins left
    if game_map[y][x] == "E" and len(coins) != 0:
        return False

    # Creates a state for each branch and tuples the list of coins, avoiding
    # false negatives due to its immutable position
    state = (x, y, tuple(sorted(tuple(c) for c in coins)), gate_open)
    if state in visited:
        return False
    visited.add(state)

    # opens the gate
    new_gate_open = gate_open or (game_map[y][x] == "L")
    
    # copy coins and pick them
    new_coins = coins.copy()
    if game_map[y][x] == "C" and [x, y] in new_coins:
        new_coins.remove([x, y])
    
    # win if exits whit all coins picked
    if game_map[y][x] == "E" and len(new_coins) == 0:
        return True

    # recursively moves the player in 4 directions
    return (solvable(game_map, x + 1, y, new_coins, new_gate_open, visited) or
            solvable(game_map, x - 1, y, new_coins, new_gate_open, visited) or
            solvable(game_map, x, y + 1, new_coins, new_gate_open, visited) or
            solvable(game_map, x, y - 1, new_coins, new_gate_open, visited))


def check_map(lan, game_map, pos):

    if not check_limits(lan, game_map):
        return False
    if not check_size(lan, game_map):
        return False
    if not check_values(lan, game_map):
        return False
    
    x, y = pos["player"]
    coins = pos["coin"]
    visited = set()
    gate_open = False
    if not solvable(game_map, x, y, coins, gate_open, visited):
        print(messages[lan]["unsolvable"])
        return False
    
    return True
