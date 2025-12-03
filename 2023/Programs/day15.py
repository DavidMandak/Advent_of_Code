strings = open("Advent_of_Code_15.txt").read().split(",")
boxes = {}
total = 0
current = 0
for string in strings:
    for i in range(0, len(string)):
        if string[i] == "=":
            if current not in boxes:
                boxes[current] = {}
            boxes[current][string[:i]] = string[-1]
        elif string[i] == "-":
            if current in boxes and string[:i] in boxes[current]:
                boxes[current].pop(string[:i])
        current += ord(string[i])
        current *= 17
        current %= 256
    current = 0
for box in boxes:
    i = 1
    for label in boxes[box]:
        total += (box+1)*i*int(boxes[box][label])
        i += 1
print(total)
