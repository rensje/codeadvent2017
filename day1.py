import itertools as it
import functools as ft

with open('digits.txt') as f:
    digits = f.readline().rstrip()

digits = digits + digits[0]
sum = 0
for x in range(len(digits)-1):
    if digits[x]==digits[x+1]: sum+=int(digits[x])

print(sum)

digits1 = digits[0:len(digits)//2]
digits2 = digits[len(digits)//2:]

sum = 0
for digit in zip(digits1, digits2):
    if digit[0]==digit[1]: sum+=2*int(digit[0])

print(sum)