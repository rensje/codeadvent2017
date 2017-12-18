from aocd import data
from functools import reduce

def knot_hash(data):
    lengths = [int.from_bytes(bytes(x, encoding="ascii"), byteorder="little") for x in data] + [17, 31, 73, 47, 23]
    lst = list(range(0,256))
    lstlen = len(lst)
    pos = 0
    skip = 0
    for _ in range(0,64):
        for length in lengths:
            if pos+length>lstlen:
                reverse=list(reversed(lst[pos:]+lst[0: (pos+length)%(lstlen)]))
                lst[pos:]=reverse[0:lstlen-pos] # reverse first part
                lst[0: (pos+length)%(lstlen)] = reverse[lstlen-pos:]

                # lst.reverse()
                # lst[(pos+length)%lstlen: pos] = reversed(lst[(pos+length)%lstlen: pos])
            else:
                lst[pos:pos+length] = reversed(lst[pos:pos+length])
            pos = (pos+length+skip)%(lstlen)
            skip+=1

    densehash = [lst[i:i + 16] for i in range(0, len(lst), 16)]
    densehash = [reduce(lambda x,y: x ^ y, block) for  block in densehash]
    print("".join("{:02x}".format(x) for x in densehash))
    return densehash

data = [data+"-"+str(x) for x in range(0, 128)]
hashes = [knot_hash(d) for d in data ]
print(hashes)

def count_ones_in_byte(byte):
    return bin(byte).count("1")

square_count = sum(count_ones_in_byte(byte) for row in hashes for byte in row)

def construct_binary_matrix(hashes):
    rows = []
    for row in hashes:
        bitstring = "".join(x for x in ("{:08b}".format(byte) for byte in row))
        print(bitstring)
        rows.append([int(x) for x in bitstring])

    return rows

def find_group(bmat, seen, cell, rowi, coli):
    if cell==0 or (rowi, coli) in seen:
        return 0
    else:
        seen.add((rowi,coli))
        moves = ((0,1), (1, 0), (0, -1), (-1, 0))
        for move in moves:
            rowi2 = rowi+move[0]
            coli2 = coli + move[1]
            if 0<=rowi2<=127 and 0<=coli2<=127:
                find_group(bmat, seen, bmat[rowi2][coli2], rowi2, coli2)
        return 1


bmat = construct_binary_matrix(hashes)
seen = set()
groups_found = []
for rowi, row in enumerate(bmat):
    for coli, cell in enumerate(row):
        groups_found.append(find_group(bmat, seen, cell, rowi, coli))

print(sum(groups_found))
