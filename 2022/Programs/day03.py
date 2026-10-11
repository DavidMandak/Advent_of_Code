lines = open("03.txt").readlines()
a = 0
for line in lines:
    b = None
    j = len(line)//2
    while j < len(line)-1:
        i = 0
        while i <= len(line)//2-1:
            if ord(line[i]) == ord(line[j]):
                b = 1
                letter = ord(line[i])
                break
            i += 1
        if b == 1:
            if 65 <= ord(line[i]) <= 90:
                a += ord(line[i])-38
            else:
                a += ord(line[i])-96
            break
        j += 1
print(a)
x = None
y = None
z = None
a = 0
i = 0
j = 0
k = 0
saver = 0
for line in lines:
    b = 0
    if saver == 0:
        x = line
        saver += 1
        continue
    elif saver == 1:
        y = line
        saver += 1
        continue
    elif saver == 2:
        z = line
        saver = 0
    j = 0
    while j < len(y):
        i = 0
        while i < len(x):
            if ord(x[i]) == ord(y[j]):
                k = 0
                while k < len(z):
                    if ord(x[i]) == ord(z[k]):
                        b = 1
                        letter = ord(x[i])
                        break
                    k += 1
            if b == 1:
                break
            i += 1
        if b == 1:
            break
        j += 1
    if 65 <= ord(x[i]) <= 90:
        a += ord(x[i])-38
    else:
        a += ord(x[i])-96
print(a)
