# Author: Reza Khojasteh
# Date: 2023-01-27
# Merge sort is a divide and conquer algorithm. It divides the input array into two halves, calls itself for the two halves, and then merges the two sorted halves. The merge() function is used for merging two halves. The merge(arr, l, m, r) is the key process that assumes that arr[l..m] and arr[m+1..r] are sorted and merges the two sorted sub-arrays into one.
# Merge sort requires O(nlog(n)) time for the worst case and O(nlog(n)) extra space.

# def merge_sort(my_list):
#     n = len(my_list)
#     if n > 1:
#         mid = n // 2
#         left = my_list[:mid]
#         right = my_list[mid:]
#         merge_sort(left)
#         merge_sort(right)
#         i = j = k = 0
#         while i < len(left) and j < len(right):
#             if left[i] < right[j]:
#                 my_list[k] = left[i]
#                 i += 1
#             else:
#                 my_list[k] = right[j]
#                 j += 1
#             k += 1
#         while i < len(left):
#             my_list[k] = left[i]
#             i += 1
#             k += 1
#         while j < len(right):
#             my_list[k] = right[j]
#             j += 1
#             k += 1
#     # print(my_list) # uncomment this line to see the steps of the merge sort algorithm

# merge_sort([4, 2, 3, 1]) # uncomment this line to see the steps of the merge sort algorithm


# OR even better, with O(nlog(n)) time for the worst case and O(n) extra space:
def merge_sort(mylist):
    # create an empty list for merging.  doing it once
    empty_list = [0] * len(mylist)
    # is more efficient than repeatedly creating it when merging

    recursive_merge_sort(
        mylist, 0, len(mylist) - 1, empty_list
    )  # call recursive mergesort


def recursive_merge_sort(mylist, first_index, last_index, empty_list):
    # recursive merge sort.  the base case occurs when first_index >= last_index
    # that situation will only occur if the portion of the list is size 0 or 1.
    # in either case, do nothing and exit function.

    if first_index < last_index:
        mid_index = (first_index + last_index) // 2
        recursive_merge_sort(mylist, first_index, mid_index, empty_list)
        recursive_merge_sort(mylist, mid_index + 1, last_index, empty_list)
        merge(mylist, first_index, mid_index + 1, last_index, empty_list)


# this function will merge two sorted pieces of an array into a single sorted segment.
# We will refer to the two smaller sorted pieces of lists as a and b.
# These are not true lists but rather pieces of mylist
# list a starts at a_first_index and ends at b_first_index - 1 (inclusive)
# list b starts at b_first_index and ends at b_last_index (inclusive)
# this function will merge them together using empty_list as temporary storage
# once it is merged together, it is copied back into mylist, creating a single
# sorted segment that starts at a_first_index to b_last_index (inclusive)


def merge(mylist, a_first_index, b_first_index, b_last_index, empty_list):
    a_ptr = a_first_index  # used to track value from a
    b_ptr = b_first_index
    empty_list_index = a_ptr

    while (a_ptr < b_first_index) and (b_ptr <= b_last_index):
        if mylist[a_ptr] <= mylist[b_ptr]:
            empty_list[empty_list_index] = mylist[a_ptr]
            empty_list_index += 1
            a_ptr += 1
        else:
            empty_list[empty_list_index] = mylist[b_ptr]
            empty_list_index += 1
            b_ptr += 1

    while a_ptr < b_first_index:
        empty_list[empty_list_index] = mylist[a_ptr]
        empty_list_index += 1
        a_ptr += 1

    while b_ptr <= b_last_index:
        empty_list[empty_list_index] = mylist[b_ptr]
        empty_list_index += 1
        b_ptr += 1

    for i in range(a_first_index, b_last_index + 1):
        mylist[i] = empty_list[i]
