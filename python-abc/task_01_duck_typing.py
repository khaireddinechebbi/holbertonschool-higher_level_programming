"""
This module provides an implementation of duck typing with abstract \
base classes for shapes.

It defines an abstract class `Shape` with two abstract methods: \
`area()` and `perimeter()`.
Two concrete classes, `Circle` and `Rectangle`, inherit from `Shape` \
and implement these methods.
A standalone function `shape_info` is provided to print the area \
and perimeter of a shape object.

Example:
    # Instantiate a Circle and a Rectangle
    circle = Circle(radius=5)
    rectangle = Rectangle(width=4, height=7)

    # Print information about the shapes
    shape_info(circle)
    shape_info(rectangle)

Classes:
    Shape(ABC): An abstract base class representing a shape.
    Circle(Shape): A concrete class representing a circle.
    Rectangle(Shape): A concrete class representing a rectangle.

Functions:
    shape_info(shape): Prints the area and perimeter of a shape.

Attributes:
    pi (float): The mathematical constant pi.
"""

from abc import ABC, abstractmethod
from math import pi


class Shape(ABC):
    """Abstract base class representing a shape."""

    @abstractmethod
    def area(self):
        """Abstract method to calculate the area of the shape."""
        pass

    @abstractmethod
    def perimeter(self):
        """Abstract method to calculate the perimeter of the shape."""
        pass


class Circle(Shape):
    """Class representing a circle."""

    def __init__(self, radius):
        """Initialize a circle with a given radius."""
        self.radius = radius
    
        if radius < 0:
            raise ValueError("Radius must be non-negative")

    def area(self):
        """Calculate the area of the circle."""
        return pi * self.radius ** 2

    def perimeter(self):
        """Calculate the perimeter of the circle."""
        return 2 * pi * self.radius


class Rectangle(Shape):
    """Class representing a rectangle."""

    def __init__(self, width, height):
        """Initialize a rectangle with given width and height."""
        self.width = width
        self.height = height

    def area(self):
        """Calculate the area of the rectangle."""
        return self.width * self.height

    def perimeter(self):
        """Calculate the perimeter of the rectangle."""
        return 2 * (self.width + self.height)


def shape_info(shape):
    """
    Print the area and perimeter of a shape.

    Args:
        shape (Shape): An object representing a shape.

    Example:
        # Instantiate a Circle and a Rectangle
        circle = Circle(radius=5)
        rectangle = Rectangle(width=4, height=7)

        # Print information about the shapes
        shape_info(circle)
        shape_info(rectangle)
    """
    print("Area:", shape.area())
    print("Perimeter:", shape.perimeter())


if __name__ == "__main__":
    # Instantiate a Circle and a Rectangle
    circle = Circle(radius=5)
    rectangle = Rectangle(width=4, height=7)

    # Print information about the shapes
    shape_info(circle)
    shape_info(rectangle)
