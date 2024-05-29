#!/usr/bin/python3
"""
Module for CustomObject class with serialization and deserialization.
"""
import pickle


class CustomObject:
    """
    A class to represent a custom object.

    Attributes:
    ----------
    name : str
        the name of the person
    age : int
        the age of the person
    is_student : bool
        whether the person is a student or not
    """

    def __init__(self, name, age, is_student):
        """
        Initialize the CustomObject instance with name, age, and is_student.

        Parameters:
        ----------
        name : str
            The name of the person
        age : int
            The age of the person
        is_student : bool
            Whether the person is a student or not
        """
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """
        Display the attributes of the CustomObject instance.
        """
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """
        Serialize the CustomObject instance to a file.

        Parameters:
        ----------
        filename : str
            The name of the file to serialize the object to
        """
        with open(filename, 'w') as f:
            pickle.dump(self, f)

    @classmethod
    def deserialize(cls, filename):
        """
        Deserialize a CustomObject instance from a file.

        Parameters:
        ----------
        filename : str
            The name of the file to deserialize the object from

        Returns:
        -------
        CustomObject
            The deserialized CustomObject instance
        """
        with open(filename, 'r') as f:
            return pickle.load(f)
