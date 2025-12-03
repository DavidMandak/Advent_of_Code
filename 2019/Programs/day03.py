first, second = [wire.split(",") for wire in open("../Inputs/Advent_of_Code_03.txt").read().replace("R", "1 0 ")
.replace("L", "-1 0 ").replace("U", "0 -1 ").replace("D", "0 1 ").splitlines()]

step_total, man_total = None, None
x, y = 0, 0
steps = 0
h = []
v = []
for line in first:
    dx, dy, distance = list(map(int, line.split()))
    if dy == 0:
        h.append((range(x, x+dx*(distance+1), dx), y, steps))
        x += dx*distance
    else:
        v.append((x, range(y, y+dy*(distance+1), dy), steps))
        y += dy*distance
    steps += distance
x, y = 0, 0
steps = 0
for line in second:
    dx, dy, distance = list(map(int, line.split()))
    if dy == 0:
        width = range(x, x+dx*(distance+1), dx)
        for path in v:
            if path[0] in width and y in path[1]:
                man = abs(y)+abs(path[0])
                if man != 0 and (man_total is None or man < man_total):
                    man_total = man
                step_sum = steps+abs(path[0]-x)+path[2]+abs(y-path[1][0])
                if step_sum != 0 and (step_total is None or step_sum < step_total):
                    step_total = step_sum
        x += dx*distance
    else:
        height = range(y, y+dy*(distance+1), dy)
        for path in h:
            if path[1] in height and x in path[0]:
                man = abs(x)+abs(path[1])
                if man != 0 and (man_total is None or man < man_total):
                    man_total = man
                step_sum = steps+abs(path[1]-y)+path[2]+abs(x-path[0][0])
                if step_sum != 0 and (step_total is None or step_sum < step_total):
                    step_total = step_sum
        y += dy*distance
    steps += distance
print(f"{man_total}\n{step_total}")
