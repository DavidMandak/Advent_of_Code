import time

def maximum(array: list) -> tuple:
    high = 0
    high_i = None
    for i in range(len(array)):
        num = array[i]
        if num > high:
            high = num
            high_i = i
    return high, high_i



def solve(lines: list, n: int) -> int:
    total = 0
    for line in lines:
        length = len(line)
        num_i = -1
        range_i = 0
        for i in range(1, n+1):
            num, num_i = maximum(line[range_i:length-(n-i)])
            range_i += num_i+1
            total += num*10**(n-i)
    return total




if __name__ == "__main__":
    t = time.time()
    lines = [list(map(int, list(line))) for line in open("2025/Inputs/input03.txt").read().splitlines()]
    total_1 = solve(lines, 2)
    total_2 = solve(lines, 12)
    print(total_1)
    print(total_2)
    print(time.time()-t)

