import time
from collections import defaultdict


def main() -> None:
    lines = [line.split() for line in open("2025/Inputs/test.txt").read().splitlines()]
    t = time.time()

    nodes_1 = setup_1(lines)
    total_1 = solve_1(nodes_1)

    nodes_2 = setup_2(lines)
    total_2 = solve_2(nodes_1, nodes_2, len(lines))

    print(total_1)
    print(total_2)
    print(time.time()-t)


def setup_1(lines: list) -> dict:
    nodes = {}
    for line in lines:
        nodes[line[0][:-1]] = line[1:]
    
    return nodes


def solve_1(nodes: dict) -> int:
    return
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


def solve_2(nodes_1: dict, nodes_2: dict, length: int) -> int:
    total_2 = 1

    paths = defaultdict(int)
    dfs_2("svr", nodes_1, paths)
    total_2 *= dfs_2_back("fft", nodes_2, paths)+1
    #print(paths)

    paths = defaultdict(int)
    dfs_2("fft", nodes_1, paths)
    total_2 *= dfs_2_back("dac", nodes_2, paths)+1
    #print(paths)
    print()

    paths = defaultdict(int)
    dfs_2("dac", nodes_1, paths)
    print(paths)
    total_2 *= dfs_2_back("out", nodes_2, paths)+1

    return total_2


def dfs_2(curr: str, nodes: dict, paths: dict) -> None:
    paths[curr] += 1
    if paths[curr] != 1:
        return
    elif curr == "out":
        return
    
    for node in nodes[curr]:
        dfs_2(node, nodes, paths)


def dfs_2_back(curr: str, nodes: dict, paths: dict) -> int:
    if paths[curr]:
        a = [dfs_2_back(node,  nodes, paths) for node in nodes[curr]]
        print(curr)
        print(a)
        print(paths[curr]+sum(a)-1)
        return paths[curr]+sum(a)-1
    return 0


if __name__ == "__main__":
    main()
