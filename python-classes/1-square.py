#!/usr/bin/python3
"""
This module defines a class Square with a private attribute size.
"""


class Square:
    """
    A class that defines a square by its size.

    Attributes:
        __size (int): The size of the square (private).

    Methods:
        __init__(self, size): Initializes a new Square instance with the given size.
    """

    def __init__(self, size):
        """
        Initializes a new Square instance with the given size.

        Args:
            size (int): The size of the square.
        """
        self.__size = size
