import time


def main():
    lines = [line.split() for line in open("Inputs/input08.txt").read().splitlines()]
    t = time.time()

    total1 = solve1(lines)
    total2 = solve2(lines)

    print(total1)
    print(total2)
    print(time.time()-t)


def solve1(lines: list) -> int:
    visited = [False]*len(lines)
    pos = 0
    acc = 0
    while not visited[pos]:
        visited[pos] = True
        ins, val = lines[pos]

        match ins:
            case "jmp":
                pos += int(val)-1
            case "acc":
                acc += int(val)
        pos += 1

    return acc


def solve2(lines: list) -> int:
    length = len(lines)
    visited = [False]*length
    pos = 0
    acc = 0
    stack = []
    while not visited[pos]:
        visited[pos] = True
        stack.append(pos)
        ins, val = lines[pos]

        match ins:
            case "jmp":
                pos += int(val)-1
            case "acc":
                acc += int(val)
        pos += 1
    
    i = 0
    while True:
        i += 1
        pos = stack.pop()
        ins, val = lines[pos]
        while ins == "acc":
            acc -= int(val)
            pos = stack.pop()
            ins, val = lines[pos]
        
        #Save if the fix is wrong
        save = (pos, acc, visited.copy())

        #Fix
        match ins:
            case "nop":
                pos += int(val)
            case "jmp":
                pos += 1

        #Check if the fix is right
        while not visited[pos]:
            visited[pos] = True
            ins, val = lines[pos]

            match ins:
                case "jmp":
                    pos += int(val)-1
                case "acc":
                    acc += int(val)
            pos += 1

            if pos == length:
                return acc

        pos, acc, visited = save



if __name__ == "__main__":
    main()
