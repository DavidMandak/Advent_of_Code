from collections import defaultdict
lines = open("../Inputs/Advent_of_Code_06.txt").read()

start_pos = lines.index("^")
lines = lines.splitlines()
save = lines.copy()
start_y = start_pos//(len(lines[0])+1)
start_x = start_pos%(len(lines[0])+1)
x, y = start_x, start_y
total = 0
direction = [0, -1]
k = -1
while 0 <= x < len(lines[0]) and 0 <= y < len(lines):
    if lines[y][x] == "#":
        x -= direction[0]
        y -= direction[1]
        temp = direction[0]
        direction[0] = direction[1]*k
        direction[1] = temp*k
        k *= -1
    elif lines[y][x] != "X":
        lines[y] = lines[y][:x]+"X"+lines[y][x+1:]
        total += 1
    x += direction[0]
    y += direction[1]
print(total)

total = 0
lines[start_y] = lines[start_y][:start_x]+"^"+lines[start_y][start_x+1:]
for a in range(len(lines)):
    for b in range(len(lines[a])):
        if lines[a][b] == "X":
            save[a] = save[a][:b]+"#"+save[a][b+1:]
            x, y = start_x, start_y
            direction = [0, -1]
            k = -1
            squares = defaultdict(list)
            while 0 <= x < len(lines[0]) and 0 <= y < len(lines):
                if save[y][x] == "#":
                    x -= direction[0]
                    y -= direction[1]
                    temp = direction[0]
                    direction[0] = direction[1]*k
                    direction[1] = temp*k
                    k *= -1
                if direction in squares[(x, y)]:
                    total += 1
                    break
                squares[(x, y)].append([direction[0], direction[1]])
                x += direction[0]
                y += direction[1]
            save[a] = save[a][:b]+"."+save[a][b+1:]
print(total)
