from aocd import data
import numpy as np

matrix = []
for row in data.splitlines():
    matrix.append(list(row))

def traverse(matrix):
    encounters = []
    pos = np.array((0, matrix[0].index("|"))) #coord-system (y,x), top (0) to bottom, left(0) to right
    direction = np.array((1,0))
    count = 0
    while(True):
        count += 1
        pos = pos+direction
        char = matrix[pos[0]][pos[1]]
        if char == "+":
            moves = {(0, 1), (-1, 0), (0, -1), (1, 0)}
            moves -= {tuple(-1*direction)} # do not go back in the same direction
            for move in moves:
                newpos = pos+np.array(move)
                if 0<=newpos[0]<len(matrix) and 0<=newpos[1]<len(matrix[pos[0]]):
                    if matrix[newpos[0]][newpos[1]]!=" ":
                        direction = np.array(move)
                        break
        elif char in ("|", "-"):
            pass

        elif char == " ":
            break

        else:
            encounters.append(char)

    return (encounters, count)

encounters, count = traverse(matrix)
print("".join(encounters), count)
