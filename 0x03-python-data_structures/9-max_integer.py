#!/usr/bin/python3
def max_integer(my_list=[]):
    # finds biggest integer

    if not my_list:  # list is empty
        return None

    large_int = my_list[0]

    for num in my_list:
        if num > large_int:
            large_int = num

    return large_int
