lines  = open("Inputs/Advent_of_Code_01.txt").read().splitlines()

total = 0
total1 = 0
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
        total1 -= 1
    if pos <= 0:
        total1 += -((pos-1)//100)
    else:
        total1 += pos//100
    pos = pos % 100
    start = False
    if not pos:
        total += 1
        start = True

print(total)
print(total1)
