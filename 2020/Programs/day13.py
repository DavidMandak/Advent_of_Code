import time


def main():
    lines = open("Inputs/input13.txt").read().splitlines()
    t = time.time()

    total1 = solve1(lines1)
    total2 = solve2(lines2)

    print(total1)
    print(total2)
    print(time.time()-t)


def solve1(lines: list) -> int:
    time = int(lines[0])
    buses = list(map(int, lines[1].replace(",", "").replace("x", " ").split()))

    low = float("inf")
    num = None
    for bus in buses:
        wait = bus - (time % bus)
        if wait < low:
            low = wait
            num = bus
    
    return low*num


def solve2(lines: list) -> int:
    


if __name__ == "__main__":
    main()
