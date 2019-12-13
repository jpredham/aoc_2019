"""
Day 6: Orbit maps
"""

import sys



def orbital_distance(orbits, start, dest):
    # index parent relationships
    parents = {orbiter: orbitee for orbitee, orbiter in orbits}
    dest_parents = set()
    tmp = parents[dest]
    while tmp in parents:
        tmp = parents[tmp]
        dest_parents.add(tmp)

    hops = 0
    traveler = parents[start]
    while traveler not in dest_parents:
        traveler = parents[traveler]
        hops += 1

    # at this point traveler is the nearest ancestor between start and dest
    tmp = parents[dest]
    while tmp != traveler:
        tmp = parents[tmp]
        hops += 1

    return hops
    


def checksum(orbits):
    # index parent relationships
    parents = {orbiter: orbitee for orbitee, orbiter in orbits}

    direct = 0
    indirect = 0

    for orbitee, orbiter in orbits:
        direct += 1
        tmp = orbitee
        while tmp in parents:
            indirect += 1
            tmp = parents[tmp]

    return direct + indirect


def main():
    input_file = sys.argv[1]
    orbits_raw = None
    with open(input_file, 'r') as f:
        orbits_raw = f.readlines()
    orbits = [o.strip().split(')') for o in orbits_raw]
    dist = orbital_distance(orbits, "YOU", "SAN")
    print(dist)

main()
