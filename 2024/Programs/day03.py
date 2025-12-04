import time

lines = open("2024/Inputs/input03.txt").read().splitlines()

t = time.time()
total = 0
for line in lines:
    i = 0
    while i < len(line):
        if line[i:i+4] == "mul(":
            i += 4
            a = ""
            b = ""
            try:
                while line[i] != ",":
                    int(line[i])
                    a += line[i]
                    i += 1
                i += 1
                while line[i] != ")":
                    int(line[i])
                    b += line[i]
                    i += 1
            except ValueError:
                continue
            total += int(a)*int(b)
        i += 1
print(total)

total = 0
enabled = True
for line in lines:
    i = 0
    while i < len(line):
        if line[i:i+7] == "don't()":
            enabled = False
        elif line[i:i+4] == "do()":
            enabled = True
        elif enabled is True and line[i:i+4] == "mul(":
            i += 4
            a = ""
            b = ""
            try:
                while line[i] != ",":
                    int(line[i])
                    a += line[i]
                    i += 1
                i += 1
                while line[i] != ")":
                    int(line[i])
                    b += line[i]
                    i += 1
            except ValueError:
                continue
            total += int(a)*int(b)
        i += 1
print(total)
print(time.time()-t)
