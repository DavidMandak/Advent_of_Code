import Intcode
import time

program = list(map(int, open("../Inputs/test.txt").read()[:-1].split(",")))


def find_1(phases, inp):
    global total
    if not phases and inp > total:
        total = inp
    for i in range(len(phases)):
        find_1(phases[:i]+phases[i+1:], Intcode.run(program[:], [phases[i], inp]))


t = time.time()
total = 0
find_1(list(range(5)), 0)
print(total)


def find_2(phases, inputs):
    global total
    if not phases:
        programs = [program[:] for _ in range(5)]
        pos = [[0] for _ in range(5)]
        out = 0
        while True:
            for i in range(5):
                inputs[i].append(out)
                try:
                    out = Intcode.run(programs[i], inputs[i], pos[i])
                except TypeError:
                    return
                inputs[i] = []
            if pos[-1][0] is None:
                if out > total:
                    total = out
                return
    for i in range(len(phases)):
        find_2(phases[:i]+phases[i+1:], inputs+[[phases[i]]])


total = 0
find_2(list(range(5, 10)), [])
print(total)
print(time.time()-t)
