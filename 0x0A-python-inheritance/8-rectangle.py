#!/usr/bin/python3
"""Defines a base geometry class BaseGeometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class BaseGeometry(Rectangle):
    """Represents a rectangle using BaseGeometry"""

    def __init__(self, width, height):
        """Initialize a new Rectangle.

        Args:
            width (int): The width is the new Rectangle.
            height (int): The height of the new Rectangle.
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

