# Author: Reza Khojasteh
# Date: 2023-01-30
# Description: A unit test to test the quick sort algorithm

# This is a unit test composed of different test cases to check the correctness of the the quick_sort function in the quick_sort.py file (in the same directory)
# the test cases cover all the possible scenarios, including the best case, the worst case, and the average case
# the test cases also cover the edge cases, such as an empty list, a list with one element, a list with two elements, and a list with three elements
# the test cases also cover the edge cases, such as a list with duplicate elements, a list with negative elements, a list with floating point numbers, and a list with strings

import unittest
from quick_sort import quick_sort


class TestQuickSort(unittest.TestCase):
    def test_empty_list(self):
        list = []
        quick_sort(list)
        self.assertEqual(list, [])

    def test_one_element_list(self):
        list = [1]
        quick_sort(list)
        self.assertEqual(list, [1])

    def test_two_element_list(self):
        list = [2, 1]
        quick_sort(list)
        self.assertEqual(list, [1, 2])

    def test_three_element_list(self):
        list = [3, 2, 1]
        quick_sort(list)
        self.assertEqual(list, [1, 2, 3])

    def test_list_with_duplicate_elements(self):
        list = [1, 2, 3, 3, 2, 1]
        quick_sort(list)
        self.assertEqual(list, [1, 1, 2, 2, 3, 3])

    def test_list_with_negative_elements(self):
        list = [-1, -2, -3, -4, -5]
        quick_sort(list)
        self.assertEqual(list, [-5, -4, -3, -2, -1])

    def test_list_with_floating_point_numbers(self):
        list = [1.1, 2.2, 3.3, 4.4, 5.5]
        quick_sort(list)
        self.assertEqual(list, [1.1, 2.2, 3.3, 4.4, 5.5])

    def test_list_with_strings(self):
        list = ["a", "b", "c", "d", "e"]
        quick_sort(list)
        self.assertEqual(list, ["a", "b", "c", "d", "e"])

    def test_best_case(self):
        list = [1, 2, 3, 4, 5]
        quick_sort(list)
        self.assertEqual(list, [1, 2, 3, 4, 5])

    def test_worst_case(self):
        list = [5, 4, 3, 2, 1]
        quick_sort(list)
        self.assertEqual(list, [1, 2, 3, 4, 5])

    def test_average_case(self):
        list = [5, 1, 4, 2, 3]
        quick_sort(list)
        self.assertEqual(list, [1, 2, 3, 4, 5])


if __name__ == "__main__":
    unittest.main()
