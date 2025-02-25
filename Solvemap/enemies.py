import random

def is_valid(game_map, x, y):

    rows = len(game_map)
    col = len(game_map[0])

    if 0 <= x < col and 0 <= y < rows and game_map[y][x] == ' ':
        return True
    else: 
        return False

def move_in_map(game_map, pattern):

    new_pos = []
    for enemy in pattern:
        cx, cy = enemy["pos"]
        dx, dy = enemy["pattern"]
        nx, ny = cx + dx, cy + dy #move each enemy to its new position
        if is_valid(game_map, nx, ny): #check if it is a valid position
            new_pos.append([nx, ny])
        else:
            alternatives = [] #if not, creates a list of alternatives
            for adx, ady in [(1, 0), (-1, 0), (0, 1), (0, -1)]: 
                ax, ay = adx + cx, ady + cy
                if is_valid(game_map, ax, ay): 
                    alternatives.append([ax, ay])
            if alternatives: #if any alternative is valid, randomize one
                ax, ay = random.choice(alternatives)
                new_pos.append([ax, ay])
            else:
                new_pos.append([cx, cy]) #if not, then the enemy is trapped and doesn't move
    return new_pos



def move_enemies(game_map, enemies):
    patterns = []

    #create a pattern for every enemy
    if len(enemies) > 0 and enemies[0] is not None:
        patterns.append({"pos": enemies[0], "pattern": (1, 0)})
    if len(enemies) > 1 and enemies[1] is not None:
        patterns.append({"pos": enemies[1], "pattern": (-1, 0)})
    if len(enemies) > 2 and enemies[2] is not None:
        patterns.append({"pos": enemies[2], "pattern": (0, 1)})
    if len(enemies) > 3 and enemies[3] is not None:
        patterns.append({"pos": enemies[3], "pattern": (1, -1)})
    return move_in_map(game_map, patterns)
