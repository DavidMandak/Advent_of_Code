lines = open("../Inputs/Advent_of_Code_12.txt").read().splitlines()
save = lines.copy()


def f(crop, x, y):
    global area, perimeter, lines
    dx, dy = 1, 0
    lines[y] = lines[y][:x]+lines[y][x].casefold()+lines[y][x+1:]
    for _ in range(4):
        next_x = x+dx
        next_y = y+dy
        if 0 <= next_x < len(lines[0]) and 0 <= next_y < len(lines):
            if lines[next_y][next_x] == crop:
                f(crop, x+dx, y+dy)
                area += 1
            elif crop.casefold() != lines[next_y][next_x]:
                perimeter += 1
        else:
            perimeter += 1
        temp = dy
        dy = -1*dx
        dx = temp


total = 0
for y in range(len(lines)):
    for x in range(len(lines[y])):
        if ord(lines[y][x]) < 91:
            area = 1
            perimeter = 0
            f(lines[y][x], x, y)
            total += area*perimeter
print(total)


def g(crop, x, y):
    global area, corners, lines
    if 0 <= x < len(lines[0]) and 0 <= y < len(lines):
        if lines[y][x] == crop:
            area += 1
            lines[y] = lines[y][:x]+lines[y][x].casefold()+lines[y][x+1:]
            neighbors = 4*[None]
            for i in range(4):
                dx, dy = directions[i]
                neighbors[i] = g(crop, x+dx, y+dy)
            for i in range(-1, 3):
                if neighbors[i] is False:
                    if neighbors[i+1] is False:
                        corners += 1
                elif neighbors[i+1] is True:
                    d = 2*[0]
                    d[i % 2] = directions[i][i % 2]
                    i += 1
                    d[i % 2] = directions[i][i % 2]
                    if g(crop, x+d[0], y+d[1]) is False:
                        corners += 1
            return True
        elif lines[y][x] == crop.casefold():
            return True
    return False


lines = save
total = 0
directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
for y in range(len(lines)):
    for x in range(len(lines[y])):
        if ord(lines[y][x]) < 91:
            area = 0
            corners = 0
            g(lines[y][x], x, y)
            total += area*corners
print(total)
