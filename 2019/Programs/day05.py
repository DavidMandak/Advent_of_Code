import Intcode
program = list(map(int, open("../Inputs/Advent_of_Code_05.txt").read()[:-1].split(",")))

print(Intcode.run(program[:], [1]))
print(Intcode.run(program[:], [5]))
