import sys, copy
lines = open("../Inputs/Advent_of_Code_20.txt").read()
sys.setrecursionlimit(10**6)

start_i = lines.index("S")
end_i = lines.index("E")
lines = lines.replace("S", ".")
lines = lines.replace("E", ".")
lines = list(map(list, lines.splitlines()))
start = (start_i % (len(lines[0])+1), start_i//(len(lines[0])+1))
end = (end_i % (len(lines[0])+1), end_i//(len(lines[0])+1))


def memoization(pos, parent, score):
    global memo
    memo[pos[1]][pos[0]] = score
    if pos == end:
        return
    dx, dy = 1, 0
    for _ in range(4):
        x, y = pos[0]+dx, pos[1]+dy
        if (x, y) != parent and lines[y][x] != "#":
            memoization((x, y), pos, score+1)
            return
        temp = dy
        dy = -1*dx
        dx = temp


def move(pos, parent, score):
    if pos == end:
        return
    dx, dy = 1, 0
    for _ in range(4):
        x, y = pos[0] + dx, pos[1] + dy
        if lines[y][x] == "#":
            cheat_2ps((x, y), pos, score+1)
        elif (x, y) != parent:
            move((x, y), pos, score+1)
        temp = dy
        dy = -1*dx
        dx = temp


def cheat_2ps(pos, parent, score):
    global total
    dx, dy = 1,0
    for _ in range(4):
        x, y = pos[0]+dx, pos[1]+dy
        if 0 <= x < len(lines[0]) and 0 <= y < len(lines) and (x, y) != parent and lines[y][x] != "#" and\
                memo[y][x]-(score+1) >= 100:
            total += 1
        temp = dy
        dy = -1*dx
        dx = temp


def cheat_20ps(px, py):
    global total
    parent = memo[py][px]
    for size in range(1, 21):
        kx, ky = 1, 1
        for _ in range(4):
            for dx in range((kx+1)//2, size+(ky+1)//2):
                x, y = px+kx*dx, py+ky*(size-dx)
                if 0 <= x < len(lines[0]) and 0 <= y < len(lines) and lines[y][x] == "." and\
                        memo[y][x]-(parent+size) >= 100:
                    total += 1
            temp = ky
            ky = -1*kx
            kx = temp


total = 0
memo = copy.deepcopy(lines)
memoization(start, (-1, -1), 0)
move(start, (-1, -1), 0)
print(total)
total = 0
for y in range(len(lines)):
    for x in range(len(lines[y])):
        if lines[y][x] == ".":
            cheat_20ps(x, y)
print(total)
