import time
from collections import deque


def main():
    file = open("2025/Inputs/input07.txt").read().splitlines()

    lines = setup(file)
    total_1 = solve_1(lines)
    total_2 = solve_2(lines)

    return total_1, total_2


def setup(file: list) -> list:
    lines = []
    for i in range(0, len(file), 2):
        lines.append(file[i])
    
    return lines


def solve_1(lines: list) -> int:
    width = len(lines[0])
    height = len(lines)

    total_1 = 0
    start = (width//2, 0)
    bfs = deque([start])
    visited = [[False]*width for _ in range(height)]
    while bfs:
        x, y = bfs.pop()

        if y == height:
            break
        
        if visited[y][x]:
            continue
        visited[y][x] = True

        if lines[y][x] == "^":        
            total_1 += 1
            bfs.appendleft((x-1, y+1))
            bfs.appendleft((x+1, y+1))
        else:
            bfs.appendleft((x, y+1))
    
    return total_1


def solve_2(lines: list) -> int:
    width = len(lines[0])
    height = len(lines)

    total_2 = 0
    sx, sy = width//2, 0
    bfs = deque([(sx, sy)])
    beams = [[0]*width for _ in range(height+1)]
    beams[sy][sx] = 1
    while bfs:
        x, y = bfs.pop()

        if y == height:
            break

        if lines[y][x] == "^":
            for k in (-1, 1):
                nx, ny = x+k, y+1
                if not beams[ny][nx]:
                    bfs.appendleft((nx, ny))
                beams[ny][nx] += beams[y][x]
        else:
            if not beams[y+1][x]:
                bfs.appendleft((x, y+1))
            beams[y+1][x] += beams[y][x]
    
    total_2 = sum(beams[-1])

    return total_2


if __name__ == "__main__":
    t = time.time()

    total_1, total_2 = main()

    print(total_1)
    print(total_2)
    print(time.time()-t)
