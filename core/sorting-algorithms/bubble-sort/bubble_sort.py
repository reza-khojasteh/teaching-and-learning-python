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
    # set the n to the length of the list
    n = len(list)
    i = 0
    # set the swapped to True so that we can enter the while loop at least once
    swapped = True
    # as long as we haven't done the n - 1 steps/iterations and the list is not yet sorted, enter the while loop and do another iteration
    while i < n - 1 and swapped:
        # set the swapped to False so that we can exit the outer while loop if we don't do any swapping in this iteration
        swapped = False
        # for each element in the list, compare it with the next element and swap them if they are in the wrong order
        # j goes from 0 to n - 2 - i, because in each pass, we will have one less element to compare with
        for j in range(n - 1 - i):
            if list[j] > list[j + 1]:
                list[j + 1], list[j] = list[j], list[j + 1]
                # set the swapped back to True so that we still continue running the outer while loop
                swapped = True
        # do the next (potential) step/iteration of the outer while loop
        i += 1
