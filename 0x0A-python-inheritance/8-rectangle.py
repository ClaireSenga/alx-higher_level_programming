#!/usr/bin/python3
"""Defines a class Rectangle that inherits from BaseGeometry."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):

    def __init__(self, width, height):
        """instantiation of new Rectangle
        Args:
            width (int): Width of Rectangle
            height (int): Height of Rectangle
            """

        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height
