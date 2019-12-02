import numpy as np

from day.one import *
import unittest


class TestDayOnePartOne(unittest.TestCase):
    def test_part_one(self):
        input_data = np.loadtxt("testData.txt", dtype='i4')
        output = day_one_part_one(input_data)

        self.assertEqual(output, 34237)


class TestDayOnePartTwo(unittest.TestCase):
    def test_part_two(self):
        input_data = np.loadtxt("testData.txt", dtype='i4')
        output = day_one_part_two(input_data)

        self.assertEqual(output, 51312)


if __name__ == '__main__':
    unittest.main()
