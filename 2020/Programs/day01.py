import time


def main():
    lines = list(map(int, open("Inputs/input01.txt").read().splitlines()))
    t = time.time()

    total1 = solve1(lines)
    total2 = solve2(lines)

    print(total1)
    print(total2)
    print(time.time()-t)


def solve1(lines: list) -> int:
    gaps = []
    for line in lines:

        if line in gaps:
            return line*(2020-line)
        gaps.append(2020-line)
    
    return None


def solve2(lines: list) -> int:
    gaps = {}
    for i in range(len(lines)):
        line = lines[i]

        if line in gaps:
            print(line, gaps[line])
            return line*gaps[line]
        
        for pair in lines[i:]:
            if pair+line < 2020:
                gaps[2020-(pair+line)] = pair*line


if __name__ == "__main__":
    main()
