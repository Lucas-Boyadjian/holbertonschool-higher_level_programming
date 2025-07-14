# Python Classes

This repository contains exercises and scripts related to Python classes, created as part of Holberton School projects.

## What is a Python Class?

A **class** in Python is a blueprint for creating objects. Classes encapsulate data for the object and methods to manipulate that data. Using classes allows you to implement object-oriented programming (OOP) concepts such as encapsulation, inheritance, and polymorphism.

Example:
```python
class Dog:
    def __init__(self, name):
        self.name = name

    def bark(self):
        print(f"{self.name} says woof!")
```

## Project Structure

Each file in this directory demonstrates or practices a concept related to Python classes.

```
python-classes/
├── 0-class_definition.py
├── 1-init_method.py
├── 2-instance_attributes.py
├── 3-class_attributes.py
├── 4-methods.py
├── 5-inheritance.py
├── 6-polymorphism.py
├── ... (other scripts)
└── README.md
```

## Topics Covered

- Defining classes and creating objects
- Using the `__init__` constructor
- Instance and class attributes
- Defining and calling methods
- Inheritance and subclassing
- Method overriding and polymorphism

## How to Use

1. Clone this repository or download the files.
2. Run any script with Python 3:
   ```
   python3 <script_name.py>
   ```
3. Read the code and comments to understand how classes work in Python.

## Requirements

- Basic knowledge of Python
- Python 3.x installed on your system

## Author

Lucas - Holberton School Student