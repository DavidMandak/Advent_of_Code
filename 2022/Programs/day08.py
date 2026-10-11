line = open("08.txt").read()
print(line)
i = 0
a = 0
print(len(line))
while i < 9899:
    print(line[i], end="")
    no = 0
    if i % 100 == 99:
        i += 1
        continue
    j = i-1
    while j % 100 != 99:
        if int(line[j]) >= int(line[i]):
            no = 1
            break
        j -= 1
    if no != 1:
        a += 1
        i += 1
        continue
    no = 0
    j = i+1
    while j % 100 != 99:
        if int(line[j]) >= int(line[i]):
            no = 1
            break
        j += 1
    if no != 1:
        a += 1
        i += 1
        continue
    no = 0
    j = i+100
    while j < 9899:
        if int(line[j]) >= int(line[i]):
            no = 1
            break
        j += 100
    if no != 1:
        a += 1
        i += 1
        continue
    no = 0
    j = i-100
    while j > -1:
        if int(line[j]) >= int(line[i]):
            no = 1
            break
        j -= 100
    if no != 1:
        a += 1
        i += 1
        continue
    i += 1
print()
print(a)
i = 101
a = 0
most = 0
while i != 9798:
    a = 0
    b = 0
    if i % 100 == 98:
        i += 3
        continue
    j = i-1
    while j % 100 != 99:
        if int(line[j]) >= int(line[i]):
            b += 1
            break
        b += 1
        j -= 1
    a = b
    b = 0
    j = i+1
    while j % 100 != 99:
        if int(line[j]) >= int(line[i]):
            b += 1
            break
        b += 1
        j += 1
    a *= b
    b = 0
    j = i+100
    while j < 9899:
        if int(line[j]) >= int(line[i]):
            b += 1
            break
        b += 1
        j += 100
    a *= b
    b = 0
    j = i-100
    while j > -1:
        if int(line[j]) >= int(line[i]):
            b += 1
            break
        b += 1
        j -= 100
    a *= b
    i += 1
    if a > most:
        most = a
print(most)
