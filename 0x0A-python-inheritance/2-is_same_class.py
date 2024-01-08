#!/usr/bin/python3
""" defines a class-checking function """

def is_same_class(obj, a_class):
    """ returns true if object is the exact instance """

    Args:
        obj (any): The object to check.
        a_class (type): The class to match the type of obj to.

        Returns:
            if obj is exactly an instance of a_class - True.
            Otherwise - False

           """
            if type(obj) == a_class:
            return True
        return False
