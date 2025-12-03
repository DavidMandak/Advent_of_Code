from collections import defaultdict
lines = open("../Inputs/Advent_of_Code_08.txt").read().splitlines()
save = lines.copy()

antennas = defaultdict(list)
for y in range(len(lines)):
    for x in range(len(lines[y])):
        if lines[y][x] != ".":
            antennas[lines[y][x]].append((x, y))

total = 0
for antenna in antennas:
    for i in range(len(antennas[antenna])):
        p_x, p_y = antennas[antenna][i]
        for x, y in antennas[antenna][i+1:]:
            x_pos1 = 2*x-p_x
            y_pos1 = 2*y-p_y
            x_pos2 = 2*p_x-x
            y_pos2 = 2*p_y-y
            if 0 <= x_pos1 < len(lines[0]) and 0 <= y_pos1 < len(lines) and lines[y_pos1][x_pos1] != "#":
                lines[y_pos1] = lines[y_pos1][:x_pos1]+"#"+lines[y_pos1][x_pos1+1:]
                total += 1
            if 0 <= x_pos2 < len(lines[0]) and 0 <= y_pos2 < len(lines) and lines[y_pos2][x_pos2] != "#":
                lines[y_pos2] = lines[y_pos2][:x_pos2]+"#"+lines[y_pos2][x_pos2+1:]
                total += 1
print(total)

total = 0
lines = save
for antenna in antennas:
    for i in range(len(antennas[antenna])):
        p_x, p_y = antennas[antenna][i]
        for x, y in antennas[antenna][i+1:]:
            x_dif = x-p_x
            y_dif = y-p_y
            p_x_dif = p_x-x
            p_y_dif = p_y-y
            k = 0
            while 0 <= x+k*x_dif < len(lines[0]) and 0 <= y+k*y_dif < len(lines):
                if lines[y+k*y_dif][x+k*x_dif] != "#":
                    lines[y+k*y_dif] = lines[y+k*y_dif][:x+k*x_dif]+"#"+lines[y+k*y_dif][x+k*x_dif+1:]
                    total += 1
                k += 1
            k = 0
            while 0 <= p_x+k*p_x_dif < len(lines[0]) and 0 <= p_y+k*p_y_dif < len(lines):
                if lines[p_y+k*p_y_dif][p_x+k*p_x_dif] != "#":
                    lines[p_y+k*p_y_dif] = lines[p_y+k*p_y_dif][:p_x+k*p_x_dif]+"#"+lines[p_y+k*p_y_dif][p_x+k*p_x_dif+1:]
                    total += 1
                k += 1
print(total)
