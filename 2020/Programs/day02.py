import time


def main():
    lines = [line.split() for line in open("Inputs/input02.txt").read().splitlines()]
    t = time.time()

    total1 = solve1(lines)
    total2 = solve2(lines)

    print(total1)
    print(total2)
    print(time.time()-t)


def solve1(lines: list) -> int:
    total = 0
    for line in lines:
        low, high = tuple(map(int, line[0].split("-")))
        letter = line[1][:1]
        password = line[2]

        if low <= password.count(letter) <= high:
            total += 1

    return total        


def solve2(lines: list) -> int:
    total = 0
    for line in lines:
        positions = tuple(map(int, line[0].split("-")))
        letter = line[1][:1]
        password = line[2]

        checks = 0
        for pos in positions:
            if password[pos-1] == letter:
                checks += 1
        
        if checks == 1:
            total += 1
    
    return total


if __name__ == "__main__":
    main()
