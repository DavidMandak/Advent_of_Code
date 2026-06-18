import time


def main():
    #print(sum([len(set(group))-1 for group in open("Inputs/input06.txt").read().split("\n\n")])+1)
    #print(sum([len(eval(str(group)[1:-1].replace("},", "} &"))) for group in [list(map(set, g.split())) for g in open("Inputs/input06.txt").read().split("\n\n")]]))
    lines = open("Inputs/input06.txt").read().split("\n\n")
    t = time.time()

    total1, total2 = solve(lines)

    print(total1)
    print(total2)
    print(time.time()-t)


def solve(lines: list) -> int:
    total1 = sum([len(set(group))-1 for group in lines])+1
    total2 = sum([len(eval(str(group)[1:-1].replace("},", "} &"))) for group in [list(map(set, g.split())) for g in lines]])

    return total1, total2


if __name__ == "__main__":
    main()
