#!/usr/bin/python3
"""Module that defines a Square class"""


class Square:
    """Class that defines a square by its size

    Attributes:
        __size (int): Private attribute for the size of the square
    """

    def __init__(self, size):
        """Initialize a new Square instance

        Args:
            size: Size of the square
        """
        self.__size = size
