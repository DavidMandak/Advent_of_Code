from collections import defaultdict
lines = [orbit.split(")") for orbit in open("../Inputs/Advent_of_Code_06.txt").read().splitlines()]

total = 0
orbits = defaultdict(list)
for orbit in lines:
    orbits[orbit[0]].append(orbit[1])


def checksum(obj, dist):
    global total, orbits
    total += dist
    for o in orbits[obj]:
        checksum(o, dist+1)


checksum("COM", 0)
print(total)


def find_min(obj, dist):
    global orbits, you, san
    match obj:
        case "YOU":
            you = dist
            yield
        case "SAN":
            san = dist
            yield
    for o in orbits[obj]:
        match len(list(find_min(o, dist+1))):
            case 1:
                yield
            case 2:
                print(you+san-2*(dist+2))
                exit()


you, san = 0, 0
print(list(find_min("COM", 0)))
