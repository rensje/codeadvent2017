from aocd import data
import re


def gen(start, factor, multiple):
    remainder_arg = 2147483647
    number = (start*factor)%remainder_arg
    while(True):
        if (number%multiple==0):
            yield number
        number = (number*factor)%remainder_arg

data = data.splitlines()
data = tuple(int(re.search(r"\d+", x).group(0)) for x in data)

gena = gen(data[0], 16807, 1)
genb = gen(data[1], 48271, 1)
genab = zip(gena, genb)

def lowest_16_bits_equal(a, b):
    bit_mask = 0xFFFF
    return 1 if (a & bit_mask) == (b & bit_mask) else 0

equal = 0
for _ in range(0, 4*(10**7)):
    equal += lowest_16_bits_equal(*next(genab))

print(equal)

##part 2
gena = gen(data[0], 16807, 4)
genb = gen(data[1], 48271, 8)
genab = zip(gena, genb)

equal = 0
for _ in range(0, 5*(10**6)):
    equal += lowest_16_bits_equal(*next(genab))

print(equal)




