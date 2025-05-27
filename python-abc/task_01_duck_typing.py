#!/usr/bin/env python3
"""
Module illustrating the use of abstract classes
and duck typing in Python.
"""

from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """Abstract class defining the interface for geometric shapes.

    This class cannot be instantiated directly and forces
    its subclasses to implement specific methods.
    """

    @abstractmethod
    def area(self):
        """Abstract method to calculate the area of the shape.

        Returns:
            float: The area of the shape
        """
        pass

    @abstractmethod
    def perimeter(self):
        """Abstract method to calculate the perimeter of the shape.

        Returns:
            float: The perimeter of the shape
        """
        pass


class Circle(Shape):
    """Class representing a circle."""

    def __init__(self, radius):
        """Initialize a circle with a given radius.

        Args:
            radius (float): The radius of the circle
        """
        self.radius = radius

    def area(self):
        """Calculate the area of the circle.

        Returns:
            float: The area of the circle (pi * r²)
        """
        return math.pi * self.radius ** 2

    def perimeter(self):
        """Calculate the perimeter (circumference) of the circle.

        Returns:
            float: The perimeter of the circle (2 * pi * r)
        """
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """Class representing a rectangle."""

    def __init__(self, width, height):
        """Initialize a rectangle with a given width and height.

        Args:
            width (float): The width of the rectangle
            height (float): The height of the rectangle
        """
        self.width = width
        self.height = height

    def area(self):
        """Calculate the area of the rectangle.

        Returns:
            float: The area of the rectangle (width * height)
        """
        return self.width * self.height

    def perimeter(self):
        """Calculate the perimeter of the rectangle.

        Returns:
            float: The perimeter of the rectangle (2 * (width + height))
        """
        return 2 * (self.width + self.height)


def shape_info(Shape):
    """Display the area and perimeter of a geometric shape.

    This function uses the principle of duck typing: it works with
    any object that has area() and perimeter() methods, without explicitly
    checking its type.

    Args:
        shape (Shape): An object that implements the area() and
        perimeter() methods
    """
    print("Area: {}".format(Shape.area()))
    print("Perimeter: {}".format(Shape.perimeter()))
