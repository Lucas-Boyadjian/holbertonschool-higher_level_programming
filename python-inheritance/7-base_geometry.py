#!/usr/bin/python3
"""Module for the BaseGeometry class"""


class BaseGeometry:
    """
    A base class for geometry-related operations

    This class provides a foundation for geometric calculations
    and includes validation methods for geometric properties.
    """

    def area(self):
        """
        Calculate the area of a geometric shape

        Raises:
            Exception: This method is not implemented in the base class
                      and should be overridden by subclasses
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates that a value is a positive integer

        Args:
            name (str): The name of the parameter being validated
            value: The value to validate

        Raises:
            TypeError: If value is not an integer
            ValueError: If value is less than or equal to 0
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
