from collections import deque
import time
import copy


def main():
    lines = [line.split() for line in open("2025/Inputs/test.txt").read().splitlines()]
    t = time.time()

    total_1 = solve_1(lines)
    total_2 = solve_2(lines)

    print(total_1)
    print(total_2)
    print(time.time()-t)


def solve_1(lines: list) -> int:
    total_1 = 0
    for line in lines:
        lights = line[0].strip("[]")
        lights = {i for i in range(len(lights)) if lights[i] == "#"}
        buttons = [list(map(int, button[1:-1].split(","))) for button in line[1:-1]]
        joltage = list(map(int, line[-1][1:-1].split(",")))

        length = len(buttons)
        bfs = deque([(set(), -1, 0)])
        while bfs:
            pattern, i, clicks = bfs.pop()

            for j in range(i+1, length):
                nxt = press_1(pattern.copy(), buttons[j])
                if nxt == lights:
                    total_1 += clicks+1
                    bfs = []
                    break
                bfs.appendleft((nxt, j, clicks+1))
    
    return total_1


def press_1(pattern: set, button: list) -> list:
    for light in button:
        if light in pattern:
            pattern.remove(light)
        else:
            pattern.add(light)
    return pattern


def solve_2(lines: list) -> int:
    total_2 = 0
    for line in lines:
        lights = line[0].strip("[]")
        lights = {i for i in range(len(lights)) if lights[i] == "#"}
        buttons = [list(map(int, button[1:-1].split(","))) for button in line[1:-1]]
        joltage = list(map(int, line[-1][1:-1].split(",")))

        total_2 += dfs([0]*len(joltage), joltage, buttons, 0)

    return total_2



def dfs(counters: list, joltage: list, buttons: list, clicks: int) -> int:
    if counters == joltage:
        return clicks
    
    low = float("inf")
    for button in buttons:
        check = press_2(counters.copy(), button, joltage)
        if check:
            n = dfs(check, joltage, buttons, clicks+1)
            if n < low:
                low = n
    
    return low
        
        
def press_2(counters: list, button: list, joltage: list) -> bool:
    for pos in button:
        if counters[pos] == joltage[pos]:
            return []
        counters[pos] += 1
    return counters


if __name__ == "__main__":
    main()