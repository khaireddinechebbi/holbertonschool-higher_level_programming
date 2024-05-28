#!/usr/bin/python3
"""
This module provides a function to write a Python object \
to a file using JSON representation.

Functions:
    save_to_json_file(my_obj, filename):
    Writes an object to a text file in JSON format.
"""

import json


def save_to_json_file(my_obj, filename):
    """
    Writes an object to a text file, using a JSON representation.

    Args:
        my_obj (object): The Python object to be serialized \
        and written to the file.
        filename (str): The name of the file to write \
        the JSON representation to.
    """
    with open(filename, 'w', encoding='UTF-8') as f:
        json.dump(my_obj, f)
