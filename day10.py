from aocd import data
from functools import reduce

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
        else:
            lst[pos:pos+length] = reversed(lst[pos:pos+length])
        pos = (pos+length+skip)%(lstlen)
        skip+=1

densehash = [lst[i:i + 16] for i in range(0, len(lst), 16)]
densehash = [reduce(lambda x,y: x ^ y, block) for  block in densehash]
print("".join("{:02x}".format(x) for x in densehash))