"""
Day 3: Crossed Wires
"""

import sys


def get_end_point(xs, ys, tok):
    dir = tok[:1]
    length = int(tok[1:])
    if dir == 'U':
        return xs, ys + length
    elif dir == 'D':
        return xs, ys - length
    elif dir == 'L':
        return xs - length, ys
    elif dir == 'R':
        return xs + length, ys
    else:
        raise Exception("Bad token direction")


def get_intersection(line_1, line_2):
    xs1, ys1, xn1, yn1 = line_1
    xs2, ys2, xn2, yn2 = line_2

    # line 1: (8, 5) - (3, 5)
    # line 2: (6, 7) - (6, 3)

    # Rule out parallel lines (can't intersect)
    if xs1 == xn1 and xs2 == xn2:
        return None
    if ys1 == yn1 and ys2 == yn2:
        return None
    
    if xs1 <= xs2 <= xn1 or xn1 <= xs2 <= xs1:
        if ys2 <= ys1 <= yn2 or yn2 <= ys1 <= ys2:
            return xs2, ys1

    if xs2 <= xs1 <= xn2 or xn2 <= xs1 <= xs2:
        if ys1 <= ys2 <= yn1 or yn1 <= ys2 <= ys1:
            return xs1, ys2

    return None


def generate_lines(wire):
    xs, ys = 0, 0
    for tok in wire:
        xn, yn = get_end_point(xs, ys, tok)
        yield xs, ys, xn, yn
        xs, ys = xn, yn


def generate_steps(line):
    xs, ys, xn, yn = line
    xc, yc = xs, ys
    while xc != xn or yc != yn:
        if xc < xn:
            xc, yc = xc + 1, yc
        elif xc > xn:
            xc, yc = xc - 1, yc
        elif yc < yn:
            xc, yc = xc, yc + 1
        else:
            xc, yc = xc, yc -1
        yield xc, yc


def steps_to_intersection(intx, line):
    intx_x, intx_y = intx
    steps = 0
    for x, y in generate_steps(line):
        steps += 1
        if x == intx_x and y == intx_y:
            print(f"Line {line} steps: {steps}")
            return steps
    print(f"Line {line} steps: {steps}")
    return steps


def line_length(line):
    xs, ys, xn, yn = line
    if xs < xn:
        return xn - xs
    elif xs > xn:
        return xs - xn
    elif ys < yn:
        return yn - ys
    else:
        return ys - yn


def get_steps_for_intersection(intx, wire):
    step_sum = 0
    for line in generate_lines(wire):
        steps = steps_to_intersection(intx, line)
        step_sum += steps
        if steps < line_length(line):
            return step_sum
    return step_sum


def find_all_intersections(wire_1, wire_2):
    """Points = (x, y)"""
    intxs = []
    for line_1 in generate_lines(wire_1):
        for line_2 in generate_lines(wire_2):
            intx = get_intersection(line_1, line_2)
            if intx:
                wire_1_steps = get_steps_for_intersection(intx, wire_1)
                wire_2_steps = get_steps_for_intersection(intx, wire_2)
                print(f"Steps for intx {intx}: {wire_1_steps + wire_2_steps}")
                intxs.append((intx, wire_1_steps + wire_2_steps))
    return intxs


def get_dist_for_intx(intx):
    x, y = intx
    return abs(x) + abs(y)


def find_shortest_distance(intersections):
    dists = sorted([get_dist_for_intx(intx) for intx in intersections])
    if dists[0] == 0:
        dists = dists[1:]
    return dists[0]


def get_shortest_steps(intxs):
    steps = sorted([s for intx, s in intxs])
    print(steps)
    if steps[0] == 0:
        steps = steps[1:]
    return steps[0]


def main():
    input_file = sys.argv[1]
    wire_1 = None
    wire_2 = None
    
    with open(input_file, 'r') as f:
        wire_1 = [t.strip() for t in f.readline().split(',')]
        wire_2 = [t.strip() for t in f.readline().split(',')]
        
    intxs = find_all_intersections(wire_1, wire_2)
    answer = get_shortest_steps(intxs)
    return answer

print(main())
