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
        buttons = [button[1] for button in sorted(zip(list(map(len, buttons)), buttons))]
        joltage = list(map(int, line[-1][1:-1].split(",")))

        total_2 = s(joltage, buttons)
        #total_2 += dfs([0]*len(joltage), joltage, buttons, 0, len(buttons)-1)
        #total_2 += bfs(joltage, buttons)

    return total_2


def s(joltage: list, buttons: list) -> int:
    total_2 = 0
    length = len(joltage)
    buttons_pos = [[] for _ in range(length)]

    for _ in range(length):
        amount = min(joltage)
        pos = joltage.index(amount)
        joltage[pos] = float("inf")

        for i in range(len(buttons)-1, -1, -1):
            if pos in buttons[i]:
                buttons_pos[pos].append(buttons[i])

    stack = []
    print(buttons_pos)
    return total_2      


def dfs(counters: list, joltage: list, buttons: list, clicks: int, curr: int) -> int:
    if counters == joltage:
        return clicks
    
    for i in range(curr, -1, -1):
        button = buttons[i]
        check = press_2(counters.copy(), joltage, button)
        if check:
            n = dfs(check, joltage, buttons, clicks+1, i)
            if n:
                return n
    
    return 0


def bfs(joltage: list, buttons: list) -> int:
    bfs = deque([([0]*len(joltage), 0, len(buttons)-1)])
    while bfs:
        counters, clicks, curr = bfs.pop()

        if counters == joltage:
            return clicks
        
        for i in range(curr, -1, -1):
            button = buttons[i]
            check = press_2(counters.copy(), joltage, button)
            if check:
                bfs.appendleft((check, clicks+1, i))
    
    raise Exception


def press_2(counters: list, joltage: list, button: str) -> str:
    for pos in button:
        if counters[pos] == joltage[pos]:
            return []
        counters[pos] += 1

    return counters


if __name__ == "__main__":
    main()
