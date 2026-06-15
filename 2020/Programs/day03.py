import time


def main():
    grid = open("Inputs/input03.txt").read().splitlines()
    t = time.time()

    total1 = solve(grid, [(3, 1)])
    total2 = solve(grid, [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)])

    print(total1)
    print(total2)
    print(time.time()-t)


def solve(grid: list, slopes: list) -> int:
    total = 1
    for dx, dy in slopes:
        total *= check(grid, dx, dy)

    return total


def check(grid: list, dx: int, dy: int) -> int:
    height = len(grid)
    width = len(grid[0])
    
    x = 0
    y = 0
    total = 0
    while y < height:
        if grid[y][x] == "#":
            total += 1

        y += dy
        x = (x+dx) % width
    
    return total


if __name__ == "__main__":
    main()
