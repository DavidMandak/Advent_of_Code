import time

lines = open("2024/Inputs/input04.txt").read().splitlines()


def check(x, y, string):
  global total
  for a, b in directions:
    if 0 <= x+3*b < len(lines[0]) and 0 <= y+3*a < len(lines) and all(lines[y+i*a][x+i*b] == string[i]
                                                                        for i in range(1, 4)):
        total += 1

total = 0
directions = [(0, 1), (1, 0), (1, 1), (-1, 1)]
for y in range(len(lines)):
  for x in range(len(lines[0])):
    if lines[y][x] == "X":
      check(x, y, "XMAS")
    elif lines[y][x] == "S":
      check(x, y, "SAMX")
print(total)

total = 0
directions = [((-1, -1), (1, 1)), ((-1, 1), (1, -1))]
for y in range(1, len(lines)-1):
  for x in range(1, len(lines[0])-1):
    if lines[y][x] == "A":
      for a, b in directions:
        if lines[y+a[0]][x+a[1]] == "M" and lines[y+b[0]][x+b[1]] == "S":
          total += 1/2
        elif lines[y+a[0]][x+a[1]] == "S" and lines[y+b[0]][x+b[1]] == "M":
          total += 1/2
      total //= 1
print(int(total))
print(time.time()-t)
