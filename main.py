import numpy as np

from day.one import *


def call_day_one():
    input_data = np.loadtxt("input", dtype='i4')

    part_one = day_one_part_one(input_data)
    part_two = day_one_part_two(input_data)

    output_string = "Part one: " + str(part_one) + " Part two: " + str(part_two)

    return output_string


def main():
    print("Day One:")
    print(call_day_one())
    print("")


main()



