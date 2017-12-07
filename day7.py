import re
from collections import defaultdict
class Tower:
    def __init__(self, name, weight, successors, towers):
        self.name = name
        self.weight = weight
        self._successors = successors
        self.towers = towers
        self._predecessor = None

    def __str__(self):
        return f"{self.name} {self.weight} {[self._successors]}"

    def __repr__(self):
        return self.__str__()

    def successors(self):
        yield from (self.towers[x] for x in self._successors)

    def set_predecessor(self, name):
        self._predecessor = name

    def get_combined_weight(self):
        return self.weight + sum(x.get_combined_weight() for x in self.successors())

    def predecessor(self):
        return self.towers.get(self._predecessor, None)

towers = {}
with open("towers.txt") as f:
    for line in f:
        match = re.match(r"(?P<name>[a-z]+) \((?P<weight>\d+)\)(?: -> (?P<successors>.*))?", line)
        name = match.group("name")
        weight = int(match.group("weight"))
        if match.group("successors") is not None:
            successors = frozenset(match.group("successors").replace(' ','').split(','))
        else:
            successors = frozenset()
        towers[name] = Tower(name, weight, successors, towers)

for tower in towers.values():
    for successor in tower.successors():
        successor.set_predecessor(tower.name)

start = list(towers.values())[0]
while(start.predecessor() != None):
    start = start.predecessor()

print(start)

def weight_okay(root):
    #If no successors then it must be balancing correctly
    if(len(list(root.successors())) == 0):
        return True
    #Check whether the successors are balancing correctly, if not then the problematic program must be in the tree rooted at that program.
    for successor in root.successors():
        okay = weight_okay(successor)
        # Test not whether it's value is truthy, but whether it is the actual boolean value True
        if not (okay is True):
            return okay

    #Check whether this program is the problem

    #Partition the successors according to their combined weight
    weights = defaultdict(set)
    for successor in root.successors():
        weights[successor.get_combined_weight()].add(successor)

    #Find the smallest partition, note if it is the wrong program then twrs length equals 1
    weight, twrs = min(weights.items(), key = lambda kv: len(kv[1]))

    #If we have more than 1 partition then the smallest must be wrong
    if len(weights.keys())>1:
        for x in weights.keys():
            if x!=weight:
                otherweight = x
        tower = next(enumerate(twrs))[1]
        return (tower, weight, otherweight, otherweight-weight, tower.weight, tower.weight+(otherweight-weight))

    return True

print(weight_okay(start))

