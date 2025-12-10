from PIL import Image
import time


def main():
    lines = [tuple(map(int, line.split(","))) for line in open("2025/Inputs/input09.txt").read().splitlines()]
    t = time.time()

    total_1, total_2 = solve(lines)

    print(total_1)
    print(total_2)
    print(time.time()-t)


def solve(lines: list) -> int:
    total_1 = 0
    total_2 = 0
    length = len(lines)
    for i in range(length):
        x, y = lines[i]
        for j in range(i+2, length):
            a, b = lines[j]
            area = (abs(x-a)+1)*(abs(y-b)+1)
            if area > total_2 and check(sorted((x, a)), sorted((y, b)), lines):
                total_2 = area
            elif area > total_1:
                total_1 = area
            
    return total_1, total_2


def check(rx: list, ry: list, lines: list) -> bool:
    sx, ex = rx
    sy, ey = ry
    for x, y in lines:
        if sx < x < ex and sy < y < ey:
            return False
    return True


if __name__ == "__main__":
    main()
