#!/usr/bin/python3
def print_list_integer(my_list=[]):

    if my_list is None:
        return

    for num in my_list:  # used to iterate values
        print("{}".format(num))
