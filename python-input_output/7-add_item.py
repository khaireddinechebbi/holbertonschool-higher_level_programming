#!/usr/bin/python3
import sys
import os
"""
This module adds all command-line arguments to a Python list \
and saves them to a file.

The list is saved as a JSON representation in a file named 'add_item.json'.
If the file doesn't exist, it is created.

Usage:
    ./7-add_item.py arg1 arg2 ...

Arguments:
    arg1, arg2, ... : Arguments to be added to the list and saved to the file.
"""


save_to_json_file = __import__("5-save_to_json_file.py").save_to_json_file
"""
This module provides a function to write a Python object \
to a file using JSON representation.
"""
load_from_json_file = __import__("6-load_from_json_file.py").\
    load_from_json_file
"""
This module provides a function to create a Python object from a JSON file.
"""
filename = 'add_item.json'

if os.path.exists(filename):
    items = load_from_json_file(filename)
else:
    items = []

items.extend(sys.argv[1:])
save_to_json_file(items, filename)
