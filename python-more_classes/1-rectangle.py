#!/usr/bin/python3
"""
This module defines a class Rectangle \
with private attributes width and height.
"""


class Rectangle:
    """
    A class used to represent a Rectangle.
    ...

    Attributes:
        width (int): width of the rectangle (default is 0)
        height (int): height of the rectangle (default is 0)

    Methods:
        width(): Gets the width of the rectangle
        width(value): Sets the width of the rectangle
        height(): Gets the height of the rectangle
        height(value): Sets the height of the rectangle
    """

    def __init__(self, width=0, height=0):
        """
        Constructs all the necessary attributes for the rectangle object.

        Parameters:
            width (int, optional): Width of the rectangle (default is 0)
            height (int, optional): Height of the rectangle (default is 0)
        """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """
        Gets the width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Sets the width of the rectangle.

        Parameters
        ----------
        value : int
            Width of the rectangle

        Raises
        ------
        TypeError
            If width is not an integer
        ValueError
            If width is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Gets the height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Sets the height of the rectangle.

        Parameters
        ----------
        value : int
            Height of the rectangle

        Raises
        ------
        TypeError
            If height is not an integer
        ValueError
            If height is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
