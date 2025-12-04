import time

lines = open("2023/Inputs/input12.txt").read().splitlines()

t = time.time()
springs = []
records = []
total = 0
transfer = None
for line in lines:
    line = line.split(" ")
    springs.append(((line[0]+"?")*5)[:-1])
    record = line[1].split(",")*5
    for i in range(0, len(record)):
        record[i] = int(record[i])
    records.append(record)


def generate(location_index, place, row, record, record_index, sequence, checking):
    global transfer, total
    if place == count:
        if memoization(row, len(row)-1, record, record_index, sequence, checking, location_index) is not False:
            total += 1
    else:
        save = row
        for i in range(location_index+1, len(unknown)-count+1+place):
            row = save
            location = unknown[i]
            row = row[:location]+"#"+row[location+1:]
            transfer = None
            if memoization(row, location, record, record_index, sequence, checking, location_index) is False:
                continue
            generate(i, place+1, row, record, transfer[0], transfer[1], transfer[2])


def memoization(row, location, record, record_index, sequence, checking, location_index):
    global transfer
    if location_index == -1:
        start = 0
    else:
        start = unknown[location_index]+1
    for i in range(start, location+1):
        spring = row[i]
        if checking is True:
            if spring == "#":
                sequence -= 1
            elif sequence == 0:
                checking = False
                record_index += 1
            else:
                return False
        elif spring == "#":
            checking = True
            sequence = record[record_index]-1
    if sequence < 0:
        return False
    transfer = [record_index, sequence, checking]


def check(row, record):
    global total
    row += "."
    a = 0
    sequence = None
    checking = False
    for spring in row:
        if checking is True:
            if spring == "#":
                sequence -= 1
            elif sequence < 0:
                return
            elif sequence == 0:
                checking = False
                a += 1
            else:
                return
        elif spring == "#":
            checking = True
            sequence = record[a]-1
    total += 1
    return True


for i in range(0, len(lines)):
    row = springs[i]
    count = 0
    for num in records[i]:
        count += num
    unknown = []
    for j in range(0, len(row)):
        if row[j] == "#":
            count -= 1
        elif row[j] == "?":
            unknown.append(j)
    generate(-1, 0, springs[i], records[i], 0, None, False)
    break
print(total)
print(time.time()-t)
