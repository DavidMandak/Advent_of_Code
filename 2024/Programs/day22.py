from collections import  defaultdict
lines = list(map(int, open("../Inputs/Advent_of_Code_22.txt").read().splitlines()))

total = 0
count = 0
highs = defaultdict(int)
for line in lines:
    done = []
    last = int(str(line)[-1])
    path = "," * 4
    for _ in range(2000):
        line = (line^(line*64))%16777216
        line = (line^(line//32))%16777216
        line = (line^(line*2048))%16777216
        price = int(str(line)[-1])
        path = path.split(",", 1)[1]
        path += f"{price-last},"
        if path[0] != "," and path not in done:
            done.append(path)
            highs[path] += price
        last = price
    total += line
print(total)

most = 0
for high in highs:
    if highs[high] > most:
        most = highs[high]
print(most)
