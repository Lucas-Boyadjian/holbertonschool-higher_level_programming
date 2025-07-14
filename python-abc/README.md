# Python ABC

This repository contains exercises and scripts related to Python's Abstract Base Classes (ABC) as part of Holberton School projects.

## What is an Abstract Base Class?

An **Abstract Base Class (ABC)** in Python is a class that cannot be instantiated directly. It is used to define a common interface for its subclasses. ABCs are useful for enforcing that certain methods are implemented in any subclass.

You create an ABC by inheriting from `abc.ABC` and marking methods with the `@abstractmethod` decorator.

Example:
```python
from abc import ABC, abstractmethod

class MyBaseClass(ABC):
    @abstractmethod
    def do_something(self):
        pass
```

## Project Structure

Each file in this directory demonstrates or practices a concept related to Python ABCs.

```
python-abc/
├── 0-abstract_base.py
├── 1-my_abc.py
├── 2-shape.py
├── 3-concrete.py
├── ... (other scripts)
└── README.md
```

## Topics Covered

- Creating abstract base classes with `abc.ABC`
- Using the `@abstractmethod` decorator
- Enforcing method implementation in subclasses
- Understanding the difference between abstract and concrete classes
- Practical examples of ABCs in Python

## How to Use

1. Clone this repository or download the files.
2. Run any script with Python 3:
   ```
   python3 <script_name.py>
   ```
3. Read the code and comments to understand how ABCs work in Python.

## Requirements

- Basic knowledge of Python
- Python 3.x installed on your system

## Author

Lucas - Holberton School Student