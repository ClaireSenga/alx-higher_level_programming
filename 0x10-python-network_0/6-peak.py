#!/usr/bin/python3
""" Finds a peak in a list of unsorted ints"""


def find_peak(list_of_integers):
    """
    Finds a peak in a list of unsorted ints.

    Args:
        list_of_integers (list): List of unsorted ints.

    Returns:
        int or None: The peak element in the list, \
                or None if the list is empty.
    """
    if not list_of_integers:
        return None

    low = 0
    high = len(list_of_integers) - 1

    while low < high:
        mid = (low + high) // 2
        if list_of_integers[mid] <= list_of_integers[mid + 1]:
            low = mid + 1
        else:
            high = mid

    return list_of_integers[low]
