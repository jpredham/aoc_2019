import sys


def get_fuel_for_mass(mass):
    fuel = (mass / 3) - 2
    if fuel < 0:
        fuel = 0
    return fuel


def get_fuel_for_mass_improved(mass):
    fuel = get_fuel_for_mass(mass)
    fuel_for_fuel = get_fuel_for_mass(fuel)
    while fuel_for_fuel > 0:
        fuel += fuel_for_fuel
        fuel_for_fuel = get_fuel_for_mass(fuel_for_fuel)
    return fuel


def main():
    input_file = sys.argv[1]
    with open(input_file, 'r') as f:
        masses = (int(l.strip()) for l in f if l)
        fuels = (get_fuel_for_mass_improved(m) for m in masses)
        return sum(fuels)
    

print(main())
