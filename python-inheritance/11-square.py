#!/usr/bin/python3
"""Module for Square class that inherits from Rectangle"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Square class that inherits from Rectangle

    This class represents a square, which is a special kind of rectangle
    where all sides have equal length.
    """

    def __init__(self, size):
        """
        Initialize a Square with size

        Args:
            size (int): The size of the square, must be a positive integer

        Raises:
            TypeError: If size is not an integer
            ValueError: If size is less than or equal to 0
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """
        Calculate the area of the square

        Returns:
            int: The area (size * size)
        """
        return self.__size * self.__size

    def __str__(self):
        """
        Return string representation of the Square

        Returns:
            str: A string in the format '[Square] size/size'
        """
        return "[Square] {}/{}".format(self.__size, self.__size)
