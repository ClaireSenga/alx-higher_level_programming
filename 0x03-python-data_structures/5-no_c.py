#!/usr/bin/python3

def no_c(my_string):
    # initialise empty string
    result = ""

    for char in my_string:
        if char.lower() != 'c':  # converts char to lowercase
            result += char

    return result
