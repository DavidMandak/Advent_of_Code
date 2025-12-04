import time

schematics = open("2024/Inputs/input25.txt").read().split("\n\n")

def read(sch, char):
    heights = [5]*5
    for x in range(5):
        for y in range(1, 6):
            if sch[y][x] != char:
                heights[x] = y-1
                break
    return heights


t = time.time()
total = 0
keys = []
locks = []
for schematic in schematics:
    if schematic[0] == "#":
        locks.append(read(schematic.splitlines(), "#"))
    else:
        keys.append(read(schematic.splitlines(), "."))

for lock in locks:
    for key in keys:
        for i in range(5):
            if lock[i] > key[i]:
                total -= 1
                break
        total += 1
print(total)
print(time.time()-t)
