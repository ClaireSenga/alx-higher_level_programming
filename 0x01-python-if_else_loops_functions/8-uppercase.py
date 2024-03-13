#!/usr/bin/python3

def uppercase(s):
    for char in s:
        if 'a' <= char <= 'z':
            print("{}".format(chr(ord(char) - 32)), end='')
        else:
            print(char, end='')
    print()

# Test cases
uppercase("Holberton")
uppercase("Holberton School")
