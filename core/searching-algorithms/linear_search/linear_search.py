"""
Performs a linear search on the list my_list for the key.

Parameters: 
my_list (list): The list to search.
key (any): The value to search for.

i (int): The index currently being searched.

The list is iterated over from index 0 to the length of the list.
If the key is found at any index, that index is returned.
If the key is not found, -1 is returned.
"""


def linear_search(my_list, key):
    n = len(my_list)
    # iterate over the list
    for i in range(n):
        if my_list[i] == key:
            return i

    return -1


print(linear_search([1, 2, 6, 4], 6))
