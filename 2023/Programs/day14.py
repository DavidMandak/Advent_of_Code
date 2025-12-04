import time

lines = open("2023/Inputs/input14.txt").read().splitlines()
vertical_length = len(lines)
horizontal_length = len(lines[0])
totals = []
cycles = []
total = 0
east_total = 0


def north():
    for x in range(0, len(lines[0])):
        for y in range(0, len(lines)):
            if lines[y][x] == "O":
                lines[y] = lines[y][:x]+"."+lines[y][x+1:]
                i = y-1
                while i >= 0:
                    if lines[i][x] != ".":
                        lines[i+1] = lines[i+1][:x]+"O"+lines[i+1][x+1:]
                        break
                    i -= 1
                if i < 0:
                    lines[0] = lines[0][:x]+"O"+lines[0][x+1:]


def west():
    for y in range(0, len(lines)):
        for x in range(0, len(lines[y])):
            if lines[y][x] == "O":
                lines[y] = lines[y][:x]+"."+lines[y][x+1:]
                i = x-1
                while i >= 0:
                    if lines[y][i] != ".":
                        lines[y] = lines[y][:i+1]+"O"+lines[y][i+2:]
                        break
                    i -= 1
                if i < 0:
                    lines[y] = "O"+lines[y][1:]


def south():
    for x in range(0, len(lines[0])):
        for y in range(-len(lines)+1, 1):
            y *= -1
            if lines[y][x] == "O":
                lines[y] = lines[y][:x]+"."+lines[y][x+1:]
                i = y+1
                while i < len(lines):
                    if lines[i][x] != ".":
                        lines[i-1] = lines[i-1][:x] + "O" + lines[i-1][x+1:]
                        break
                    i += 1
                if i == len(lines):
                    lines[-1] = lines[-1][:x] + "O" + lines[-1][x+1:]


def east():
    global total, east_total
    for y in range(0, len(lines)):
        for x in range(-len(lines[y])+1, 1):
            x *= -1
            if lines[y][x] == "O":
                total += vertical_length - y
                lines[y] = lines[y][:x]+"."+lines[y][x+1:]
                i = x+1
                while i < len(lines[y]):
                    if lines[y][i] != ".":
                        lines[y] = lines[y][:i-1]+"O"+lines[y][i:]
                        east_total += horizontal_length - i
                        break
                    i += 1
                if i == len(lines[y]):
                    lines[y] = lines[y][:-1]+"O"
                    east_total += horizontal_length


t = time.time()
i = 1
while True:
    total = 0
    east_total = 0
    north()
    west()
    south()
    east()
    if (total, east_total) in totals:
        if lines == cycles[totals.index((total, east_total))]:
            break
    totals.append((total, east_total))
    cycles.append(lines.copy())
    i += 1
num = totals.index((total, east_total)) + 1
print(totals[num+((1000000000-num) % (i-num))-1][0])
print(time.time()-t)
