#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    #  replaces values

    new_list = my_list[:]  # creates copy of new list

    if idx < 0:
        return my_list

    elif idx >= len(my_list):
        return my_list

    else:
        return new_list[idx] = element
