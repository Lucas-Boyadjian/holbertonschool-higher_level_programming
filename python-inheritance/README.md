# Python Inheritance

This repository contains exercises and scripts related to inheritance in Python, created as part of Holberton School projects.

## What is Inheritance?

**Inheritance** is an object-oriented programming concept that allows a class (child/subclass) to inherit attributes and methods from another class (parent/superclass).  
It promotes code reuse and makes it easier to create and maintain applications.

Example:
```python
class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def speak(self):
        print("Dog barks")

d = Dog()
d.speak()  # Output: Dog barks
```

## Project Structure

Each file in this directory demonstrates or practices a concept related to Python inheritance.

```
python-inheritance/
├── 0-base_class.py
├── 1-simple_inheritance.py
├── 2-multiple_inheritance.py
├── 3-method_override.py
├── 4-super_usage.py
├── ... (other scripts)
└── README.md
```

## Topics Covered

- Creating base (parent) and derived (child) classes
- Inheriting attributes and methods
- Overriding methods in subclasses
- Using `super()` to access parent class methods
- Multiple inheritance

## How to Use

1. Clone this repository or download the files.
2. Run any script with Python 3:
   ```
   python3 <script_name.py>
   ```
3. Read the code and comments to understand how inheritance works in Python.

## Requirements

- Basic knowledge of Python
- Python 3.x installed on your system

## Author

Lucas - Holberton School Student