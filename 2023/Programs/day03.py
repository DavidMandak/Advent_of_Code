lines = open("Advent_of_Code_3.txt").read().splitlines()
check = False
number = ""
first_index = None
chosen = False
total = 0
gears = {}
for line_index in range(0, len(lines)):
    line = lines[line_index]
    for character_index in range(0, len(line)):
        character = line[character_index]
        if check is True:
            if character.isdigit() is True:
                number += character
            else:
                if lines[line_index][first_index-1] == "*":
                    pos = str(line_index)+","+str(first_index-1)
                    if pos in gears:
                        gears[pos].append(int(number))
                    else:
                        gears[pos] = [int(number)]
                elif lines[line_index][character_index] == "*":
                    pos = str(line_index)+","+str(character_index)
                    if pos in gears:
                        gears[pos].append(int(number))
                    else:
                        gears[pos] = [int(number)]
                else:
                    for x in [-1, 1]:
                        for index in range(first_index-1, character_index+1):
                            if lines[line_index+x][index] == "*":
                                pos = str(line_index+x)+","+str(index)
                                if pos in gears:
                                    gears[pos].append(int(number))
                                else:
                                    gears[pos] = [int(number)]
                                chosen = True
                                break
                        if chosen is True:
                            break
                chosen = False
                number = ""
                check = False
                first_index = None
        elif character.isdigit() is True:
            check = True
            number += character
            first_index = character_index
for gear in gears:
    if len(gears[gear]) == 2:
        total += gears[gear][0]*gears[gear][1]
print(gears)
print(total)
