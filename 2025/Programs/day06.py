import sys
import time

def main() -> tuple:
    total_1 = solve_1()
    total_2 = solve_2()

    return total_1, total_2

def setup_1() -> tuple:
    sys.stdin = open("2025/Inputs/input06.txt")

    numbers = []
    inp = input().split()
    while inp[0].isdigit():
        numbers.append(inp)
        inp = input().split()

    operators = inp

    return numbers, operators


def solve_1() -> int:
    numbers, operators = setup_1()

    total_1 = 0
    for i in range(len(operators)):
        ans = ""
        operator = operators[i]

        for line in numbers:
            ans += line[i]+operator

        total_1 += eval(ans[:-1])
    return total_1


def setup_2() -> tuple:
    sys.stdin = open("2025/Inputs/input06.txt")

    lines = []
    inp = input()
    while inp.strip()[0].isdigit():
        lines.append(inp)
        inp = input()

    operators_line = inp

    return lines, operators_line


def solve_2():
    lines, operators_line = setup_2()

    total_2 = 0
    numbers = [[] for _ in range(len(lines))]
    curr = 0
    width = len(operators_line)
    height = len(lines)
    while curr < width:
        ans = ""
        operator = operators_line[curr]

        nxt = curr+2
        while True:
            if nxt >= width:
                nxt = width+1
                break
            elif operators_line[nxt] != " ":
                break
            nxt += 1
            
        for n in range(curr, nxt-1):
            for i in range(height):
                num = lines[i][n]
                if num != " ":
                    ans += num
            ans += operator

        total_2 += eval(ans[:-1])
        curr = nxt
    
    return total_2

if __name__ == "__main__":
    t = time.time()
    total_1, total_2 = main()
    print(total_1)
    print(total_2)
    print(time.time()-t)
