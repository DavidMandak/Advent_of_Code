from collections import defaultdict

towels, designs = open("2024/Inputs/input19.txt").read().split("\n\n")
towels = towels.split(", ")


def find_front(pattern):
    if pattern == "":
        return True
    for towel in towels:
        if towel == pattern[:len(towel)]:
            if find_back(pattern[len(towel):]):
                return True
    return False


def find_back(pattern):
    if pattern == "":
        return True
    for towel in towels:
        start = len(pattern)-len(towel)
        if towel == pattern[start:]:
            if find_front(pattern[:start]):
                return True
    return False


total = 0
for design in designs.splitlines():
    if find_front(design):
        total += 1
print(total)


def front(pattern):
    global memo
    if pattern == "":
        return 1
    elif pattern in memo:
        return memo[pattern]
    count = 0
    for towel in towels:
        if towel == pattern[:len(towel)]:
            count += back(pattern[len(towel):])
    memo[pattern] = count
    return count


def back(pattern):
    global memo
    if pattern == "":
        return 1
    elif pattern in memo:
        return memo[pattern]
    count = 0
    for towel in towels:
        start = len(pattern)-len(towel)
        if towel == pattern[start:]:
            count += front(pattern[:start])
    memo[pattern] = count
    return count


total = 0
memo = defaultdict(int)
for design in designs.splitlines():
    total += front(design)
print(total)
