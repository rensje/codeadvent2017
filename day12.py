from aocd import data
import re
from collections import defaultdict

adjacency = defaultdict(list)

for line in data.split("\n"):
    match = re.match(r"(\d+) <-> ((?:\d*(?:, )?)*)", line)
    a = match.group(1)
    bs = match.group(2).replace(" ", "").split(",")

    for b in bs:
        adjacency[a].append(b)
        adjacency[b].append(a)

seen = set()
def find_connected(id):
    seen.add(id)
    for adjacent in adjacency[id]:
        if adjacent not in seen:
            find_connected(adjacent)

find_connected("0")
print(len(seen))

count = 1
for id in adjacency.keys():
    if id not in seen:
        find_connected(id)
        count += 1

print(count)