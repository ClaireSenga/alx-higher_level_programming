#!/usr/bin/python3
""" a funtion that instance classes and objects """


def is_kind_of_class(obj, a_class):
    """function that returns true if object is instance of class that inherited from

    Args:
        obj(any): The object to check
        a_class(type): The class to match the type obj to.
        Returns:
            if obj is an instance or inherited instance of a_class - True

    """

            if isinstance(obj, a_class):
            return True
        return False
