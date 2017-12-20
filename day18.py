from aocd import data
from collections import defaultdict
from queue import Queue
import threading


instructions = [x.strip().split(" ") for x in data.splitlines()]
print(instructions)
send_count = defaultdict(lambda: 0)

def run_program(id, send_queue, receive_queue):
    registers = defaultdict(lambda: 0)
    registers["p"] = id
    program_counter = 0
    last_sound = -1

    def read_val(arg):
        value = None
        try:
            value = int(arg)
        except ValueError:
            value = int(registers[arg])
        return value


    while 0<=program_counter<len(instructions):
        global send_count
        cur = instructions[program_counter]
        if (cur[0] == "snd"):
            send_queue.put(read_val(cur[1]))
            send_count[id]+=1
            program_counter+=1

        elif (cur[0] == "set"):
            registers[cur[1]] = read_val(cur[2])
            program_counter += 1

        elif (cur[0] == "add"):
            registers[cur[1]] += read_val(cur[2])
            program_counter += 1

        elif (cur[0] == "mul"):
            registers[cur[1]] *= read_val(cur[2])
            program_counter += 1

        elif cur[0] == "mod":
            registers[cur[1]] = registers[cur[1]] % read_val(cur[2])
            program_counter += 1

        elif cur[0] == "rcv":
            try:
                rcvd = receive_queue.get(timeout=20)
                registers[cur[1]] = rcvd
                program_counter+=1
            except:
                return -1

        elif cur[0] == "jgz":
            if read_val(cur[1])>0:
                program_counter += read_val(cur[2])
            else:
                program_counter += 1


    return 0

queue_1 = Queue()
queue_2 = Queue()
program1 = threading.Thread(target=run_program, args=(0, queue_2, queue_1))
program2 = threading.Thread(target=run_program, args=(1, queue_1, queue_2))

program1.start()
program2.start()
program1.join()
program2.join()
print(send_count[1])

