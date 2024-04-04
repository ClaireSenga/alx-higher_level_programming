#!/usr/bin/python3
"""a function that prints the 1st x elements with only ints"""


def safe_print_list_integers(my_list=[], x=0):
    num = 0  # initial no. of the count

    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            num += 1  # increment the count of num.
        except (ValueError, TypeError):
            pass
    print()
    return num
