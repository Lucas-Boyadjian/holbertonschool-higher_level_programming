#!/usr/bin/python3
"""
Module that defines the Student class
"""


class Student:
    """
    Class that defines a student
    """
    def __init__(self, first_name, last_name, age):
        """
        Initialize a new Student instance

        Args:
            first_name (str): The first name of the student
            last_name (str): The last name of the student
            age (int): The age of the student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        Returns a dictionary representation of the Student instance

        Returns:
            dict: Dictionary containing all instance attributes
        """
        return self.__dict__
