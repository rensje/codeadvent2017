import re
from collections import namedtuple, defaultdict

Instruction = namedtuple("Instruction", ["register", "operation", "argument", "register2", "condition", "condition_arg"])

def parse(instruction):
    match = re.match(r"(?P<register>[a-z]+) (?P<operation>(?:inc)|(?:dec)) (?P<argument>-?\d*) if (?P<register2>[a-z]+) (?P<condition>[^ ]+) (?P<condition_arg>-?\d*)", instruction)

    dic = match.groupdict()
    dic["argument"] = int(dic["argument"])
    dic["condition_arg"] = int(dic["condition_arg"])

    return Instruction(**dic)

instructions = []
with open("day8.txt") as f:
    for line in f:
        instructions.append(parse(line.rstrip()))

registers = defaultdict(lambda: 0)
highest = None
for instruction in instructions:
    condition = eval(f"{registers[instruction.register2]} {instruction.condition} {instruction.condition_arg}")
    if condition:
        if instruction.operation == "inc":
            registers[instruction.register] = registers[instruction.register] + instruction.argument
        elif instruction.operation =="dec":
            registers[instruction.register] = registers[instruction.register] - instruction.argument

        if highest is None or registers[instruction.register] > highest:
            highest = registers[instruction.register]

print(max(registers.items(), key=lambda kv: kv[1]))
print(highest)