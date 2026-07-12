import time
import copy


def main():
    lines = list(map(list, open("Inputs/input11.txt").read().splitlines()))
    t = time.time()

    total1 = solve1(copy.deepcopy(lines))
    total2 = solve2(lines)

    print(total1)
    print(total2)
    print(time.time()-t)


def solve1(grid: list) -> int:
    length = len(grid)
    width = len(grid[0])

    stable = False
    while not stable:
        stable = True

        occupied = [[0]*width for _ in range(length)]
        for y in range(length):
            for x in range(width):
                if grid[y][x] == "L":

                    ry = range(max((0, y-1)), min((y+2, length)))
                    rx = range(max((0, x-1)), min((x+2, width)))
                    for ny in ry:
                        for nx in rx:
                             occupied[ny][nx] += 1

        for y in range(length):
            for x in range(width):
                match grid[y][x]:
                    case "E":
                        if not occupied[y][x]:
                            grid[y][x] = "L"
                            stable = False
                    case "L":
                        if occupied[y][x] >= 5:
                            grid[y][x] = "E"
                            stable = False
    
    return sum([line.count("L") for line in grid])


def solve2(grid: list) -> int:
    length = len(grid)
    width = len(grid[0])

    neighbours = [[[] for __ in range(width)] for _ in range(length)]
    directions = (-1, 0, 1)
    for y in range(length):
        for x in range(width):
            if grid[y][x] == "L":

                for dy in directions:
                    for dx in directions:
                        if dx or dy:
                            cx = x+dx
                            cy = y+dy
                            while 0 <= cx < width and 0 <= cy < length:
                                if grid[cy][cx] == "L":
                                    neighbours[y][x].append((cx, cy))
                                    break
                                cx += dx
                                cy += dy

    stable = False
    while not stable:
        stable = True

        occupied = [[0]*width for _ in range(length)]
        for y in range(length):
            for x in range(width):
                if grid[y][x] == "L":
                    for nx, ny in neighbours[y][x]:
                        occupied[ny][nx] += 1


        for y in range(length):
            for x in range(width):
                match grid[y][x]:
                    case "E":
                        if not occupied[y][x]:
                            grid[y][x] = "L"
                            stable = False
                    case "L":
                        if occupied[y][x] >= 5:
                            grid[y][x] = "E"
                            stable = False
    
    return sum([line.count("L") for line in grid])


if __name__ == "__main__":
    main()
