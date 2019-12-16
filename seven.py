"""
Day 7: Amplifiers

Five amplifiers. Each has two inputs: an input signal and a phase setting.

The first amplifier's input signal is 0, but all subsequent inputs are the
output from the previous amplifier.

Each "phase setting" is an input (0-4) that is used only once.

Trying to find the sequence of phase settings that yield the highest output.
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
        

def run_intcode_program(ops, input_stack):
    i = 0
    ptr_modified = False
    output_stack = []
    while i < len(ops):
        modes, func, size = get_instruction(ops[i])
        # print(f"Modes: {modes} Function: {func}")
        if func == "exit":
            return output_stack
        elif func == "out":
            val = get_val(ops, modes, i, 1)
            print(f"Outputting {val}")
            output_stack.append(val)
            input_stack.append(val)
        elif func == "in_op":
            #val = int(input())
            val = input_stack.pop()
            print(f"Consuming {val}")
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

    raise Exception("Program terminated early")

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


def get_program_text(input_file):
    prg = None
    with open(input_file, 'r') as f:
        prg = f.read()
    return prg


def get_ops(prg):
    return [int(o) for o in prg.split(',')]


def run_amplifiers(prg, initial_input, phase_sequence):
    input_signal = initial_input
    input_stack = [input_signal]
    for i, phase in enumerate(phase_sequence):
        ops = get_ops(prg)
        input_stack.append(phase)
        print(f"Round {i+1} Input: {input_stack}")
        output = run_intcode_program(ops, input_stack)
        print(f"Output: {output}, remaining input: {input_stack}")

    return input_stack.pop()


def generate_phase_sequences():
    for i in range(5, 10):
        for ii in [x for x in range(5, 10) if x != i]:
            for iii in [x for x in range(5, 10) if x != i and x != ii]:
                for iv in [x for x in range(5, 10) if x != i and x != ii and x != iii]:
                    for v in [x for x in range(5, 10) if x != i and x != ii and x != iii and x != iv]:
                        yield [i, ii, iii, iv, v]


def main():
    prg = get_program_text(sys.argv[1])
    max_output = -1
    max_seq = None
    input_signal = 0

    output = run_amplifiers(prg, input_signal, [9,8,7,6,5])
    print(f"Output: {output}")

    # output = run_amplifiers(prg, output, [9,8,7,6,5])
    # print(f"Output: {output}")

    # output = run_amplifiers(prg, output, [9,8,7,6,5])
    # print(f"Output: {output}")
    
    # for seq in generate_phase_sequences():
    #     output = run_amplifiers(prg, input_signal, seq)
    #     if output > max_output:
    #         max_output = output
    #         max_seq = seq
    # print(f"Max Output: {max_output} with sequence: {max_seq}")
    

main()
