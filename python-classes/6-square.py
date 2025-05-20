#!/usr/bin/python3
"""Module containing the Square class that represents a square"""


class Square:
    """Class that defines a square by its size and position

    Attributes:
        __size (int): Length of the square's side
        __position (tuple): Position of the square as (x, y)
    """

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a new Square instance

        Args:
            size (int, optional): Length of the square's side. Defaults to 0.
            position (tuple, optional): Position (x, y) of the square.
                Defaults to (0, 0).
        """
        self.size = size
        self.position = position

    def area(self):
        """Calculate the area of the square

        Returns:
            int: The area of the square (side²)
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

    @property
    def position(self):
        """Getter for the private attribute __position

        Returns:
            tuple: Position of the square (x, y)
        """
        return self.__position

    @position.setter
    def position(self, value):
        """Setter for the private attribute __position

        Args:
            value (tuple): New position (x, y) for the square

        Raises:
            TypeError: If value is not a tuple of 2 positive integers
        """
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")

        if (not isinstance(value[0], int) or not isinstance(value[1], int) or
                value[0] < 0 or value[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        """Print the square using # characters

        The square is printed with an offset according to position:
        - position[1] empty lines at the beginning (vertical offset)
        - position[0] spaces before each line (horizontal offset)

        If size is 0, prints only an empty line.
        """
        if self.size == 0:
            print()
            return

        for _ in range(self.__position[1]):
            print()

        for _ in range(self.size):
            print(" " * self.__position[0] + "#" * self.size)
