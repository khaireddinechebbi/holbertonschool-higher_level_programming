#!/usr/bin/python3
"""
This module provides a function `add_integer` to add two integers.
"""

def add_integer(a, b=98):
    """
    Adds two integers or floats after casting them to integers.

    Args:
        a (int, float): The first number, must be an integer or float.
        b (int, float): The second number, must be an integer or float, default is 98.

    Returns:
        int: The sum of a and b as an integer.

    Raises:
        TypeError: If either a or b is not an integer or float.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
