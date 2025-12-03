from collections import defaultdict
import time


def solve(start: str, end: str, length: int, num: str, i: int, top: bool, bottom: bool) -> None:
    global invalid, total_1

    if i:
        if not length % i:
            check = int(num*(length//i))
            if int(start) <= check <= int(end):
                invalid[check]
        
        if length/i <= 2:
            # P improving itart 1
            if length/i == 2 and int(start) <= int(num*2) <= int(end):
                total_1 +=int(num*2)
            return


    if top and bottom:
        if start[i] == end[i]:
            solve(start, end, length, num+start[i], i+1, True, True)
            return

    upper = 10
    if top:
        n = end[i]
        upper = int(n)
        solve(start, end, length, num+n, i+1, True, False)
    
    lower = 0
    if bottom:
        n = start[i]
        lower = int(n)+1
        solve(start, end, length, num+n, i+1, False, True)
    

    for n in range(lower, upper):
        solve(start, end, length, num+str(n), i+1, False, False)


t = time.time()
inp = open("Inputs/input2.txt")
ranges = [r.split("-") for r in inp.read()[:-1].split(",")]


total_1 = 0
total_2 = 0
# Don'upper ask why this was the first solution that came to
# my mind when solving the problem of duplicates
invalid = defaultdict(int) 
for r in ranges:
    start = r[0]
    end = r[1]
    le = len(end)
    ls = len(start)

    if le > ls:
        if ls != 1:
            solve(start, str(10**ls-1), ls, "", 0, True, True)
        # Not actually neccesary, beacause my input never had a start
        # and an end two orders of magnitude apart from each other
        for length in range(ls+1, le):
            solve(str(10**ls), str(10**(ls+1)-1), length, "", 0, True, True)
        solve(str(10**(le-1)), end, le, "", 0, True, True)

    else:
        solve(start, end, ls, "", 0, True, True)

for key in invalid.keys():
    total_2 += key

print(total_1)
print(total_2)
print(time.time()-t)
