import time
import re
from collections import defaultdict, deque


def main():
    lines = open("Inputs/input07.txt").read().splitlines()
    t = time.time()

    total1 = solve1(lines)
    total2 = solve2(lines)

    print(total1)
    print(total2)
    print(time.time()-t)


def solve1(lines: list) -> int:
    bags = defaultdict(list)
    for line in lines:
        line = re.split(" contain |, ", line)

        if line[1] == "no other bags.":
            continue

        outer = line[0][:-5]
        for inner in line[1:]:
            inner = inner.rstrip("bags.")[2:-1]
            bags[inner].append(outer)
    
    total = -1
    visited = set()
    dq = deque(["shiny gold"])
    while dq:
        total += 1
        curr = dq.pop()

        for bag in bags[curr]:
            if bag not in visited:
                visited.add(bag)
                dq.appendleft(bag)

    return total


def solve2(lines: list) -> int:
    bags = {}
    for line in lines:
        line = re.split(" contain |, ", line)

        if line[1] == "no other bags.":
            bags[line[0][:-5]] = []

        else:
            bags[line[0][:-5]] = [tuple(bag.rstrip("bags.")[:-1].split(" ", 1)) for bag in line[1:]]
    
    total = -1
    dq = deque([(1, "shiny gold")])
    while dq:
        k, curr = dq.pop()
        total += k

        for bag in bags[curr]:
            dq.appendleft((k*int(bag[0]), bag[1]))
    
    return total


if __name__ == "__main__":
    main()
