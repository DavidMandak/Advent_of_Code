import time

lines = open("2025/Inputs/input04.txt").read().splitlines()

t = time.time()
total_1 = 0
height = len(lines)
width = len(lines[0])
grid = [[None]*width for _ in range(height)]
removable = []

for y in range(height):
    for x in range(width):
        if lines[y][x] == "@":

            neighbours = 0
            for dy in range(-1, 2):
                for dx in range (-1, 2):
                    nx, ny = x+dx, y+dy
                    if 0 <= nx < width and 0 <= ny < height and lines[ny][nx] == "@":
                        neighbours += 1

            
            if neighbours < 5:
                total_1 += 1
                removable.append((x, y))
            else:
                grid[y][x] = neighbours

total_2 = 0
while removable:
    x, y = removable.pop()
    total_2 += 1

    for dy in range(-1, 2):
        for dx in range (-1, 2):
            nx, ny = x+dx, y+dy
            if 0 <= nx < width and 0 <= ny < height:
                neighbour = grid[ny][nx]

                if neighbour is not None:
                    if neighbour-1 < 5:
                        removable.append((nx, ny))
                        grid[ny][nx] = None
                    else:
                        grid[ny][nx] -= 1

print(total_1)
print(total_2)
print(time.time()-t)
