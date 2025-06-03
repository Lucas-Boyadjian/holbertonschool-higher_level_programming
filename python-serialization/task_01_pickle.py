#!/usr/bin/env python3

import pickle


class CustomObject:
    """
    A class representing a custom object that can be
    serialized and deserialized using pickle
    """
    def __init__(self, name, age, is_student):
        """
        Initialize a CustomObject with name, age and student status

        Args:
            name: Person's name
            age: Person's age
            is_student: Boolean indicating student status
        """
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """
        Display the object's attributes in a formatted way
        """
        print("Name: {}".format(self.name))
        print("Age: {}".format(self.age))
        print("Is Student: {}".format(self.is_student))

    def serialize(self, filename):
        """
        Serialize this object and save it to a file using pickle

        Args:
            filename: Path to the output file
        """
        with open(filename, "wb") as my_file:
            pickle.dump(self, my_file)

    @classmethod
    def deserialize(cls, filename):
        """
        Deserialize an object from a file

        Args:
            filename: Path to the pickle file

        Returns:
            The deserialized CustomObject or None if
            file not found or pickle error
        """
        try:
            with open(filename, "rb") as my_file:
                return pickle.load(my_file)
        except (pickle.UnpicklingError):
            return None
