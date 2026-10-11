lines = open("06.txt").readlines()
line = lines[0]
a = 14
while True:
    i = 1
    while i != 15:
        j = 1
        while j != 15:
            if j == i:
                j += 1
                continue
            if line[a-j] == line[a-i]:
                break
            if j == 14:
                j = 15
                break
            j += 1
        if j != 15:
            break
        i += 1
    if i == 15:
        break
    print(line[a-14])
    a += 1
print(a)
