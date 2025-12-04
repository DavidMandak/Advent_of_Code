from collections import defaultdict
lines = open("2024/Inputs/input23.txt").read().splitlines()

total = 0
neighbours = defaultdict(list)
for pair in lines:
    a, b = pair.split("-")
    neighbours[a].append(b)
    neighbours[b].append(a)
groups = []
for pc in neighbours:
    if pc[0] == "t": # Change to True for part 2
        for neighbour in neighbours[pc]:
            for third in neighbours[neighbour]:
                if pc in neighbours[third] and {pc:0, neighbour:0, third:0} not in groups:
                    groups.append({pc:0, neighbour:0, third:0})
                    total += 1
print(total)
codes = defaultdict(int)
for group in list(map(list, groups)):
    for code in group:
        codes[code] += 1
party = []
for code in codes:
    if codes[code] == 66:
        party.append(code)
party.sort()
print(str(party)[2:-2].replace("\'", "").replace(" ", ""))
