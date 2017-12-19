
import time

cdef void spin(programs, int arg):
    cdef int end = 16
    cdef int begin = end - arg

    group = programs[begin: end]
    group2 = programs[0:begin]
    programs[:] = group+group2


cdef void exchange(programs, int index1, int index2):
    cdef str program1= programs[index1]
    cdef str program2 = programs[index2]
    programs[index1] = program2
    programs[index2] = program1

cdef void partner(programs, str program1, str program2):
    cdef int index1 = programs.index(program1)
    cdef int index2 = programs.index(program2)

    programs[index1] = program2
    programs[index2] = program1

def start(programs, data):
    #programs = [ord(x) for x in programs]
    commands = []
    for command in data:
        argument = command[1:]
        method = command[0]
        if method=="s":
            argument = int(argument)
            commands.append((spin, argument))
            #programs = spin(programs, argument)
        elif method=="x":
            parsed = argument.split("/")
            index1 = int(parsed[0])
            index2 = int(parsed[1])
            commands.append((exchange, index1, index2))
            #exchange(programs, argument)
        elif method=="p":
            program1 = argument[0]
            program2 = argument[2]
            commands.append((partner, program1, program2))

    initial = tuple(programs)
    time_begin = time.time()
    hashes = dict()
    cdef int x
    for x in range(34):
        for command in commands:
            command[0](programs, *command[1:])

        if tuple(programs) == initial:
            with open("repeat.txt", "w") as f:
                f.write(str(x))
            print(x)
        if x%1000==0:
            print(((time.time()-time_begin)*1000000000)/(x+1))

    print("".join(programs))