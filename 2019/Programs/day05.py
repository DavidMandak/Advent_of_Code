import Intcode
program = list(map(int, open("2019/Inputs/input05.txt").read()[:-1].split(",")))

print(Intcode.run(program[:], [1]))
print(Intcode.run(program[:], [5]))
