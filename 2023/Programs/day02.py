import re
lines = open("Advent_of_Code_2.txt").read().splitlines()
total = 0
for line in lines:
    red = 0
    green = 0
    blue = 0
    bundle = re.split(": |; |, ", line)
    for single in range(1, len(bundle)):
        separate = bundle[single].split(" ")
        number = int(separate[0])
        colour = separate[1]
        if colour == "red" and number > red:
            red = number
        if colour == "green" and number > green:
            green = number
        if colour == "blue" and number > blue:
            blue = number
    total += red*green*blue
print(total)
