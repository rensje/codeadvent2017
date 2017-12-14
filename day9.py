from aocd import data
from lark import Lark
print(data)

def remove_ignore(data):
    chars = []
    ignore = False
    for char in data:
        if ignore:
            ignore=False
            continue
        if char=="!":
            ignore=True
        else:
            chars.append(char)
    return "".join(chars)

removed = remove_ignore(data)
grammar = open("grammar.txt").read()

tree = Lark(grammar, start='group').parse(removed)

def calculate_groups(tree, level):
    tally = 0
    for subtree in tree.children:
        if subtree.data == "group":
            tally += calculate_groups(subtree, level+1)
    return tally+level

print(calculate_groups(tree, 1))

def calculate_garbage(tree):
    tally = 0
    for subtree in tree.children:
        if subtree.data == "group":
            tally += calculate_garbage(subtree)
        if subtree.data == "garbage" and len(subtree.children)!=0:
            tally += len(subtree.children[0])
    return tally

print(calculate_garbage(tree))