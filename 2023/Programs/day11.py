lines = open("2023/Inputs/input11.txt").read().splitlines()
galaxies = []
y_empty = []
empty_line = 30
total = 0
x_empty = []
for y in range(0, len(lines)):
    if lines[y] == lines[empty_line]:
        y_empty.append(y)


def column(x):
    for y in range(0, len(lines)):
        if lines[y][x] != ".":
            return False
    return True


for x in range(0, len(lines[0])):
    if column(x) is True:
        x_empty.append(x)
for y in range(0, len(lines)):
    for x in range(len(lines[y])):
        if lines[y][x] == "#":
            galaxies.append([x, y])
i = 1
for galaxy in galaxies:
    for j in range(i, len(galaxies)):
        destination = galaxies[j]
        total += abs(galaxy[0]-destination[0])+abs(galaxy[1]-destination[1])
        if galaxy[0] < destination[0]:
            x_start = galaxy[0]+1
            x_end = destination[0]
        else:
            x_start = destination[0]+1
            x_end = galaxy[0]
        for x in range(x_start, x_end):
            if x in x_empty:
                total += 999999
        if galaxy[1] < destination[1]:
            y_start = galaxy[1]+1
            y_end = destination[1]
        else:
            y_start = destination[1]+1
            y_end = galaxy[1]
        for y in range(y_start, y_end):
            if y in y_empty:
                total += 999999
    i += 1
print(total)
