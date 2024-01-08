#!/usr/bin/python3
""" a lass that inherits """

class Mylist(list):
    """ implements sorted printing for the built-in list class. """

    def print_sorted(self):
        """ print a list in sorted ascending order """
        print(sorted(self))
