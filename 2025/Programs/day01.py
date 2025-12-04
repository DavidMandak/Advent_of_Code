import time

lines  = open("Inputs/Advent_of_Code_01.txt").read().splitlines()

t = time.time()
total_1 = 0
total_2 = 0
pos = 50
start = False
for rotation in lines:

    match rotation[0]:
        case "R":
            pos += int(rotation[1:])
        case "L":
            pos -= int(rotation[1:])
        case _:
            raise Exception

    if start and pos < 0:
        total_2 -= 1
    if pos <= 0:
        total_2 += -((pos-1)//100)
    else:
        total_2 += pos//100
    pos = pos % 100
    start = False
    if not pos:
        total_1 += 1
        start = True

print(total_1)
print(total_2)
print(time.time()-t)
