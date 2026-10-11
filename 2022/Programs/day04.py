lines = open("04.txt").readlines()
a = 0
for line in lines:
    if line[1] != "-":
        w = line[0]+line[1]
        x = line[3]+line[4]
        if line[7] != "-":
            y = line[6]+line[7]
            z = line[9]+line[10]
        else:
            y = line[6]
            if line[9] != "\\n":
                z = line[8]+line[9]
            else:
                z = line[8]
    else:
        w = line[0]
        if line[3] != ",":
            x = line[2]+line[3]
            if line[6] != "-":
                y = line[5]+line[6]
                z = line[8]+line[9]
            else:
                y = line[5]
                if line[8] != "\\n":
                    z = line[7]+line[8]
                else:
                    z = line[7]
        else:
            x = line[2]
            if line[5] != "-":
                y = line[4]+line[5]
                z = line[7]+line[8]
            else:
                y = line[4]
                if line[7] != "\\n":
                    z = line[6]+line[7]
                else:
                    z = line[6]
    if int(w) <= int(y) and int(x) >= int(z):
        a += 1
    elif int(y) <= int(w) and int(z) >= int(x):
        a += 1
    w = x = y = z = 0
print(a)
a = 0
for line in lines:
    if line[1] == "-":
        w = line[0]
        if line[3] == ",":
            x = line[2]
            if line[5] == "-":
                y = line[4]
                if line[7] == "\\n":
                    z = line[6]
                else:
                    z = line[6]+line[7]
            else:
                y = line[4]+line[5]
                z = line[7]+line[8]
        else:
            x = line[2]+line[3]
            if line[6] == "-":
                y = line[5]
                if line[8] == "\\n":
                    z = line[7]
                else:
                    z = line[7]+line[8]
            else:
                y = line[5]+line[6]
                z = line[8]+line[9]
    elif line[2] == "-":
        w = line[0]+line[1]
        x = line[3]+line[4]
        if line[7] == "-":
            y = line[6]
            if line[9] == "\\n":
                z = line[8]
            else:
                z = line[8]+line[9]
        else:
            y = line[6]+line[7]
            z = line[9]+line[10]
    else:
        continue
    if int(w) <= int(y) and int(x) >= int(z) or int(y) <= int(w) and int(z) >= int(x):
        print(str(w) + "-" + str(x) + "," + str(y) + "-" + str(z))
        a += 1
    elif int(w) <= int(y) <= int(x) <= int(z) or int(y) <= int(w) <= int(z) <= int(x):
        print(str(w) + "-" + str(x) + "," + str(y) + "-" + str(z))
        a += 1
    w = x = y = z = 0
print(a)
