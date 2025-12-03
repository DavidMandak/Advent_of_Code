def run(program, inp=None, start=None):
    if not start:
        start = [0]
    pos = start[0]
    inp_i = 0
    out = None
    while pos < len(program):
        modes, opcode = setup(program[pos])
        match opcode:
            case 1:
                a = get(program, pos+1, modes[0])
                b = get(program, pos+2, modes[1])
                c = program[pos+3]
                program[c] = a+b
                pos += 4
            case 2:
                a = get(program, pos+1, modes[0])
                b = get(program, pos+2, modes[1])
                c = program[pos+3]
                program[c] = a*b
                pos += 4
            case 3:
                if inp_i < len(inp):
                    c = program[pos+1]
                    program[c] = inp[inp_i]
                    inp_i += 1
                    pos += 2
                else:
                    start[0] = pos
                    return out
            case 4:
                a = get(program, pos+1, modes[0])
                out = a
                pos += 2
            case 5:
                a = get(program, pos+1, modes[0])
                b = get(program, pos+2, modes[1])
                if a:
                    pos = b
                else:
                    pos += 3
            case 6:
                a = get(program, pos+1, modes[0])
                b = get(program, pos+2, modes[1])
                if not a:
                    pos = b
                else:
                    pos += 3
            case 7:
                a = get(program, pos+1, modes[0])
                b = get(program, pos+2, modes[1])
                c = program[pos+3]
                program[c] = 1 if a < b else 0
                pos += 4
            case 8:
                a = get(program, pos+1, modes[0])
                b = get(program, pos+2, modes[1])
                c = program[pos+3]
                program[c] = 1 if a == b else 0
                pos += 4
            case 99:
                start[0] = None
                return out


def setup(instr):
    op = instr % 100
    mod = []
    instr = str(instr)
    length = len(instr)
    for i in range(-3, -5, -1):
        if -i > length:
            mod.append(0)
        else:
            mod.append(int(instr[i]))
    return mod, op


def get(program, pos, mode):
    parameter = program[pos]
    match mode:
        case 0:
            return program[parameter]
        case 1:
            return parameter
    exit("Invalid mode")
