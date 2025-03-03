import random

def is_valid(game_map, x, y):
    rows = len(game_map)
    col = len(game_map[0])
    return 0 <= x < col and 0 <= y < rows and (game_map[y][x] == ' ' or game_map[y][x] == 'C')


def get_alternative_moves(game_map, x, y, original_dx, original_dy):
    """ Devuelve una lista de movimientos alternativos en caso de bloqueo """
    moves = [(original_dx, original_dy),  # Intentar el movimiento original
             (0, -1),  # Arriba
             (0, 1),  # Abajo
             (-1, 0),  # Izquierda
             (1, 0)]  # Derecha

    valid_moves = [(dx, dy) for dx, dy in moves if is_valid(game_map, x + dx, y + dy)]
    
    return valid_moves if valid_moves else [(0, 0)]  # Si no hay movimiento válido, quedarse quieto


def move_enemies(game_map, enemies):

    movesets = [(1, 0), (-1, 0), (0, 1), (-1, 1)]
    new_positions = []
    new_movesets = []

    for i, enemy in enumerate(enemies):
        cx, cy = enemy
        dx, dy = movesets[i]  # Obtener patrón de movimiento del enemigo

        # Comprobar si la dirección es válida
        if is_valid(game_map, cx + dx, cy + dy):
            new_positions.append([cx + dx, cy + dy])
            new_movesets.append((dx, dy))  # Mantener el mismo patrón
        else:
            # Buscar una alternativa si el movimiento es inválido
            alternative_moves = get_alternative_moves(game_map, cx, cy, dx, dy)
            new_dx, new_dy = random.choice(alternative_moves)  # Seleccionar una alternativa válida
            new_positions.append([cx + new_dx, cy + new_dy])
            new_movesets.append((new_dx, new_dy))  # Actualizar el patrón de movimiento

    return new_positions

