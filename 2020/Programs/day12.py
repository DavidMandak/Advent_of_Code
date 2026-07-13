import time


def main():
    lines = open("Inputs/input12.txt").read().splitlines()
    t = time.time()

    total1 = solve1(lines)
    total2 = solve2(lines)

    print(total1)
    print(total2)
    print(time.time()-t)


def solve1(lines: list) -> int:
    x = 0
    y = 0
    rot = "E"
    roti = 1
    directions = {"N": (0, -1), "E":(1, 0), "S":(0, 1), "W":(-1, 0)}
    dirs = list(directions.keys())

    for line in lines:
        match line[0]:

            case "L":
                roti = (roti-int(line[1:])//90) % 4
                rot = dirs[roti]
            case "R":
                roti = (roti+int(line[1:])//90) % 4
                rot = dirs[roti]

            case "F":
                dis = int(line[1:])
                dx, dy = directions[rot]
                x += dx*dis
                y += dy*dis
           
            case default:
                dis = int(line[1:])
                dx, dy = directions[line[0]]
                x += dx*dis
                y += dy*dis          
    
    return abs(x)+abs(y)


def solve2(lines: list) -> int:
    x = 0
    y = 0
    wx = 10
    wy = -1
    directions = {"N": (0, -1), "E":(1, 0), "S":(0, 1), "W":(-1, 0)}

    for line in lines:
        match line[0]:

            case "L":
                for _ in range(int(line[1:])//90):
                    temp = -wx
                    wx = wy
                    wy = temp
            case "R":
                for _ in range(int(line[1:])//90):
                    temp = wx
                    wx = -wy
                    wy = temp

            case "F":
                dis = int(line[1:])
                x += wx*dis
                y += wy*dis
           
            case default:
                dis = int(line[1:])
                dx, dy = directions[line[0]]
                wx += dx*dis
                wy += dy*dis          
    
    return abs(x)+abs(y)


if __name__ == "__main__":
    main()
