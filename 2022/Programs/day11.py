m0 = [99, 67, 92, 61, 83, 64, 98]
m1 = [78, 74, 88, 89, 50]
m2 = [98, 91]
m3 = [59, 72, 94, 91, 79, 88, 94, 51]
m4 = [95, 72, 78]
m5 = [76]
m6 = [69, 60, 53, 89, 71, 88]
m7 = [72, 54, 63, 80]
i = 0
a = 0
b = 0
c = 0
d = 0
e = 0
f = 0
g = 0
h = 0
while i != 10000:
    for num in m0:
        num *= 17
        if num % 3 == 0:
            m4.append(num)
        else:
            m2.append(num)
        a += 1
    m0 = []

    for num in m1:
        num *= 11
        if num % 5 == 0:
            m3.append(num)
        else:
            m5.append(num)
        b += 1
    m1 = []

    for num in m2:
        num += 4
        if num % 2 == 0:
            m6.append(num)
        else:
            m4.append(num)
        c += 1
    m2 = []

    for num in m3:
        num *= num
        if num % 13 == 0:
            m0.append(num)
        else:
            m5.append(num)
        d += 1
    m3 = []

    for num in m4:
        num += 7
        if num % 11 == 0:
            m7.append(num)
        else:
            m6.append(num)
        e += 1
    m4 = []

    for num in m5:
        num += 8
        if num % 17 == 0:
            m0.append(num)
        else:
            m2.append(num)
        f += 1
    m5 = []

    for num in m6:
        num += 5
        if num % 19 == 0:
            m7.append(num)
        else:
            m1.append(num)
        g += 1
    m6 = []

    for num in m7:
        num += 3
        if num % 7 == 0:
            m1.append(num)
        else:
            m3.append(num)
        h += 1
    m7 = []

    i += 1
most = [a, b, c, d, e, f, g, h]
most.sort(reverse=True)
print(most[0]*most[1])
