#!/usr/bin/python3
"""
This module defines a class Square with a private attribute size,\
 proper validation, and methods to get and set the size, as well \
as calculate the area, and print the square.
"""


class Square:
    """
    A class that defines a square by its size and position.

    Attributes:
        __size (int): The size of the square (private).
        __position (tuple): The position of the square (private).

    Methods:
        __init__(self, size=0, position=(0, 0)): Initializes a new \
Square instance with the given size and position.
        size(self): Gets the size of the square.
        size(self, value): Sets the size of the square.
        position(self): Gets the position of the square.
        position(self, value): Sets the position of the square.
        area(self): Returns the current square area.
        my_print(self): Prints in stdout the square with the character #.
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes a new Square instance with the given size and position.

        Args:
            size (int): The size of the square, defaults to 0.
            position (tuple): The position of the square, defaults to (0, 0).

        Raises:
            TypeError: If size is not an integer or if position \
is not a tuple of 2 positive integers.
            ValueError: If size is less than 0 or if position \
contains non-positive integers.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """
        Gets the size of the square.

        Returns:
            int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets the size of the square.

        Args:
            value (int): The new size of the square.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """
        Gets the position of the square.

        Returns:
            tuple: The position of the square.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Sets the position of the square.

        Args:
            value (tuple): The new position of the square.

        Raises:
            TypeError: If position is not a tuple of 2 positive integers.
            ValueError: If position contains non-positive integers.
        """
        if (not isinstance(value, tuple) or len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        Returns the current square area.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2

    def my_print(self):
        """
        Prints in stdout the square with the character #.

        If size is equal to 0, prints an empty line.
        The position attribute will be used to adjust the \
position of the square.
        """
        if self.__size == 0:
            print("")
            return

        [print("") for _ in range(self.__position[1])]

        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
