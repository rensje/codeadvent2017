from aocd import data
import numpy as np
def move_to_coord(move):
    if move=="n":
        return ( 0, +1, -1)

    elif move=="ne":
        return (+1,  0, -1)

    elif move=="se":
        return (+1, -1,  0)

    elif move=="s":
        return ( 0, -1, +1)

    elif move=="sw":
        return (-1,  0, +1)

    elif move=="nw":
        return (-1, +1,  0)

def grid_gen():
    cur_coord = np.array((0,0,0))
    while True:
        move=(yield cur_coord)
        move = move_to_coord(move)
        cur_coord = np.array(move) + cur_coord

def do_moves(moves):
    gen = grid_gen()
    gen.send(None)
    for move in moves:
        yield gen.send(move)



moves =data.split(",")
coords = list(do_moves(moves))
last_coord = coords[-1]
print(np.linalg.norm(last_coord, 1.0)/2)

print(max(np.linalg.norm(x, 1.0)/2 for x in coords))
