#!/usr/bin/python3

def islower(c):
    # check if char is alphabetic
    if c.isalpha():
        return ord('a') <= ord(c.lower()) <= ord('z')
    else:
        return False  # for non alphabetic char

print("a is {}".format("lower" if islower("a") else "upper"))
print("H is {}".format("lower" if islower("H") else "upper"))
print("A is {}".format("lower" if islower("A") else "upper"))
print("4 is {}".format("lower" if islower("4") else "upper"))
print("g is {}".format("lower" if islower("g") else "upper"))
