import time

lines = open("2024/Inputs/input21.txt").read().splitlines()
pad = {
    "7":(0, 0), "8":(1, 0), "9":(2, 0),
    "4":(0, 1), "5":(1, 1), "6":(2, 1),
    "1":(0, 2), "2":(1, 2), "3":(2, 2),
    "A":(2, 3), "0":(1, 3),
    "0,-1":(1, 0), "0,0":(2, 0),
    "-1,0":(0, 1), "0,1":(1, 1), "1,0":(2, 1)
}

t = time.time()
total = 0
segments = []
for line in lines:
    px, py = 2, 3
    code = line
    for _ in range(3):
        ey = py
        path = ""
        for num in code:
            x, y = pad[num]
            diff_x = x-px
            diff_y = y-py
            if px == 0 and y == ey or (diff_x < 0 and (x != 0 or py != ey)):
                if diff_x != 0:
                    path += f"{diff_x//abs(diff_x)},0 "*abs(diff_x)
                if diff_y != 0:
                    path += f"0,{diff_y//abs(diff_y)} "*abs(diff_y)
                path += "0,0 "
            else:
                if diff_y != 0:
                    path += f"0,{diff_y//abs(diff_y)} "*abs(diff_y)
                if diff_x != 0:
                    path += f"{diff_x//abs(diff_x)},0 "*abs(diff_x)
                path += "0,0 "
            px, py = x, y
        if _ == 0:
            segments.append([s+"0,0" for s in path.split("0,0 ")][:-1]) # This is for part 2
        code = path.split()
        px, py = 2, 0
    total += len(path.split())*int(line[:-1])
print(total)


def move(seg, depth):
    global cache
    if depth == 0:
        return len(seg.split())
    px, py = 2, 0
    ey = py
    if seg not in cache[depth]:
        path = ""
        for num in seg.split():
            x, y = pad[num]
            diff_x = x-px
            diff_y = y-py
            if px == 0 and y == ey or (diff_x < 0 and (x != 0 or py != ey)):
                if diff_x != 0:
                    path += f"{diff_x // abs(diff_x)},0 " * abs(diff_x)
                if diff_y != 0:
                    path += f"0,{diff_y // abs(diff_y)} " * abs(diff_y)
                path += "0,0 "
            else:
                if diff_y != 0:
                    path += f"0,{diff_y // abs(diff_y)} " * abs(diff_y)
                if diff_x != 0:
                    path += f"{diff_x // abs(diff_x)},0 " * abs(diff_x)
                path += "0,0 "
            px, py = x, y
        count = 0
        for part in [p+"0,0" for p in path.split("0,0 ")][:-1]:
             count += move(part, depth-1)
        cache[depth][seg] = count
        return count
    else:
        return cache[depth][seg]


cache = {d:{} for d in range(1, 26)}
total = 0
for i in range(len(lines)):
    segment = segments[i]
    seg_sum = 0
    for s in segment:
        seg_sum += move(s, 25)
    total += seg_sum*int(lines[i][:-1])
print(total)
print(time.time()-t)
