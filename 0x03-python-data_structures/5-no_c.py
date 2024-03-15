#!/usr/python3

def no_c(my_string):
    # removes all c characters

    for char in my_string:
        if char.lower() != 'c':  # converts char to lowercase
            result += char
            return result
