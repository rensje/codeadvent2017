valid = 0
with open("passwords.txt") as f:
    for line in f:
        words = tuple(frozenset(x) for x in line.rstrip().split(' '))
        if len(set(words)) == len(words):
            valid+=1
print(valid)

