import time

file = [lines.splitlines() for lines in open("2025/Inputs/input05.txt").read().split("\n\n")]
ranges = [tuple(map(int, line.split("-"))) for line in file[0]]
ids = list(map(int, file[1]))

t = time.time()
total_1 = 0
for i in ids:
    for r in ranges:
        if r[0] <= i <= r[1]:
            total_1 += 1
            break

total_2 = 0
fresh = []
for r in ranges:
    r = [r]
    while r:
        s, e = r.pop()
        for sf, ef in fresh:

            if s < sf:
                if e >= sf:
                    if e <= ef:
                        e = sf-1
                    else:
                        e = sf-1
                        r.append(ef+1, e)
                else:
                    pass
            else:
                if s <= ef:
                    if e > ef:
                        s = ef+1
                    else:
                        s = None
                        break
                else:
                    pass

            if s is not None:
                fresh.append(s, e)
                            
for sf, ef in fresh:
    total_2 += ef-sf+1

print(total_1)
print(total_2)
print(time.time()-t)
