import time


def main():
    lines = open("Inputs/input.txt").read().splitlines()
    t = time.time()

    total = solve(lines)

    print(total)
    print(time.time()-t)


def solve(lines: list) -> int:
    pass


if __name__ == "__main__":
    main()
