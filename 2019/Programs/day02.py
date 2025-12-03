import Intcode
program = list(map(int, open("../Inputs/Advent_of_Code_02.txt").read()[:-1].split(",")))
program[1], program[2] = 12, 2
save = program[:]

Intcode.run(program)
print(program[0])
for noun in range(99):
    for verb in range(99):
        program = save[:]
        program[1], program[2] = noun, verb
        Intcode.run(program)
        if program[0] == 19690720:
            print(100*noun+verb)
            exit()
