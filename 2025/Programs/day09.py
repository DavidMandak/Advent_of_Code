import time


def main():
    lines = [tuple(map(int, line.split(","))) for line in open("2025/Inputs/input09.txt").read().splitlines()]

    total_1 = solve(lines)

    print(total_1)


def solve(lines: list) -> int:
    total_1 = 0
    length = len(lines)
    for i in range(length):
        x, y = lines[i]
        for j in range(i+1, length):
            a, b = lines[j]
            area = (abs(x-a)+1)*(abs(y-b)+1)
            if area > total_1:
                total_1 = area
    
    return total_1


if __name__ == "__main__":
    main()