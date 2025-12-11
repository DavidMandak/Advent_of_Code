import time
from collections import defaultdict


def main() -> None:
    lines = [line.split() for line in open("2025/Inputs/input11.txt").read().splitlines()]
    t = time.time()

    nodes_1 = setup_1(lines)
    total_1 = solve_1(nodes_1)

    nodes_2 = setup_2(lines)
    total_2 = solve_2(nodes_1)

    print(total_1)
    print(total_2)
    print(time.time()-t)


def setup_1(lines: list) -> dict:
    nodes = {}
    for line in lines:
        nodes[line[0][:-1]] = line[1:]
    
    return nodes


def solve_1(nodes: dict) -> int:
    total_1 = dfs_1("you", nodes)

    return total_1


def dfs_1(curr: str, nodes: dict) -> int:
    if curr == "out":
        return 1
    
    return sum([dfs_1(node, nodes) for node in nodes[curr]])


def setup_2(lines: list) -> dict:
    nodes = defaultdict(list)
    for line in lines:
        for node in line[1:]:
            nodes[node].append(line[0][:-1])
    
    return nodes


def solve_2(nodes: dict) -> int:
    total_2 = dfs_2("svr", nodes, False)


def dfs_2(curr: str, nodes: dict, dac: bool) -> int:
    if curr == "dac":
        if dac:
            raise Exception
        dac = True
    elif curr == "out":
        return 0
    
    return sum([dfs_2(node, nodes, dac) for node in nodes[curr]])



if __name__ == "__main__":
    main()
