import time

lines = list(map(int, open("2019/Inputs/input01.txt").read().splitlines()))

t = time.time()
total = 0
for mass in lines:
    total += mass//3-2
print(total)

total = 0
for mass in lines:
    fuel = 1
    while fuel > 0:
        fuel = mass//3-2
        total += fuel
        mass = fuel
    total -= fuel
print(total)
print(time.time()-t)
