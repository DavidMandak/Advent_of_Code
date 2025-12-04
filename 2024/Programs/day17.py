import time

registers, program = open("2024/Inputs/input17.txt").read().split("\n\n")
registers = registers.splitlines()
for i in range(3):
    registers[i] = int(registers[i].split(": ")[1])
check = program.split(": ")[1][:-1]
program = list(map(int, program.split(": ")[1].split(",")))


def adv(operand, register):
    global registers
    combo_operand = operand if operand <= 3 else registers[operand-4]
    registers[register] = registers[0]//(2**combo_operand)


def bxl(operand):
    global registers
    registers[1] = registers[1] ^ operand


def bst(operand):
    global registers
    combo_operand = operand if operand <= 3 else registers[operand-4]
    registers[1] = combo_operand % 8


def jnz(operand):
    global registers, pos
    if registers[0] != 0:
        pos = operand-2

def bxc():
    global registers
    registers[1] = registers[1] ^ registers[2]


def out(operand):
    global registers, output
    combo_operand = operand if operand <= 3 else registers[operand-4]
    output += str(combo_operand % 8)+","


t = time.time()
output = ""
pos = 0
while pos < len(program):
    instruction = program[pos]
    oper = program[pos+1]
    if instruction == 1:
        bxl(oper)
    elif instruction == 2:
        bst(oper)
    elif instruction == 3:
        jnz(oper)
    elif instruction == 4:
        bxc()
    elif instruction == 5:
        out(oper)
    else:
        adv(oper, instruction % 5)
    pos += 2
print(output[:-1])

a = 0
i = 1
sequences = []
seq = ""
while output[:-1] != check:
    registers = [a, 0, 0]
    output = ""
    pos = 0
    while pos < len(program):
        instruction = program[pos]
        oper = program[pos+1]
        if instruction == 1:
            bxl(oper)
        elif instruction == 2:
            bst(oper)
        elif instruction == 3:
            jnz(oper)
        elif instruction == 4:
            bxc()
        elif instruction == 5:
            out(oper)
        else:
            adv(oper, instruction % 5)
        pos += 2
    if output[:-1] == check[len(check)-len(output)+1:]:
        a = int(oct(a)+"0", 8)
        continue
    a += 1
print(int(oct(a)[:-1], 8))
print(time.time()-t)
