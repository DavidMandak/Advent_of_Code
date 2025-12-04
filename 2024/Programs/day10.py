import copy
lines = open("2024/Inputs/input10.txt").read().splitlines()


def trail(x, y):
    global total
    if save[y][x] == 9:
        total += 1
        save[y][x] += 1 #for the first of the puzzle leave this line in, for the second part delete it
    else:
        dx = 1
        dy = 0
        for _ in range(4):
            if 0 <= x+dx < len(save[0]) and 0 <= y+dy < len(save) and save[y + dy][x + dx] == save[y][x]+1:
                trail(x + dx, y + dy)
            temp = dy
            dy = -1*dx
            dx = temp


total = 0
for y in range(len(lines)):
    lines[y] = list(map(int, lines[y]))
for y in range(len(lines)):
    for x in range(len(lines[y])):
        if lines[y][x] == 0:
            save = copy.deepcopy(lines)
            trail(x, y)
print(total)
