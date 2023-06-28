import random as r
import msvcrt
import os

WIDTH = 10
HEIGHT = 5

# -----------------------------------------------------------------------------

def init(width=WIDTH, height=HEIGHT):
    positions = []

    # Generate 3 unique random positions for P, D, K
    while len(positions) < 3:
        x = r.randint(0, width-1)
        y = r.randint(0, height-1)

        if [x, y] not in positions:
            positions.append([x, y])

    # assign position (x,y) for P, D, K
    player = positions[0]
    key = positions[1]
    door = positions[2]

    # create map
    game_map = [ ['-' for _ in range(width)] for __ in range(height) ]
    game_map[   key[1]][   key[0]] = 'K'
    game_map[  door[1]][  door[0]] = 'D'
    game_map[player[1]][player[0]] = 'P'

    return game_map, player

def print_map(game_map, width=WIDTH, height=HEIGHT, instruction=True):
    os.system('cls')
    for y in range(height):
        for x in range(width):
            print(game_map[y][x], end=' ')
        print()
    
    if instruction == True:
        print("== THE ESCAPE GAME ==")
        print("Use W A S D to move (P)layer.")
        print("Find (K)ey first then exit through the (D)oor.")

def is_valid_move(game_map, x, y, status, width=WIDTH, height=HEIGHT):
    if x < 0 or x > width-1 or y < 0 or y > height-1:
        return False
    if game_map[y][x] == 'D' and status == 0:
        return False
    return True

def move_player(game_map, player, cmd, status):
    x = px = player[0]
    y = py = player[1]

    if cmd == 'w':
        y = y - 1
    elif cmd == 's':
        y = y + 1
    elif cmd == 'a':
        x = x - 1
    elif cmd == 'd':
        x = x + 1
    
    collected_obj = None
    if is_valid_move(game_map, x, y, status) == True:
        collected_obj = game_map[y][x]
        if game_map[y][x] == '-':
            game_map[y][x], game_map[py][px] = game_map[py][px], game_map[y][x]
        else:            
            game_map[y][x] = 'P'
            game_map[py][px] = '-'
        player[0] = x
        player[1] = y

    return collected_obj


# driver code -----------------------------------------------------------------
game_map, player = init()
status = 0  # status = 0: need to find K
            # status = 1: found K, finding D
            # status = 2: found D. Won the game

while status < 2:
    print_map(game_map)

    cmd = msvcrt.getch().decode('utf-8')
    if cmd == 'q':
        break
    
    collected_obj = move_player(game_map, player, cmd, status)
    if collected_obj == 'K':
        status = 1
    elif collected_obj == 'D' and status == 1:
        status = 2

if status == 2:
    print_map(game_map, instruction=False)
    print("You won the game!")
else:
    print("Good bye.")
