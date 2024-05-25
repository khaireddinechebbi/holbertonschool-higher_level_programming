#!/usr/bin/python3
"""
This module provides a class `BaseGeometry` for representing geometry.
"""


class BaseGeometry:
    """
    A class used to represent geometry.

    Attributes:
        None

    Methods:
        area(self):
            Raises an Exception with the message "area() is not implemented".
        integer_validator(self, name, value):
            Validates if the provided value is an integer greater than 0.
    """

    def area(self):
        """
        Raises an Exception with the message "area() is not implemented".

        Args:
            None

        Returns:
            None

        Raises:
            Exception: When called.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates if the provided value is an integer greater than 0.

        Args:
            name (str): The name of the value being validated.
            value (int): The value to be validated.

        Returns:
            None

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/7-base_geometry.txt")
