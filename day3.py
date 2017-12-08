import itertools as it
from functools import reduce


def addTuple(x, y):
    return (x[0] + y[0], x[1] + y[1])

def repeat_from_iter(iterator, times):
    for el in iterator:
        yield from it.repeat(el, times)

def spiral_generator():
    moves = ((1,0), (0,1), (-1, 0), (0, -1))
    times = 1
    while(True):
        yield from repeat_from_iter(moves[0:2], times)
        times += 1
        yield from repeat_from_iter(moves[2:], times)
        times += 1

def spiral_steps(stop):
    yield from it.islice(spiral_generator(), stop)

def spiral_idx(element):
    return reduce(addTuple, spiral_steps(element-1), (0,0))

print(sum(abs(x) for x in spiral_idx(277678)))

def part2():
    grid = {(0,0): 1}
    pos = (0,0)
    gen = spiral_generator()
    neighbours = (-1, 0, 1)
    while(True):
        nextmove = next(gen)
        pos = (pos[0]+nextmove[0], pos[1]+nextmove[1])
        tally = 0
        for x in neighbours:
            for y in neighbours:
                tally += grid.get((pos, (x,y)), 0)
        grid[pos] = tally
        if(tally>277678):
            print(tally)
            break;

part2()