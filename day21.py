from aocd import data
import numpy as np
import re
from pprint import pprint
from itertools import chain

def to_tuple(array):
    return tuple(tuple(x) for x in array)

grid = """.#.
..#
###"""

grid  = np.array([[char for char in row] for row in grid.splitlines()])
rules = data.splitlines()
rules = (re.split(r" => ", rule) for rule in rules)
rule_dict = {}

def rule_str_to_grid(rule):
    return tuple(tuple(x) for x in rule.split("/"))

for rule in rules:
    rule_dict[rule_str_to_grid(rule[0])] = np.array(rule_str_to_grid(rule[1]))

def rotations(grid):
    return (to_tuple(np.rot90(grid, k=x)) for x in range(1, 4))

def flips(grid):
    return (to_tuple(np.fliplr(grid)), to_tuple(np.flipud(grid)))

def distinct(iterator):
    seen = set()
    for x in iterator:
        if not (x in seen):
            seen.add(hash(x))
            yield x

def transformations(grid):
    rotflip = chain.from_iterable(flips(x) for x in rotations(grid))
    fliprot = chain.from_iterable(iter(rotations(x) for x in flips(grid)))
    return chain([to_tuple(grid)], rotations(grid), flips(grid), rotflip)

def rule_match(grid):
    for trans in distinct(transformations(grid)):
        match = rule_dict.get(trans, None)
        if match is not None:
            return match
    return None

for _ in range(18):
    divisor = grid.shape[0]/2 if grid.shape[0]%2==0 else grid.shape[0]/3
    if divisor!=1:
        splits = [np.vsplit(x, divisor) for x in np.hsplit(grid, divisor)]
    else:
        splits = [[grid]]

    hsplits = []
    for hsplit in splits:
        vsplits = []
        for vsplit in hsplit:
            vsplits.append(rule_match(vsplit))
        hsplits.append(np.concatenate(vsplits, 0))
    grid = np.concatenate(hsplits, 1)
    print(np.count_nonzero(grid == "#"))
print(grid)

print(np.count_nonzero(grid=="#"))

