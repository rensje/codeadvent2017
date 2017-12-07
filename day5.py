instructions = [int(x) for x in open("instructions.txt").readlines()]

next = instructions[0]
steps = 0
while(next < len(instructions)):
    if instructions[next] >= 3:
        change = -1
    else:
        change = 1
    instructions[next] += change
    next = instructions[next] + (-1*change) + next
    steps+=1
steps += 1

print(steps)

