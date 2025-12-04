from collections import defaultdict
line = open("2024/Inputs/input11.txt").read().split()
save = line.copy()

total = len(line)
for _ in range(25):
    for i in range(len(line)):
        if line[i] == "0":
            line[i] = "1"
        elif len(line[i])%2 == 0:
            line.append(str(int(line[i][len(line[i])//2:])))
            line[i] = line[i][:len(line[i])//2]
            total += 1
        else:
            line[i] = str(int(line[i])*2024)
print(total)

line = save
total = len(line)
for parent in line:
    next = defaultdict(int)
    next[parent] += 1
    for _ in range(75):
        stones = next.copy()
        next = defaultdict(int)
        for stone in stones:
            if stone == "0":
                next["1"] += stones[stone]
            elif len(stone)%2 == 0:
                half = len(stone)//2
                next[str(int(stone[half:]))] += stones[stone]
                next[stone[:half]] += stones[stone]
                total += stones[stone]
            else:
                next[str(int(stone)*2024)] += stones[stone]
print(total)
