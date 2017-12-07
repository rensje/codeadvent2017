import numpy as np

def redistribute(banks):
    max_idx = np.argmax(banks)
    max_val = banks[max_idx]
    banks = list(banks)
    banks[max_idx] = 0
    while(max_val != 0):
        max_idx = (max_idx + 1) % len(banks)
        max_val -= 1
        banks[max_idx] += 1
    return tuple(banks)


seen = set()
current = tuple(int(x) for x in "2	8	8	5	4	2	3	1	5	5	1	2	15	13	5	14".split('\t'))
counter = 0

while(current not in seen):
    seen.add(current)
    current = redistribute(current)
    counter += 1


print(counter)

last = current
current = redistribute(current)
counter = 1

while(current != last):
    current = redistribute(current)
    counter += 1

print(counter)


