import time

lines = open("2023/Inputs/input17.txt").read().splitlines()
lines1 = open("../test.txt").read().splitlines()

t = time.time()
values = []
huh = []
for y in range(0, len(lines)):
    values.append([])
    huh.append([])
    for x in range(0, len(lines[y])):
        values[y].append(None)
        huh[y].append(".")
next_check = [(0, 0, 0, 0, "R")]


def f(x, y, value, count, direction):
    global values, next_check, huh
    if 0 <= x < len(lines[0]) and 0 <= y < len(lines):
        pass
    else:
        return
    value += int(lines[y][x])
    if values[y][x] is None or value < values[y][x] or (value-5 < values[y][x] and (huh[y][x][0] != direction or huh[y][x][1] > count)):
        values[y][x] = value
        if direction == "R":
            huh[y][x] = ("R", count)
            if count < 3:
                next_check.append((x+1, y, value, count+1, "R"))
            next_check.append((x, y-1, value, 1, "U"))
            next_check.append((x, y+1, value, 1, "D"))
        elif direction == "L":
            huh[y][x] = ("L", count)
            if count < 3:
                next_check.append((x-1, y, value, count+1, "L"))
            next_check.append((x, y-1, value, 1, "U"))
            next_check.append((x, y+1, value, 1, "D"))
        elif direction == "U":
            huh[y][x] = ("U", count)
            if count < 3:
                next_check.append((x, y-1, value, count+1, "U"))
            next_check.append((x+1, y, value, 1, "R"))
            next_check.append((x-1, y, value, 1, "L"))
        else:
            huh[y][x] = ("D", count)
            if count < 3:
                next_check.append((x, y+1, value, count+1, "D"))
            next_check.append((x+1, y, value, 1, "R"))
            next_check.append((x-1, y, value, 1, "L"))


while len(next_check) > 0:
    to_check = next_check.copy()
    next_check = []
    for pos in to_check:
        f(pos[0], pos[1], pos[2], pos[3], pos[4])
print(values[-1][-1]-int(lines[0][0]))
x, y = (len(huh[-1])-1, len(huh)-1)

while (x, y) != (0, 0):
    if huh[y][x][0] == "R":
        huh[y][x] = ("#")
        x -= 1
    elif huh[y][x][0] == "L":
        huh[y][x] = ("#")
        x += 1
    elif huh[y][x][0] == "U":
        huh[y][x] = ("#")
        y += 1
    elif huh[y][x][0] == "D":
        huh[y][x] = ("#")
        y -= 1
for line in huh:
    for tile in line:
        print(tile[0], end="")
    print()
print()
print(values)
print(time.time()-t)
