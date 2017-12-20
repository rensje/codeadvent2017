from aocd import data
import re
import numpy as np
from collections import defaultdict
from pydash import flatten

def to_int(iterable):
    for x in iterable:
        yield int(x)
def parse_data(data):
    particles = []
    for particle in data.splitlines():
        match = re.match(r".*<(.*)>.*<(.*)>.*<(.*)>.*", particle)
        particle = list(np.array(tuple(to_int(x.replace(" ","").split(",")))) for x in match.groups())
        particles.append(particle)
    return particles

particles = parse_data(data)
print(len(particles))
min_acc = min(enumerate(particles), key=lambda x: np.linalg.norm(x[1][2], 1))
print(min_acc)

#part 2
def remove_duplicate_pos(particles):
    d = defaultdict(list)
    for particle in particles:
        d[tuple(particle[0])].append(particle)

    return flatten(list(filter(lambda x: len(x)==1, d.values())))


def simulate(particles, times):
    leftover = remove_duplicate_pos(particles)
    for _ in range(times):
        for particle in leftover:
            particle[1] += particle[2]
            particle[0] += particle[1]
        leftover = remove_duplicate_pos(leftover)
    return leftover

print(len(simulate(particles,10000)))