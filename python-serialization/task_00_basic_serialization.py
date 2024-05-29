#!/usr/bin/env python3
"""
Module for basic serialization and deserialization of a Python dictionary
 to and from a JSON file.
"""

import json


def serialize_and_save_to_file(data, filename):
    """
    Serializes a Python dictionary and saves it to a JSON file.

    Parameters:
    data (dict): The Python dictionary to serialize.
    filename (str): The name of the file to save the serialized data to.
        If the file already exists, it will be replaced.
    """
    with open(filename, 'w') as f:
        json.dump(data, f)


def load_and_deserialize(filename):
    """
    Loads and deserializes data from a JSON file to a Python dictionary.

    Parameters:
    filename (str): The name of the file to load the data from.

    Returns:
    dict: The deserialized Python dictionary.
    """
    with open(filename, 'r') as f:
        return json.load(f)
