# Author: Reza Khojasteh
# Date: 2023-01-30
# Quick sort is a divide and conquer algorithm and requires O(n^2) for the worst case and O(nlog(n)) for the best and average case.
# Regardig space complexity, it requires O(log(n)) for the best case and O(n) for the worst and average case.
# The worst case occurs when the partition process always picks greatest or smallest element as pivot.
# The best case occurs when the partition process always picks the middle element as pivot.
# The average case occurs when the pivot is chosen randomly.
# The worst case occirs when the partition process always picks greatest or smallest element as pivot.

import random


# def quick_sort(my_list):
#     n = len(my_list)
#     if n > 1:
#         recursive_quick_sort(my_list, 0, n - 1)


# def recursive_quick_sort(my_list, start=0, end=None):
#     # uncomment the following two 'print(my_list)' statements and the last commented out ones
#     # to see the outcome of the quick sort algorithm, after each swap!

#     if start < end:
#         # choose a random index between start and end inclusive, to get the pivot_element
#         pivot_location = random.randint(start, end)

#         # move the pivot_element out of the way by swapping it with the last value of the partition
#         my_list[pivot_location], my_list[end] = my_list[end], my_list[pivot_location]

#         pivot = end
#         pivot_element = my_list[end]
#         i = start
#         j = end - 1
#         while i <= j:
#             while i <= j and my_list[i] <= pivot_element:
#                 i += 1
#             while i <= j and my_list[j] > pivot_element:
#                 j -= 1
#             if i < j:
#                 my_list[i], my_list[j] = my_list[j], my_list[i]
#                 i += 1
#                 j -= 1
#                 # print(my_list)
#         if i != pivot:
#             my_list[i], my_list[pivot] = my_list[pivot], my_list[i]
#             # print(my_list)
#         recursive_quick_sort(my_list, 0, i - 1)
#         recursive_quick_sort(my_list, i + 1, end)


# OR, using insertion sort for small partitions:
def quick_sort(mylist):
    # call recursive quicksort
    recursive_quick_sort(mylist, 0, len(mylist) - 1)


def recursive_quick_sort(mylist, left, right, THRESHOLD=32):
    if right - left <= THRESHOLD:
        insertion_sort(mylist, left, right)
    else:
        pivot_position = partition(mylist, left, right)
        recursive_quick_sort(mylist, left, pivot_position - 1)
        recursive_quick_sort(mylist, pivot_position + 1, right)


def insertion_sort(mylist, left, right):
    for i in range(left + 1, right + 1):
        # store the first number in the unsorted part of array into curr
        curr = mylist[i]
        j = i
        # the following loop shifts value within sorted part of array to open a spot for curr
        while j > left and mylist[j - 1] > curr:
            mylist[j] = mylist[j - 1]
            j = j - 1
        mylist[j] = curr


def partition(mylist, left, right):
    # choose a random index between left and right inclusive
    pivot_location = random.randint(left, right)

    # get the pivot
    pivot = mylist[pivot_location]

    # move the pivot out of the way by swapping with
    # last value of partition.  This step is crucial as pivot will
    # end up "moving" if we don't get it out of the way which will
    # lead to inconsistent results.
    mylist[pivot_location] = mylist[right]
    mylist[right] = pivot

    end_of_smaller = left - 1

    # note the loop below does not look at pivot which is in mylist[right]
    for j in range(left, right):
        if mylist[j] <= pivot:
            end_of_smaller += 1
            mylist[end_of_smaller], mylist[j] = mylist[j], mylist[end_of_smaller]

    # restore the pivot
    mylist[end_of_smaller +
           1], mylist[right] = mylist[right], mylist[end_of_smaller + 1]

    # and return its location
    return end_of_smaller + 1


# my_list = [5, 4, 3, 2, 1]
# print("Before Sorting: ", my_list)
# quick_sort(my_list)
# print("After Sorting: ", my_list)
