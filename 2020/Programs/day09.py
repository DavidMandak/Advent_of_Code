import time
from collections import defaultdict, OrderedDict


def main():
    lines = list(map(int, open("Inputs/input09.txt").read().splitlines()))
    t = time.time()

    total1 = solve1(lines)
    total2 = solve2(lines, total1)

    print(total1)
    print(total2)
    print(time.time()-t)


def solve1(lines: list) -> int:
    preamble = 25
    sums = defaultdict(int)
    addends = OrderedDict([(line, []) for line in lines[:preamble]])
    for i in range(preamble):
        num = lines[i]
        for j in range(i+1, preamble):
            s = num+lines[j]
            sums[s] += 1
            addends[num].append(s)
    
    for num in lines[preamble:]:
        if not sums[num]:
            return num
        
        last = addends.popitem(last=False)[1]
        for s in last:
            sums[s] -= 1
        
        for n in addends:
            s = n+num
            sums[s] += 1
            addends[n].append(s)
        addends[num] = []


def solve2(lines: list, goal: int) -> int:
    first = 0
    last = -1
    curr = 0
    while curr != goal:
        if curr < goal:
            last += 1
            curr += lines[last]
        else:
            curr -= lines[first]
            first += 1
    
    cset = lines[first:last+1]
    total = max(cset)+min(cset)

    return total


if __name__ == "__main__":
    main()
