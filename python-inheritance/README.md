# Python - Inheritance

## Description
This repository contains Python exercises focused on understanding inheritance in object-oriented programming (OOP). Inheritance allows a class to inherit attributes and methods from another class, providing a way to create more specialized classes while maintaining the core functionality of a parent class. This project helps you explore how inheritance works in Python and how to use it effectively.

In this series of tasks, you will implement functions and classes that demonstrate the core concepts of inheritance, including class hierarchy, method overriding, and type checking. You will also implement custom behaviors using isinstance, issubclass, and super.

## Files

| Filename | Description |
|----------|------------|
| `0-lookup.py` | Defines a function lookup that returns the list of available attributes and methods of an object. |
| `1-my_list.py` | Defines a class MyList that inherits from list and implements a method print_sorted to print the list sorted in ascending order. |
| `2-is_same_class.py` | Implements a function is_same_class that returns True if an object is exactly an instance of the specified class. |
| `3-is_kind_of_class.py` | Implements a function is_kind_of_class that checks if an object is an instance of a class or if it inherited from the specified class. |
| `4-inherits_from.py` | Implements a function inherits_from that checks if an object is an instance of a class that inherited from the specified class (directly or indirectly). |
| `5-base_geometry.py` | Empty class BaseGeometry. |
| `6-base_geometry.py` | Class BaseGeometry with area() method that raises an exception. |
| `7-base_geometry.py` | Class BaseGeometry with integer_validator() method for validation. |
| `8-rectangle.py` | Class Rectangle that inherits from BaseGeometry and validates width and height. |
| `9-rectangle.py` | 	Class Rectangle that inherits from BaseGeometry, validates width and height, implements area(). |
| `10-square.py` | Class Square that inherits from Rectangle, validates size, and implements area(). |
| `11-square.py` | Class Square that inherits from Rectangle, validates size, implements area(), and prints square description. |