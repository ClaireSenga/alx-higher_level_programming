#!/usr/bin/python3
"""a function that priints x elements of a list"""


def safe_print_list(my_list=[], x=0):
    """create function and set x to default zero"""

    num = 0  # initialise a variable to keep track of no. of elements

    for i in range(x):
        try:
            print(my_list[i], end="")
            num += 1
        except IndexError:
            break
    print("")
    Return
