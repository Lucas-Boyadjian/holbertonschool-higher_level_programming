#!/usr/bin/python3
"""Module that defines a Square class"""


class Square:
    """Class that defines a square by its size

    Attributes:
        __size (int): Private attribute for the size of the square
    """

    def __init__(self, size=0):
        """Initialize a new Square instance

        Args:
            size (int, optional): Size of the square. Defaults to 0.

        Raises:
            TypeError: If size is not an integer
            ValueError: If size is negative
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Calculate the area of the square

        Returns:
            int: The area of the square (size²)
        """
        return self.__size**2

    @property
    def size(self):
        """Getter method for the private attribute __size

        Returns:
            int: The size of the square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Setter method for the private attribute __size

        Args:
            value (int): New size for the square

        Raises:
            TypeError: If value is not an integer
            ValueError: If value is negative
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
