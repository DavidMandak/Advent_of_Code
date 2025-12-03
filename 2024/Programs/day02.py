lines = open("../Inputs/Advent_of_Code_02.txt").read().splitlines()

total = 0
for line in lines:
    line = list(map(int, line.split()))
    for i in range(len(line)-1):
        if line[i] < line[i+1] <= line[i]+3:
            pass
        else:
            total -= 1
            break
    for i in range(len(line)-1):
        if line[i] > line[i+1] >= line[i]-3:
            pass
        else:
            total -= 1
            break
    total += 2
print(total)

# Doesn't work, used a little thinking and the code above to figure out how many to add
total = 0
for line in lines:
    line = list(map(int, line.split()))
    test = 0
    i = 0
    while i < len(line)-1:
        if line[i] < line[i+1] <= line[i]+3:
            pass
        elif test == 0:
            if i+2 == len(line):
                break
            elif line[i] < line[i+2] <= line[i]+3:
                test += 1
                i += 1
            else:
                total -= 1
                break
        else:
            total -= 1
            break
        i += 1
    test = 0
    i = 0
    while i < len(line)-1:
        if line[i] > line[i+1] >= line[i]-3:
            pass
        elif test == 0:
            if i+2 == len(line):
                break
            elif line[i] > line[i+2] >= line[i]-3:
                test += 1
                i += 1
            else:
                total -= 1
                break
        else:
            total -= 1
            break
        i += 1
    total += 2
print(total)
