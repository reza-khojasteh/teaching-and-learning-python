# Author: Reza Khojasteh
# Date: 2023-01-23
# Description: A simple program to sort a list of numbers using the insertion sort algorithm with O(n^2) for the worst case scenario


def insertion_sort(my_list):
    n = len(my_list)
    for i in range(1, n):
        # store the first number/value in the unsorted part of the list into curr
        curr = my_list[i]
        # store the index of the first number/value in the unsorted part of the list into j
        j = i
        # this loop might shift values within the sorted part of the list to open a spot for curr
        while j > 0 and my_list[j - 1] > curr:
            # shift the value at the index to the right
            my_list[j] = my_list[j - 1]
            j -= 1
        # insert curr at the index
        my_list[j] = curr
