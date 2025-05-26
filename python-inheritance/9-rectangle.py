#!/usr/bin/python3
"""Module for Rectangle class that inherits from BaseGeometry"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Rectangle class that inherits from BaseGeometry

    This class represents a rectangle with width and height dimensions
    and provides methods to calculate area and string representation.
    """

    def __init__(self, width, height):
        """
        Initialize a Rectangle with width and height

        Args:
            width (int): The width of the rectangle, must be a positive integer
            height (int): The height of the rectangle,
            must be a positive integer

        Raises:
            TypeError: If width or height is not an integer
            ValueError: If width or height is less than or equal to 0
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """
        Calculate the area of the rectangle

        Returns:
            int: The area (width * height)
        """
        return self.__width * self.__height

    def __str__(self):
        """
        Return string representation of the Rectangle

        Returns:
            str: A string in the format '[Rectangle] width/height'
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
