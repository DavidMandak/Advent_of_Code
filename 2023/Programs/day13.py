import time

patterns = open("2023/Inputs/input13.txt").read().split("\n\n")


def search(grid, axis):
    for i in range(1, len(grid)):
        if grid[i] == grid[i-1]:
            if len(grid)-i < i:
                if check(i, len(grid) - i, grid, axis, 0) is not False:
                    return True
            else:
                if check(i, i, grid, axis, 0) is not False:
                    return True
        else:
            line_1 = grid[i]
            line_2 = grid[i-1]
            found = 0
            for j in range(0, len(line_1)):
                if line_1[j] != line_2[j]:
                    if found == 0:
                        found += 1
                    else:
                        found += 1
                        break
            if found == 1:
                if len(grid) - i < i:
                    if check(i, len(grid) - i, grid, axis, found) is not False:
                        return True
                else:
                    if check(i, i, grid, axis, found) is not False:
                        return True


def check(i, size, grid, axis, count):
    global horizontal, vertical
    for y in range(2, size+1):
        if grid[i+y-1] != grid[i-y]:
            if count != 0:
                return False
            line_1 = grid[i+y-1]
            line_2 = grid[i-y]
            found = False
            for j in range(0, len(line_1)):
                if line_1[j] != line_2[j]:
                    if found is False:
                        found = True
                    else:
                        return False
            count += 1
    if count == 1:
        if axis == "y":
            vertical += i
        else:
            horizontal += i
    else:
        return False


t = time.time()
vertical = 0
horizontal = 0
for pattern in patterns:
    pattern = pattern.splitlines()
    if search(pattern, "x") is not True:
        columns = []
        for x in range(0, len(pattern[0])):
            column = ""
            for y in range(0, len(pattern)):
                column += pattern[y][x]
            columns.append(column)
        search(columns, "y")
print(vertical+100*horizontal)
print(time.time()-t)
