start, end = tuple(map(int, open("../Inputs/Advent_of_Code_04.txt").read()[:-1].split("-")))


def create(num, prev, rank):
    global total, done
    if rank == -1:
        num = str(num)
        for i in range(5):
            check = int(f"{num[:i]}{num[i]}{num[i:]}")
            if start <= check <= end and check not in done:
                done.append(check)
                total += 1
    else:
        for numeral in range(prev, 10):
            create(num+numeral*10**rank, numeral, rank-1)


def create_no_groups(num, prev, rank):
    global total, done
    if rank == -1:
        num = str(num)
        if num[0] == num[1]:
            last = num[0]
        else:
            last = None
        for i in range(5):
            if num[i] != last and (i == 4 or num[i] != num[i+1]):
                check = int(f"{num[:i]}{num[i]}{num[i:]}")
                if start <= check <= end and check not in done:
                    done.append(check)
                    total += 1
            last = num[i]
    else:
        for numeral in range(prev, 10):
            create_no_groups(num+numeral*10**rank, numeral, rank-1)


total = 0
done = []
for n in range(2, 7):
    create(n*10**4, n, 3)
print(total)
total = 0
done = []
for n in range(2, 7):
    create_no_groups(n*10**4, n, 3)
print(total)
