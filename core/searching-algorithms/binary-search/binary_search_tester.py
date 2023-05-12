# Author: Reza Khojasteh
# Date: 2023-01-23
# Description: A unit test to test the binary search algorithm

# This is a unit test composed of different test cases to check the correctness of the the binary_search function in the binary_search.py file (in the same directory)
# the test cases cover all the possible scenarios, including the best case, the worst case, and the average case
# the test cases also cover the edge cases, such as an empty list, a list with one element, a list with two elements, and a list with three elements
# the test cases also cover the edge cases, such as a list with duplicate elements, a list with negative elements, a list with floating point numbers, and a list with strings


import unittest
from binary_search import binary_search


class TestBinarySearch(unittest.TestCase):
    def test_empty_list(self):
        list = []
        self.assertEqual(binary_search(list, 1), -1)

    def test_one_element_list(self):
        list = [1]
        self.assertEqual(binary_search(list, 1), 0)

    def test_two_element_list(self):
        list = [1, 2]
        self.assertEqual(binary_search(list, 1), 0)
        self.assertEqual(binary_search(list, 2), 1)

    def test_three_element_list(self):
        list = [1, 2, 3]
        self.assertEqual(binary_search(list, 1), 0)
        self.assertEqual(binary_search(list, 2), 1)
        self.assertEqual(binary_search(list, 3), 2)

    def test_list_with_duplicate_elements(self):
        list = [1, 1, 2, 2, 3, 3]
        self.assertEqual(binary_search(list, 1), 0)
        self.assertEqual(binary_search(list, 2), 2)
        self.assertEqual(binary_search(list, 3), 4)

    def test_list_with_negative_elements(self):
        list = [-5, -4, -3, -2, -1]
        self.assertEqual(binary_search(list, -5), 0)
        self.assertEqual(binary_search(list, -4), 1)
        self.assertEqual(binary_search(list, -3), 2)
        self.assertEqual(binary_search(list, -2), 3)
        self.assertEqual(binary_search(list, -1), 4)

    def test_list_with_floating_point_numbers(self):
        list = [1.1, 2.2, 3.3, 4.4, 5.5]
        self.assertEqual(binary_search(list, 1.1), 0)
        self.assertEqual(binary_search(list, 2.2), 1)
        self.assertEqual(binary_search(list, 3.3), 2)
        self.assertEqual(binary_search(list, 4.4), 3)
        self.assertEqual(binary_search(list, 5.5), 4)

    def test_list_with_strings(self):
        list = ['a', 'b', 'c', 'd', 'e']
        self.assertEqual(binary_search(list, 'a'), 0)
        self.assertEqual(binary_search(list, 'b'), 1)
        self.assertEqual(binary_search(list, 'c'), 2)
        self.assertEqual(binary_search(list, 'd'), 3)
        self.assertEqual(binary_search(list, 'e'), 4)

    def test_best_case(self):
        list = [1, 2, 3, 4, 5]
        self.assertEqual(binary_search(list, 3), 2)

    def test_worst_case(self):
        list = [1, 2, 3, 4, 5]
        self.assertEqual(binary_search(list, 6), -1)

    def test_average_case(self):
        list = [1, 2, 3, 4, 5]
        self.assertEqual(binary_search(list, 4), 3)


if __name__ == '__main__':
    unittest.main()
