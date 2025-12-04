import sys, copy
lines = open("2024/Inputs/input18.txt").read().splitlines()
sys.setrecursionlimit(10**6)

size = 71
amount = 2000 # Change this to 1024 for the first part, my code for the second part is not very optimal, so I just started at 2000
grid = []
for _ in range(size):
    grid.append([None]*size)
for i in range(amount):
    x, y = tuple(map(int, lines[i].split(",")))
    grid[y][x] = 0
save = copy.deepcopy(grid)


def move(x, y, steps):
    global grid
    grid[y][x] = steps
    if (x, y) != (size-1, size-1):
        steps += 1
        dx, dy = 1, 0
        for _ in range(4):
            if 0 <= y+dy < size and 0 <= x+dx < size:
                neighbour = grid[y+dy][x+dx]
                if neighbour is None or steps < neighbour:
                    move(x+dx, y+dy, steps)
            temp = dy
            dy = -1*dx
            dx = temp


move(0, 0, 0)
print(grid[size-1][size-1])


def step(x, y, steps, path):
    global grid, goal
    grid[y][x] = steps
    path += f"{x},{y}, "
    if (x, y) != (size-1, size-1):
        steps += 1
        dx, dy = 1, 0
        for _ in range(4):
            if 0 <= y+dy < size and 0 <= x+dx < size:
                neighbour = grid[y+dy][x+dx]
                if neighbour is None or steps < neighbour:
                    if step(x+dx, y+dy, steps, path):
                        return True
            temp = dy
            dy = -1*dx
            dx = temp
        return False
    else:
        goal = path
        return True


grid = copy.deepcopy(save)
goal = None
step(0, 0, 0, "")
byte = amount
while goal is not None:
    bx, by = tuple(map(int, lines[byte].split(",")))
    save[by][bx] = 0
    if lines[byte] in goal:
        grid = copy.deepcopy(save)
        goal = None
        step(0, 0, 0, "")
    byte += 1
print(lines[byte-1])
