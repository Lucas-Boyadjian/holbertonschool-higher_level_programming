#!/usr/bin/python3
"""Module containing the Square class that defines a square"""


class Square:
    """Class that defines a square by its size

    Attributes:
        __size (int): Length of the square's side
    """

    def __init__(self, size=0):
        """Initialize a new Square instance

        Args:
            size (int, optional): Length of the square's side. Defaults to 0.

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
        """Getter for the private attribute __size

        Returns:
            int: The size of the square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Setter for the private attribute __size

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

    def my_print(self):
        """Print the square using # characters

        If size is 0, prints only an empty line.
        """
        if self.size == 0:
            print()
            return

        for _ in range(self.size):
            print('#' * self.size)
