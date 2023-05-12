"""
Performs a binary search on the list my_list for the key.

Parameters:
my_list (list): The list to search.
key (any): The value to search for.

low_index (int): The lowest index where the key may be found. 
high_index (int): The highest index where the key may be found.

While low_index is less than or equal to high_index, the search space is narrowed by calculating the mid_index.
If key is found at mid_index, its index is returned.
If key is less than my_list[mid_index], the search space becomes low_index to mid_index - 1. 
If key is greater than my_list[mid_index], the search space becomes mid_index + 1 to high_index.

The search continues until low_index and high_index cross, then -1 is returned indicating the key was not found.
"""


def binary_search(my_list, key):
    # low_index stores lowest index where you might find key
    low_index = 0
    # high_index stores highest index where you might find key
    high_index = len(my_list) - 1

    # when low_index becomes bigger than high index, we stop
    while low_index <= high_index:
        # we need to find mid point
        mid_index = (low_index + high_index) // 2

        if key == my_list[mid_index]:
            return mid_index
        elif key < my_list[mid_index]:
            high_index = mid_index - 1
        else:
            low_index = mid_index + 1

    return -1


print(binary_search([1, 2, 6, 14], 14))
