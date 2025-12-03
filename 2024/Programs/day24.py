values, lines = open("../Inputs/Advent_of_Code_24.txt").read().split("\n\n")
lines = [line.split() for line in lines.splitlines()]
wires = {name:int(value) for name, value in [(start.split(": ")) for start in values.splitlines()]}


def check(wires, lines):
    total = []
    while len(lines) > 0:
        for inp1, gate, inp2, _, out in lines:
            if inp1 in wires and inp2 in wires:
                if gate == "AND":
                    save = wires[inp1] & wires[inp2]
                elif gate == "OR":
                    save = wires[inp1] | wires[inp2]
                else:
                    save = wires[inp1] ^ wires[inp2]
                wires[out] = save
                if out[0] == "z":
                    i = int(out[1:])
                    if i >= len(total):
                        total.extend([None]*(i-len(total)))
                        total.append(save)
                    else:
                        total[i] = save
                lines.remove([inp1, gate, inp2, _, out])
    return int(str(list(reversed(total)))[1:-1].replace(", ", ""), 2)


print(check(wires.copy(), lines.copy()))
swap = []
for line in lines:
    inp1, gate, inp2, _, out = line
    if out[0] == "z" and out != "z45":
        if out != "z45" and gate != "XOR":
            swap.append(out)
    elif inp1[0] != "x" and inp1[0] != "y" and gate == "XOR":
        swap.append(out)
for i in list(map(str, range(1, 45))):
    if len(i) == 1:
        i = "0"+i
    for inp1, gate, inp2, _, out in lines:
        if inp1[1:] == i:
            if gate == "XOR":
                found = False
                for line in lines:
                    if (line[0] == out or line[2] == out) and line[1] == "XOR":
                        found = True
                        break
                if found is False:
                    swap.append(out)
            if gate == "AND":
                found = False
                for line in lines:
                    if (line[0] == out or line[2] == out) and line[1] == "OR":
                        found = True
                        break
                if found is False:
                    swap.append(out)
swap.sort()
print(str(swap)[1:-1].replace("\'", "").replace(" ", ""))
