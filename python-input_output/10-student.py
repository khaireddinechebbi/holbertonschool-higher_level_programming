#!/usr/bin/python3
"""
Module defining the Student class.
"""


class Student:
    """
    A class to represent a student.

    Attributes:
    ----------
    first_name : str
        the first name of the student
    last_name : str
        the last name of the student
    age : int
        the age of the student
    """

    def __init__(self, first_name, last_name, age):
        """
        Initialize the Student instance with first name, last name, and age.

        Parameters:
        ----------
        first_name : str
            The first name of the student
        last_name : str
            The last name of the student
        age : int
            The age of the student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of a Student instance.

        Parameters:
        ----------
        attrs : list, optional
            A list of strings representing the attribute names \
            to include in the dictionary.
            If not provided, all attributes will be included.

        Returns:
        -------
        dict
            A dictionary representation of the student's attributes.
        """
        if attrs is None:
            return self.__dict__
        else:
            return {attr: self.__dict__[attr] for attr in attrs \
                    if attr in self.__dict__}
