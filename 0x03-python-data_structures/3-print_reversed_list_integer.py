#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):

    my_list.reverse()  #  apply before calling loop

    for num in my_list:  # to iterate
        print("{}".format(num))
