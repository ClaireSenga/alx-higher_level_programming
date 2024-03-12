#!/usr/bin/python3

def uppercase(str):
    uppercase_str = " "  # initialise empty string

    for char in str:
        if 'a' <= char <= 'z':
            # convert yo uppercase
            uppercase_char = "{}".format(chr(ord(char) - 32))

        else:
            uppercase_char = char  # already uppercase, leave it

        uppercase_str += uppercase_char
    return uppercase_str
