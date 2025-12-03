lines = open("Advent_of_Code_6.txt").read().splitlines()
races = []
total = 1
time = int(lines[0])
record = int(lines[1])
for ms in range(1, (time//2)+1):
    destination = (time-ms)*ms
    if destination > record:
        total *= time-(2*ms)+1
        print(time-(2*ms)+1)
        break
print(total)
