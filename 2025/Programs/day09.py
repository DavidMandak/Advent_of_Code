import time


def main():
    lines = [tuple(map(int, line.split(","))) for line in open("2025/Inputs/input09.txt").read().splitlines()]
    t = time.time()

    edges = create(lines)
    total_1, total_2 = solve(lines, edges)

    print(total_1)
    print(total_2)
    print(time.time()-t)


def create(lines: list) -> list:
    edges = [[], []]
    for i in range(0, len(lines), 2):
        edges[0].append((lines[i][1], sorted((lines[i][0], lines[i-1][0]))))
    for i in range(1, len(lines), 2):
        edges[1].append((lines[i][0], sorted((lines[i][1], lines[i-1][1]))))
    
    return edges


def solve(lines: list, edges: list) -> int:
    total_1 = 0
    total_2 = 0
    length = len(lines)
    for i in range(length):
        x, y = lines[i]
        for j in range(i+2, length):
            a, b = lines[j]
            area = (abs(x-a)+1)*(abs(y-b)+1)
            if area > total_2 and check(sorted((x, a)), sorted((y, b)), edges):
                total_2 = area
            elif area > total_1:
                total_1 = area
            
    return total_1, total_2


def check(rx: list, ry: list, edges: list) -> bool:
    sx, ex = rx
    sy, ey = ry
    horizontal, vertical = edges
    for y, dx in horizontal:
        if sy < y < ey and not (dx[1] <= sx or dx[0] >= ex):
            return False
    
    for x, dy in vertical:
        if sx < x < ex and not (dy[1] <= sy or dy[0] >= ey):
            return False
    
    return True


if __name__ == "__main__":
    main()
