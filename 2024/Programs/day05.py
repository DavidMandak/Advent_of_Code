from collections import defaultdict
lines = open("../Inputs/Advent_of_Code_05.txt").read().split("\n\n")

rules = defaultdict(list)
pairs = lines[0].splitlines()
updates = lines[1].splitlines()
for pair in pairs:
    a, b = map(int, pair.split("|"))
    rules[a].append(b)

total = 0
for update in updates:
    line = list(map(int, update.split(",")))
    check = [line[0]]
    good = True
    for i in range(1, len(line)):
        for x in rules[line[i]]:
            if x in line[:i]:
                good = False
        if good is False:
            break
    if good is True:
        total += line[len(line)//2]
print(total)


def f(line):
    for i in range(1, len(line)):
        for x in rules[line[i]]:
            if x in line[:i]:
                line.insert(line.index(x), line[i])
                line.pop(i+1)
                return False


total = 0
for update in updates:
    line = list(map(int, update.split(",")))
    k = 0
    while f(line) is False:
        k = 1
    total += k*line[len(line)//2]
print(total)
