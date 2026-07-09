import time


def main():
    lines = list(map(int, open("Inputs/input10.txt").read().splitlines()))
    t = time.time()

    total1 = solve1(lines)
    total2 = solve2(lines)

    print(total1)
    print(total2)
    print(time.time()-t)


def solve1(lines: list) -> int:
    lines = [0]+sorted(lines)
    one = 0
    three = 1
    for i in range(len(lines)-1):
        match lines[i+1]-lines[i]:
            case 1:
                one += 1
            case 3:
                three += 1
    
    return one*three


def solve2(lines: list) -> int:
    lines = [0]+sorted(lines)
    lines.append(lines[-1]+3)
    length = len(lines)

    arrangements = [1]+[0]*(length-1)
    for i in range(length-1):
        curr = lines[i]
        j = i+1
        while j < length and curr+3 >= lines[j]:
            arrangements[j] += arrangements[i]
            j += 1
    
    return arrangements[-1]


if __name__ == "__main__":
    main()
