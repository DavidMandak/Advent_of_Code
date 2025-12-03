lines = open("Advent_of_Code_9.txt").read().splitlines()
total = 0
for i in range(0, len(lines)):
    lines[i] = lines[i].split(" ")
    line = lines[i]
    for j in range(0, len(lines[i])):
        line[j] = int(line[j])


def check(sequence):
    for number in sequence:
        if number != 0:
            return True
    return False


for line in lines:
    sequences = [line.copy()]
    while check(sequences[-1]):
        addition = []
        for i in range(1, len(sequences[-1])):
            addition.append(sequences[-1][i]-sequences[-1][i-1])
        sequences.append(addition)
    for i in range(1, len(sequences)):
        sequences[-i-1].insert(0, sequences[-i-1][0]-sequences[-i][0])
    total += sequences[0][0]
print(total)
