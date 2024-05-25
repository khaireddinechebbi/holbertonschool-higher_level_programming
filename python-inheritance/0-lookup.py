#!/usr/bin/python3
"""
This module provide a function that returns the list of available attributes \
and methods of an object
"""


def lookup(obj):
    """
    Returns the list of available attributes and methods of an object.

    Args:
        obj (any): The object to inspect.

    Returns:
        list: A list of strings representing the names of the attributes \
and methods.
    """
    return dir(obj)
