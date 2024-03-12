#!/usr/bin/python3

def uppercase(str):
    uppercase_str = " " #initialise empty string

    for char in str:
        if 'a' <= char <= 'z': #if char are lowercase
            uppercase_char = chr(ord(char) - 32) #convert to uppercase

        else:
            uppercase_char = char#if char is already uppercase, leave it

    uppercase_str += uppercase_char
    return uppercase_str #close function
