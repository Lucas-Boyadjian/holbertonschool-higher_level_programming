#!/usr/bin/env python3

import pickle

class CustomObject:
    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        print("Name: {}".format(self.name))
        print("Age: {}".format(self.age))
        print("Is Student: {}".format(self.is_student))
    
    def serialize(self, filename):
        with open(filename, "wb") as my_file:
            pickle.dump(self, my_file)

    @classmethod
    def deserialize(cls, filename):
        try:
            with open(filename, "rb") as my_file:
                return pickle.load(my_file)
        except (FileNotFoundError, pickle.PickleError):
            return None
        