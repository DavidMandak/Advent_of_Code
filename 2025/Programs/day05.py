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

print(total_1)
print(time.time()-t)
