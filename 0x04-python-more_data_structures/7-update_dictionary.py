#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    if key in a_dictionary:
        a_dictionary[key] = value
    else:  # key does not exist
        a_dictionary[key] = value

    return a_dictionary
