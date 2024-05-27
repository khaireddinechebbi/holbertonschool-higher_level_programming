#!/usr/bin/python3
"""
This module provides a function to read the contents of a file.

Functions:
    read_file(filename=""): Reads and prints the content of a file.
"""


def read_file(filename=""):
    """
    Reads and prints the content of a file.

    Args:
        filename (str): The name of the file to read.
    """
    with open(filename, encoding="UTF8") as f:
        print(f"{f.read()}", end="")
