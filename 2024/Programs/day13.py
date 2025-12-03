problems = open("../Inputs/Advent_of_Code_13.txt").read().split("\n\n")

total = 0
for problem in problems:
    temp = []
    for line in problem.splitlines():
        line = line.split("X")[1][1:].split(", Y")
        temp.append((int(line[0]), int(line[1][1:])))
    a, c = temp[0]
    b, d = temp[1]
    x, y = temp[2]
    x += 10**13  # Delete these two lines
    y += 10**13  # for the first part
    result_B = (y*a-x*c)/(a*d-c*b)
    if result_B.is_integer():
        result_A = (x-b*result_B)/a
        if result_A.is_integer():
            total += int(3*result_A+result_B)
print(total)
