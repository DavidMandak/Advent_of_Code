lines = open("2023/Inputs/input05.txt").read().split("\n\n")
lines[0] = lines[0].split(" ")
lines[0].pop(0)
seeds = []
seeds_change = []
for i in range(0, len(lines[0]), 2):
    seeds.append([int(lines[0][i]), int(lines[0][i])+int(lines[0][i+1])])
for i in range(1, len(lines)):
    lines[i] = lines[i].split("\n")
    lines[i].pop(0)
    for j in range(0, len(lines[i])):
        lines[i][j] = lines[i][j].split(" ")
for change_index in range(1, len(lines)):
    change = lines[change_index]
    if change_index != 1:
        seeds = seeds_change.copy()
        seeds_change = []
    for seed in seeds:
        source_list = []
        destination_list = []
        start = seed[0]
        end = seed[1]
        for group in change:
            destination = int(group[0])
            source = int(group[1])
            finish = source+int(group[2])
            if source <= start:
                if finish >= start:
                    if finish >= end:
                        source_list.append([start, end])
                        destination_list.append([destination+start-source, destination+end-source])
                        break
                    else:
                        source_list.append([start, finish])
                        destination_list.append([destination+start-source, destination+finish-source])
            elif source <= end:
                if finish >= end:
                    source_list.append([source, end])
                    destination_list.append([destination, destination+end-source])
                else:
                    source_list.append([source, finish])
                    destination_list.append([destination, destination+finish-source])
        if len(source_list) == 0:
            seeds_change.append(seed)
            continue
        for i in range(1, len(source_list)):
            j = i
            while j > 0 and source_list[j][0] < source_list[j-1][0]:
                variable = source_list[j]
                source_list[j] = source_list[j-1]
                source_list[j-1] = variable
                j -= 1
        if source_list[0][0] > start:
            seeds_change.append([start])
        elif source_list[0][0] < start:
            exit("error 1")
        elif source_list[0][1] < end:
            seeds_change.append([source_list[0][1]+1])
            source_list.pop(0)
        elif source_list[0][1] > end:
            exit("error 2")
        else:
            seeds_change.append(destination_list[0])
            continue
        for range1 in source_list:
            if range1[0]-1 < seeds_change[-1][0]:
                seeds_change[-1][0] = range1[1]+1
            seeds_change[-1].append(range1[0]-1)
            seeds_change.append([range1[1]+1])
        if seeds_change[-1][0] < end+1:
            seeds_change[-1].append(end)
        elif seeds_change[-1][0] > end+1:
            exit("error 4")
        else:
            seeds_change.pop(-1)
        for range1 in destination_list:
            seeds_change.append(range1)
low = 99999999999999999999
for seed in seeds_change:
    if seed[0] < low:
        low = seed[0]
print(low)
