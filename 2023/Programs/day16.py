lines = open("Advent_of_Code_16.txt").read().splitlines()
energy_map = []
total = 0
most = 0
for i in range(0, len(lines)):
    energy_map.append("."*len(lines[i]))
backup = energy_map.copy()


def f(x, y, direction):
    global total
    while 0 <= x < len(lines[0]) and 0 <= y < len(lines):
        if energy_map[y][x] == ".":
            energy_map[y] = energy_map[y][:x]+"#"+energy_map[y][x+1:]
            total += 1
        elif lines[y][x] == "-" or lines[y][x] == "|":
            return
        tile = lines[y][x]
        if direction == "R":
            if tile == "." or tile == "-":
                x += 1
            elif tile == "/":
                y -= 1
                direction = "U"
            elif tile == "\\":
                y += 1
                direction = "D"
            else:
                f(x, y-1, "U")
                y += 1
                direction = "D"
        elif direction == "L":
            if tile == "." or tile == "-":
                x -= 1
            elif tile == "/":
                y += 1
                direction = "D"
            elif tile == "\\":
                y -= 1
                direction = "U"
            else:
                f(x, y-1, "U")
                y += 1
                direction = "D"
        elif direction == "U":
            if tile == "." or tile == "|":
                y -= 1
            elif tile == "/":
                x += 1
                direction = "R"
            elif tile == "\\":
                x -= 1
                direction = "L"
            else:
                f(x-1, y, "L")
                x += 1
                direction = "R"
        else:
            if tile == "." or tile == "|":
                y += 1
            elif tile == "/":
                x -= 1
                direction = "L"
            elif tile == "\\":
                x += 1
                direction = "R"
            else:
                f(x - 1, y, "L")
                x += 1
                direction = "R"


for x, d in (0, "R"), (len(lines[0])-1, "L"):
    for y in range(0, len(lines)):
        f(x, y, d)
        if total > most:
            most = total
        total = 0
        energy_map = backup.copy()
for y, d in (0, "D"), (len(lines)-1, "U"):
    for x in range(0, len(lines[0])):
        f(x, y, d)
        if total > most:
            most = total
        total = 0
        energy_map = backup.copy()
print(most)
