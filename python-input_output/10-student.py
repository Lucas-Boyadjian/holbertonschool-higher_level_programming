#!/usr/bin/python3

class Student:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if attrs is None:
            return self.__dict__
        
        new_dict = {}
        for attr in attrs:
            if hasattr(self, attr):
                new_dict[attr] = getattr(self, attr)
        return new_dict