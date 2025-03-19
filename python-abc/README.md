# Python - Abstract Classes and Interfaces

## Description
This repository contains Python exercises focused on understanding abstract classes and interfaces in object-oriented programming (OOP). In this set of exercises, you'll explore abstract base classes (ABCs), interfaces, subclassing, and duck typing. You will also learn how to use abstract methods to enforce common behavior and how to implement interfaces for ensuring that objects follow specific contracts or protocols.

The objective of this project is to get hands-on experience with important OOP concepts like method overriding, abstract classes, interfaces, and duck typing, and apply them in practical examples using Python.

## Files

| Filename | Description |
|----------|------------|
| `task_00_abc.py` | Implements an abstract class Animal with subclasses Dog and Cat, each implementing the sound method. |
| `task_01_duck_typing.py` | Defines an abstract class Shape with methods for area and perimeter. Implements concrete classes Circle and Rectangle. Also includes a function shape_info that uses duck typing to calculate the area and perimeter of the shapes. |
| `task_02_verboselist.py` | Creates a VerboseList class that extends Python's built-in list class. It overrides append, extend, remove, and pop methods to print messages when list operations are performed. |
| `task_03_countediterator.py` | Implements a CountedIterator class that tracks the number of iterations over an iterable. The class includes a get_count method to retrieve the current count of iterations. |
| `task_04_flyingfish.py` | Constructs a FlyingFish class that inherits from both Fish and Bird classes. The class overrides methods to demonstrate multiple inheritance and method resolution order (MRO). |
| `task_05_dragon.py` | Designs two mixin classes, SwimMixin and FlyMixin, and constructs a Dragon class that inherits from both to demonstrate swimming and flying abilities. |