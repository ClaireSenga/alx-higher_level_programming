#!/usr/bin/pythons3
"""Defines a class-checking function"""

def inherits_from(obj, a_class):
    """a func that checks if an objects is an instance of a class
    that had been inherited from directly or indirectly
    Args:
        obj (any): object to check
        a_class (type): to see if obj is an instance of this class
    Returns:
        True if obj is an instance of a_class
        Otherwise - False"""

    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
