from collections import defaultdict
import time

lines = open("2024/Inputs/input01.txt").read().splitlines()

t = time.time()
line = lines[0].split("   ")
left = [int(line[0])]
right = [int(line[1])]
for line in lines[1:]:
    line = line.split("   ")
    l, r = int(line[0]), int(line[1])
    i = 0
    while i < len(left) and l > left[i]:
        i += 1
    left.insert(i, l)
    i = 0
    while i < len(right) and r > right[i]:
        i += 1
    right.insert(i, r)
total = 0
for i in range(len(left)):
    total += abs(left[i]-right[i])
print(total)

left = defaultdict(int)
right = defaultdict(int)
for line in lines:
    line = line.split("   ")
    left[int(line[0])] += 1
    right[int(line[1])] += 1
total = 0
for num in left:
    total += num*left[num]*right[num]
print(total)
print(time.time()-t)
