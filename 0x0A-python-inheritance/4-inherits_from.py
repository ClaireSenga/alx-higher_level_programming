#!/usr/bin/python3
""" function that states objects and classes instances """

def inherits_from(obj, a_class):
    """ function that returns True if object is an instance of a class """

    Args:
        obj(any): The object to check
        a_class(type): The class to match the type of obj to.
        Returns:
            if obj is inherited instance of a_class - True
            Otherwise - False

            """
            if issubclass(type(obj), a_class) and type(obj) != a_class:
            return True
        return False
