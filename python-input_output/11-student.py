#!/usr/bin/python3
"""
Module that defines the Student class with JSON
serialization and deserialization
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

    def to_json(self, attrs=None):
        """
        Returns a dictionary representation of the Student instance

        Args:
            attrs (list, optional): A list of attribute names to retrieve.
                                   If None, all attributes are retrieved.

        Returns:
            dict: Dictionary containing the requested instance attributes
        """
        if attrs is None:
            return self.__dict__

        new_dict = {}
        for attr in attrs:
            if hasattr(self, attr):
                new_dict[attr] = getattr(self, attr)
        return new_dict

    def reload_from_json(self, json):
        """
        Replaces all attributes of the Student instance from a dictionary

        Args:
            json (dict): Dictionary with attribute names and values to replace

        Returns:
            None: This method modifies the object in place
        """
        for key, value in json.items():
            setattr(self, key, value)
