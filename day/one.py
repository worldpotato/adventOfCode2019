import numpy as np


def day_one_part_one(input_data):

    divided_and_floor = input_data // 3
    subtracted = np.subtract(divided_and_floor,2)
    sum_of_all = np.sum(subtracted)

    return sum_of_all


def calc_required_fuel(mass):
    required_fuel = mass//3 - 2
    if required_fuel <= 0:
        return 0
    else:
        return calc_required_fuel(required_fuel) + required_fuel


def day_one_part_two(input_data):
    single_required_fuel = []
    for fuel in input_data:
        required_fuel = calc_required_fuel(fuel)
        single_required_fuel.append(required_fuel)
    return np.sum(single_required_fuel)
