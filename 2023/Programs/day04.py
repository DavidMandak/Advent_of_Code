import re
lines = open("Advent_of_Code_4.txt").read().splitlines()
points = 0
total = 0
index = 0
dict = {}
for line in lines:
    line = line.split(": ")[1].split(" | ")
    win = re.split("  | ", line[0])
    own = re.split("  | ", line[1])
    if index in dict:
        dict[index] += 1
    else:
        dict[index] = 1
    for number in own:
        if number == "":
            pass
        elif number in win:
            points += 1
    for i in range(index+1, index+points+1):
        if i in dict:
            dict[i] += dict[index]
        else:
            dict[i] = dict[index]
        total += dict[index]
    index += 1
    points = 0
print(dict)
print(total+197)
