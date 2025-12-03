import sys, copy

sys.setrecursionlimit(10**6)
lines = list(map(list, open("../Inputs/Advent_of_Code_16.txt").read().splitlines()))
save = copy.deepcopy(lines)


def move(x, y, dx, dy, maze, score):
    global total
    maze[y][x] = score
    tile = maze[y+dy][x+dx]
    if tile == "E":
        if total is None or score+1 < total:
            total = score+1
    elif tile == "." or (isinstance(tile, int) and score+1 < tile):
        move(x+dx, y+dy, dx, dy, maze, score+1)
    for k in [1, -1]:
        kx, ky = k*dy, k*dx
        if maze[y+ky][x+kx] == "." or (isinstance(maze[y+ky][x+kx], int) and score+1001 < maze[y+ky][x+kx]):
            move(x+kx, y+ky, kx, ky,  maze, score+1001)



total = None
move(1, len(lines)-2, 1, 0, lines, 0)
print(total)


def step(x, y, dx, dy, maze, score, path):
    global total, roads
    path += str(x)+" "+str(y)+","
    maze[y][x] = score
    tile = maze[y+dy][x+dx]
    if tile == "E":
        if total is None or score+1 < total:
            total = score+1
            roads = [path+str(x+dx)+" "+str(y+dy)+","]
        elif score+1 == total:
            roads.append(path+str(x+dx)+" "+str(y+dy)+",")
    elif tile == "." or (isinstance(tile, int) and score-999 <= tile):
        step(x+dx, y+dy, dx, dy, maze, score+1, path)
    for k in [1, -1]:
        kx, ky = k*dy, k*dx
        if maze[y+ky][x+kx] == "." or (isinstance(maze[y+ky][x+kx], int) and score <= maze[y+ky][x+kx]):
            step(x+kx, y+ky, kx, ky,  maze, score+1001, path)


roads = []
lines = copy.deepcopy(save)
total = None
step(1, len(lines)-2, 1, 0, lines, 0, "")
positions = []
for road in roads:
    for pos in road.split(",")[:-1]:
        if pos not in positions:
            positions.append(pos)
print(len(positions))
