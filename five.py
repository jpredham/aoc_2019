"""
Day 5
Intcode program ++

'1 X Y Z'
Add ints at position X and Y, and store in position Z

'2 X Y Z'
Multiply ints at position X and Y, and store in position Z

'99'
Halt program

'3 X'
Take an "input" and store it at position X

'4 X'
"Output" the value at position x

'5 X Y'
"Jump if true" - if X != 0, set ptr to Y

'6 X Y'
"Jump if false" - if X == 0, set ptr to Y

'7 X Y Z'
"Less than" - if X < Y, store 1 in Z, otherwise store 0 in Z

'8 X Y Z'
"Equals" - if X == Y, store 1 in Z, otherwise store 0 in Z


"""

import sys


def get_val(ops, modes, ptr, offset):
    mode = "pos"
    if offset == 1 and modes % 10 == 1:
        mode = "imm"
    elif offset == 2 and int(modes / 10) == 1:
        mode = "imm"

    if mode == "pos":
        return ops[ops[ptr+offset]]
    else:
        return ops[ptr+offset]
        

def run_intcode_program(ops):
    i = 0
    ptr_modified = False
    while i < len(ops):
        modes, func, size = get_instruction(ops[i])
        # print(f"Modes: {modes} Function: {func}")
        if func == "exit":
            raise Exception("Finished")
        elif func == "out":
            print(get_val(ops, modes, i, 1))
        elif func == "in_op":
            val = int(input())
            ops[ops[i+1]] = val
        elif func == "add":
            val = get_val(ops, modes, i, 1) + get_val(ops, modes, i, 2)
            ops[ops[i+3]] = val
        elif func == "mult":
            val = get_val(ops, modes, i, 1) * get_val(ops, modes, i, 2)
            ops[ops[i+3]] = val
        elif func == "jump-true":
            if get_val(ops, modes, i, 1) != 0:
                i = get_val(ops, modes, i, 2)
                ptr_modified = True
        elif func == "jump-false":
            if get_val(ops, modes, i, 1) == 0:
                i = get_val(ops, modes, i, 2)
                ptr_modified = True
        elif func == "lt":
            store = 0
            if get_val(ops, modes, i, 1) < get_val(ops, modes, i, 2):
                store = 1
            ops[ops[i+3]] = store
        elif func == "eq":
            store = 0
            if get_val(ops, modes, i, 1) == get_val(ops, modes, i, 2):
                store = 1
            ops[ops[i+3]] = store

        if not ptr_modified:
            i += size
        else:
            ptr_modified = False


def get_instruction(x):
    """Modes, function, word size"""
    modes = int(x / 100)
    op = x % 10
    if op == 1:
        return modes, "add", 4
    elif op == 2:
        return modes, "mult", 4
    elif op == 3:
        return modes, "in_op", 2
    elif op == 4:
        return modes, "out", 2
    elif op == 5:
        return modes, "jump-true", 3
    elif op == 6:
        return modes, "jump-false", 3
    elif op == 7:
        return modes, "lt", 4
    elif op == 8:
        return modes, "eq", 4
    elif x == 99 or op == 99:
        return modes, "exit", 1
    else:
        raise Exception(f"Unknown Operation {x}")


def main():
    input_file = sys.argv[1]
    prg = None
    with open(input_file, 'r') as f:
        prg = f.read()
    ops = [int(o) for o in prg.split(',')]
    run_intcode_program(ops)

main()
