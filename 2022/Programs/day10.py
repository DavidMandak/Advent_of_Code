lines = open("10.txt").readlines()
i = 1
j = 1
for line in lines:
    if i == 41 or i == 81 or i == 121 or i == 181 or i == 210 or i == 241:
        print()
        j = 1
        i = 1
    if j <= i <= j + 2:
        print("#", end="")
    else:
        print(".", end="")
    if line[0] == "n":
        i += 1
    else:
        i += 1
        if i == 41 or i == 81 or i == 121 or i == 181 or i == 201 or i == 241:
            print()
            j = 1
            i = 1
        if j <= i <= j + 2:
            print("#", end="")
        else:
            print(".", end="")
        i += 1
        j += int(line.split(" ")[1])
