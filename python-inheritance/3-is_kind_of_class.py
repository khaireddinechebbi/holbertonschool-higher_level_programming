#!/usr/bin/python3
"""
This module provides a function `is_kind_of_class` that checks if an object
is an instance of, or if the object is an instance of a class that inherited from,
the specified class.
"""

def is_kind_of_class(obj, a_class):
    """
    Returns True if obj is an instance of a_class, or if obj is an instance of a class
    that inherited from a_class, otherwise False.
    
    Args:
        obj: The object to check.
        a_class: The class to match the type of obj against.
        
    Returns:
        bool: True if obj is an instance or inherited instance of a_class, otherwise False.
    """
    return isinstance(obj, a_class)
