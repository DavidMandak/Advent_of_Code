import math
lines = open("../Inputs/Advent_of_Code_10.txt").read().splitlines()
h = len(lines)
w = len(lines[0])


def check(x, y, dx, dy, k=1):
    global count
    kx, ky = x+k*dx, y+k*dy
    if 0 <= kx < w and 0 <= ky < h:
        if lines[ky][kx] == "#" or check(x, y, dx, dy, k+1):
            return True


top = 0
for y in range(h):
    for x in range(w):
        if lines[y][x] == "#":
            count = 0
            for check_y in range(h):
                for check_x in range(w):
                    if lines[check_y][check_x] == "#":
                        dx, dy = check_x-x, check_y-y
                        d = math.gcd(dx, dy)
                        d = 1 if not d else d
                        count += 1 if check(check_x, check_y, dx//d, dy//d) else 0
            top = count if count > top else top
print(top)
