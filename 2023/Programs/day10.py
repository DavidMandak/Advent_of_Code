import time

lines = open("2023/Inputs/input10.txt").read().splitlines()
positions = [[114, 36], [115, 35]]
moves = ["R", "D"]
loop = [[114, 35], [114, 36], [115, 35]]


def left(i):
    global positions
    moves[i] = "L"
    positions[i][1] -= 1


def up(i):
    global positions
    moves[i] = "U"
    positions[i][0] -= 1


def right(i):
    global positions
    moves[i] = "R"
    positions[i][1] += 1


def down(i):
    global positions
    moves[i] = "D"
    positions[i][0] += 1


t = time.time()
steps = 1
while positions[0] != positions[1]:
    for i in range(0, 2):
        y, x = positions[i]
        move = moves[i]
        pipe = lines[y][x]
        if move == "L":
            if pipe == "-":
                left(i)
            elif pipe == "L":
                up(i)
            elif pipe == "F":
                down(i)
            else:
                exit((pipe, move))
        elif move == "U":
            if pipe == "|":
                up(i)
            elif pipe == "F":
                right(i)
            elif pipe == "7":
                left(i)
            else:
                exit((pipe, move))
        elif move == "R":
            if pipe == "-":
                right(i)
            elif pipe == "J":
                up(i)
            elif pipe == "7":
                down(i)
            else:
                exit((pipe, move))
        else:
            if pipe == "|":
                down(i)
            elif pipe == "L":
                right(i)
            elif pipe == "J":
                left(i)
            else:
                exit((pipe, move))
        loop.append([y, x])
    steps += 1
file = []
for y in range(0, len(lines)):
    file.append("")
    for x in range(0, len(lines[y])):
        if [y, x] in loop:
            file[-1] += (lines[y][x])
            if [y, x+1] in loop:
                if lines[y][x] == "-" or lines[y][x] == "L" or lines[y][x] == "F" or lines[y][x] == "p"\
                        and lines[y][x+1] == "-" or lines[y][x+1] == "7" or lines[y][x+1] == "J":
                    file[-1] += "-"
                else:
                    file[-1] += " "
            else:
                file[-1] += " "
        else:
            file[-1] += ". "
    file.append("")
    for x in range(0, len(lines[y])):
        if y+1 == len(lines):
            file[-1] += "  "
        elif [y, x] in loop and [y+1, x] in loop:
            if lines[y][x] == "|" or lines[y][x] == "7" or lines[y][x] == "F" or lines[y][x] == "p" and\
                    lines[y+1][x] == "|" or lines[y+1][x] == "L" or lines[y+1][x] == "J":
                file[-1] += "| "
            else:
                file[-1] += "  "
        else:
            file[-1] += "  "
lines_list = []
for line in file:
    lines_list.append([])
    for character in line:
        lines_list[-1].append(character)
lines_list[63][202] = "|"
lines_list[64][202] = "L"
lines_list[63][203] = "-"


def flood_fill(x, y):
    if y < 0 or y >= len(lines_list) or x < 0 or x >= len(lines_list[y]):
        return
    if lines_list[y][x] != " " and lines_list[y][x] != ".":
        return
    lines_list[y][x] = "#"
    to_check.append([x+1, y])
    to_check.append([x-1, y])
    to_check.append([x, y+1])
    to_check.append([x, y-1])


pos = []
to_check = [[0, 0]]
i = 0
while 0 < len(to_check):
    pos = to_check.copy()
    to_check = []
    for pos in pos:
        flood_fill(pos[0], pos[1])
    i += 1
total = 0
for line in lines_list:
    for character in line:
        if character == ".":
            total += 1
print(total)
print(time.time()-t)
