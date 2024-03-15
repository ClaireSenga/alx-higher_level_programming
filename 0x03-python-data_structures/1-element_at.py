#!/usr/bin/python3

def element_at(my_list, idx):
    if idx < 0:  # idx is negaive
        return None

    elif idx > len(my_list):  # if idx is out of range
        return None

    else:
        return my_list[idx]
