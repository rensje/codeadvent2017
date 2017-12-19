from aocd import data
import string
import re
import time
import pyximport; pyximport.install()
from fast import start

programs = [string.ascii_lowercase[x] for x in range(0, 16)]
data = [x for x in data.split(",")]

start(programs, data)



print("".join(programs))