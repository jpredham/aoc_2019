"""
Intcode program syntax

'1 X Y Z'
Add ints at position X and Y, and store in position Z

'2 X Y Z'
Multiply ints at position X and Y, and store in position Z

'99'
Halt program
"""

import sys

def run_intcode_word(program, operation, x, y):
    if operation == 1:
        return program[x] + program[y]
    elif operation == 2:
        return program[x] * program[y]
    else:
        raise Exception("Unknown Operation " + operation)


def run_intcode_program(ops):
    cur = 0
    while ops[cur] != 99:
        val = run_intcode_word(ops, ops[cur], ops[cur+1], ops[cur+2])
        ops[ops[cur+3]] = val
        cur += 4
    return ops[0]


def main():
    input_file = sys.argv[1]
    prg = None
    with open(input_file, 'r') as f:
        prg = f.read()

    for noun in range(0, 99):
        for verb in range(0, 99):
            ops = [int(o) for o in prg.split(',')]
            ops[1] = noun
            ops[2] = verb
            output = run_intcode_program(ops)
            if output == 19690720:
                return 100 * noun + verb
    raise Exception("Intcode program terminated without finding answer")

print(main())
