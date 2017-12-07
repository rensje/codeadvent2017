import itertools as it
rows = []
with open("spreadsheet.txt") as f:
    for line in f:
        rows.append(tuple(int(x) for x in line.split('\t')))

checksum = 0
for row in rows:
    checksum += max(row)-min(row)

print(checksum)

checksum = 0
for row in rows:
    for cb in it.permutations(row, 2):
        if (cb[0] % cb[1]) == 0:
            checksum += cb[0]/cb[1]

print(checksum)
