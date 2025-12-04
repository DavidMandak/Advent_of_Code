import time

line = open("2024/Inputs/input09.txt").read().splitlines()[0]

line = list(map(int, line))
save = line.copy()
total = 0
front = 0
back = line[-1]
line = line[:-1]
pos = -1
while front < len(line):
    for pos in range(pos+1, pos+line[front]+1):
        total += front//2*pos
    front += 1
    for pos in range(pos+1, pos+line[front]+1):
        if back > 0:
            total += len(line)//2*pos
            back -= 1
        elif front != len(line)-1:
            back = line[-2]-1
            line = line[:-2]
            total += len(line)//2*pos
        else:
            break
    front += 1
for pos in range(pos+1, pos+back+1):
    total += front//2*pos
print(total)

line = save
total = 0
front = 0
pos = -1
while front < len(line):
    if isinstance(line[front], int):
        for pos in range(pos+1, pos+line[front]+1):
            total += front//2*pos
    else:
        pos += int(line[front])
    front += 1
    if front != len(line):
        space = line[front]
    else:
        break
    back = len(line)-1
    while space != 0:
        if back < front:
            pos += space
            break
        elif isinstance(line[back], int) and line[back] <= space:
            if line[back] < space:
                space -= line[back]
            elif line[back] == space:
                space = 0
            for pos in range(pos+1, pos+line[back]+1):
                total += back//2*pos
            line[back] = str(line[back])
        back -= 2
    front += 1
print(total)
print(time.time()-t)
