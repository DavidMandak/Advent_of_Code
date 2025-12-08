import time
import heapq


def main():
    coordinates = [tuple(map(int, line.split(","))) for line in open("2025/Inputs/input08.txt").read().splitlines()]
    t = time.time()

    heap = find_lengths(coordinates)
    circuits = solve_1(heap.copy(), len(coordinates))
    total_1 = final_1(circuits)

    answer = solve_2(heap, len(coordinates))
    total_2 = final_2(coordinates, answer)
    
    print(total_1)
    print(total_2)
    print(time.time()-t)


def find_lengths(coordinates: list) -> list:
    heap = []
    size = len(coordinates)
    for i in range(size):
        x, y, z = coordinates[i]
        for j in range(i+1, size):
            a, b, circuit = coordinates[j]
            heapq.heappush(heap, (((x-a)**2+(y-b)**2+(z-circuit)**2)**(1/2), i, j))

    return heap


def solve_1(heap: list, size: int) -> list:
    circuits = []
    boxes = [None]*size
    for _ in range(10**3):
        d, i, j = heapq.heappop(heap)
        circuit_i = boxes[i]
        circuit_j = boxes[j]

        if circuit_i is None:
            if circuit_j is None:
                boxes[i] = boxes[j] = len(circuits)
                circuits.append(2)

            else:
                boxes[i] = circuit_j
                circuits[circuit_j] += 1

        else:
            if circuit_j is None:
                boxes[j] = circuit_i
                circuits[circuit_i] += 1

            else:
                if circuit_j != circuit_i:
                    length_i, length_j = circuits[circuit_i], circuits[circuit_j]

                    if  length_i <= length_j:
                        length = length_i
                        circuit = circuit_i
                        change = circuit_j
                        circuits[circuit_j] += length_i
                        circuits[circuit_i] = 0
                    else:
                        length = length_j
                        circuit = circuit_j
                        change = circuit_i
                        circuits[circuit_i] += length_j
                        circuits[circuit_j] = 0
                    
                    found = 0
                    k = 0
                    while found < length:
                        if boxes[k] == circuit:
                            boxes[k] = change
                            found += 1
                        k += 1

    return circuits


def final_1(circuits: list) -> int:
    high = [0]*3
    for cir in circuits:
        for hi in range(len(high)):
            if cir > high[hi]:
                high = sum([high[:hi]], sum([high[hi+1:]], [cir]))
                break

    total_1 = 1
    for n in high:
        total_1 *= n
    
    return total_1


def solve_2(heap:list, size: int) -> tuple:
    amount = size
    circuits = []
    boxes = [None]*size
    i = 0
    while amount > 1:
        d, i, j = heapq.heappop(heap)
        circuit_i = boxes[i]
        circuit_j = boxes[j]
        amount -= 1

        if circuit_i is None:
            if circuit_j is None:
                boxes[i] = boxes[j] = len(circuits)
                circuits.append(2)

            else:
                boxes[i] = circuit_j
                circuits[circuit_j] += 1

        else:
            if circuit_j is None:
                boxes[j] = circuit_i
                circuits[circuit_i] += 1

            else:
                if circuit_j != circuit_i:
                    length_i, length_j = circuits[circuit_i], circuits[circuit_j]

                    if  length_i <= length_j:
                        length = length_i
                        circuit = circuit_i
                        change = circuit_j
                        circuits[circuit_j] += length_i
                        circuits[circuit_i] = 0
                    else:
                        length = length_j
                        circuit = circuit_j
                        change = circuit_i
                        circuits[circuit_i] += length_j
                        circuits[circuit_j] = 0
                    
                    found = 0
                    k = 0
                    while found < length:
                        if boxes[k] == circuit:
                            boxes[k] = change
                            found += 1
                        k += 1
                else:
                    amount += 1
    
    return i, j
    
    
def final_2(coordinates: list, answer: tuple) -> int:
    i, j = answer
    total_2 = coordinates[i][0]*coordinates[j][0]
    return total_2


if __name__ == "__main__":
    main()
