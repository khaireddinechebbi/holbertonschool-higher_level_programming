#!/usr/bin/python3
"""
This module provides a function `inherits_from` that checks if an object
is an instance of a class that inherited (directly or indirectly) from the
specified class.
"""


def inherits_from(obj, a_class):
    """
    Returns True if obj is an instance of a class that inherited \
(directly or indirectly) from a_class, otherwise False.

    Args:
        obj: The object to check.
        a_class: The class to match the type of obj against.

    Returns:
        bool: True if obj is an instance of a subclass of a_class, \
otherwise False.
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
