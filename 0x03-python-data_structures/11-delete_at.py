#!/usr/bin/python3

def delete_at(my_list=[], idx=0):
    # deletes an item at specific posn

    if idx < 0:
        return my_list
    elif idx >= len(my_list):
        return my_list
    else:
        return my_list[:idx] + my_list[idx + 1:]
