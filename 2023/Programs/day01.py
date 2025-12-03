lines = open("Advent_of_Code_1.txt").read().splitlines()
first = None
last = None
final = 0
x = 1
for line in lines:
    last_index = 0
    for index in range(0, len(line)):
        character = line[index]
        if character.isdigit() is True:
            last = character
            last_index = index
            if first is None:
                first = character
                first_dict = {}
                first_check = ""
                for letter in range(0, index):
                    first_check += line[letter]
                if "one" in first_check:
                    first_dict["1"] = first_check.index("one")
                if "two" in first_check:
                    first_dict["2"] = first_check.index("two")
                if "three" in first_check:
                    first_dict["3"] = first_check.index("three")
                if "four" in first_check:
                    first_dict["4"] = first_check.index("four")
                if "five" in first_check:
                    first_dict["5"] = first_check.index("five")
                if "six" in first_check:
                    first_dict["6"] = first_check.index("six")
                if "seven" in first_check:
                    first_dict["7"] = first_check.index("seven")
                if "eight" in first_check:
                    first_dict["8"] = first_check.index("eight")
                if "nine" in first_check:
                    first_dict["9"] = first_check.index("nine")
                if len(first_dict) > 0:
                    first_sorted_dict = sorted(first_dict.items(), key=lambda x: x[1])
                    first = first_sorted_dict[0][0]
    last_dict = {}
    last_check = ""
    for letter in range(-len(line)+1, -last_index):
        last_check += line[-letter]
    if "eno" in last_check:
        last_dict["1"] = last_check.index("eno")
    if "owt" in last_check:
        last_dict["2"] = last_check.index("owt")
    if "eerht" in last_check:
        last_dict["3"] = last_check.index("eerht")
    if "ruof" in last_check:
        last_dict["4"] = last_check.index("ruof")
    if "evif" in last_check:
        last_dict["5"] = last_check.index("evif")
    if "xis" in last_check:
        last_dict["6"] = last_check.index("xis")
    if "neves" in last_check:
        last_dict["7"] = last_check.index("neves")
    if "thgie" in last_check:
        last_dict["8"] = last_check.index("thgie")
    if "enin" in last_check:
        last_dict["9"] = last_check.index("enin")
    if len(last_dict) > 0:
        last_sorted_dict = sorted(last_dict.items(), key=lambda x: x[1])
        last = last_sorted_dict[0][0]
    final += int(first+last)
    print(str(x)+": "+first+last)
    first = None
    last = None
    x += 1
print(final)
