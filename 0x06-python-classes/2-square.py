#!/usr/bin/python3
"""Define a class Square."""


class Square:
    """class that defines a square"""

    def __init__(self, size=0):
        """Initialize a new Square.
        Args are:
            size (int): The size of the new square.
        """
        if not isinstance(size, int):  # checks type if int
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
