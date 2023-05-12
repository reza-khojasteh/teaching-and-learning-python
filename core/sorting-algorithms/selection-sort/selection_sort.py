# Author: Reza Khojasteh
# Date: 2023-01-23
# Description: A simple program to sort a list of numbers using the selection sort algorithm with O(n^2) for the worst case scenario

def selection_sort(my_list):
    n = len(my_list)
    for i in range(n - 1):
        min_idx = i  # record the index of the smallest value, initialized with where the smallest value may be found
        for j in range(i + 1, n):              # go through list, 
            if my_list[j] < my_list[min_idx]:  # and every time we find a smaller value,
                min_idx = j                    # record its index
        # in case there is really a need to swap, swap the smallest value with the value at the current index
        if min_idx != i:
            my_list[min_idx], my_list[i] = my_list[i], my_list[min_idx]