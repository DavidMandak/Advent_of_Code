import time


def main():
    lines = open("Inputs/input05.txt").read().splitlines()
    t = time.time()

    total1, total2 = solve(lines)

    print(total1)
    print(total2)
    print(time.time()-t)


def solve(lines: list) -> int:
    grid = [None]*85+[0]*799

    high = 0
    for seat in lines:
        sid = 0

        for i in range(7):
            if seat[i] == "B":
                sid += 2**(7-i-1)*8

        for i in range(7, 10):
            if seat[i] == "R":
                sid += 2**(10-i-1)
        
        if sid > high:
            high = sid
        
        grid[sid] = 1
    
    return high, grid.index(0)


if __name__ == "__main__":
    main()
