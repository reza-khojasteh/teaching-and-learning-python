# Author: Reza Khojasteh
# Date: 2023-01-23
# Description: A simple program to sort a list of numbers using the bubble sort algorithm with O(n^2) for the worst case scenario


# Version 1


# def bubble_sort(list):
#     n = len(list)
#     for i in range(n - 1):
#         for j in range(n - 1):
#             if list[j] > list[j + 1]:
#                 list[j + 1], list[j] = list[j], list[j + 1]
#                 # print(list)

# Version 2


# def bubble_sort(list):
#     n = len(list)
#     for i in range(n - 1):
#         for j in range(n - 1 - i):
#             if list[j] > list[j + 1]:
#                 list[j + 1], list[j] = list[j], list[j + 1]
#                 # print(list)

# Version 3 (with Ω(n) for the best case scenario)


# def bubble_sort(list):
#     n = len(list)

#     for i in range(n - 1):
#         swapped = False

#         for j in range(n - 1 - i):
#             if list[j] > list[j + 1]:
#                 list[j + 1], list[j] = list[j], list[j + 1]
#                 swapped = True

#         if not swapped:
#             break


# Version 4 (the same as version 3, just in case you want to avoid using the 'break' statement)


def bubble_sort(list):
    n = len(list)
    i = 0
    swapped = True
    # As long as we have not reached the end of the list and the boolean 'swapped' is True, we keep iterating
    while i < n - 1 and swapped:
        swapped = False

        for j in range(n - 1 - i):
            if list[j] > list[j + 1]:
                list[j + 1], list[j] = list[j], list[j + 1]
                swapped = True

        i += 1
