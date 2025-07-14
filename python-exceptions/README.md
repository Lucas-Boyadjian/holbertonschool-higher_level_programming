# Python Exceptions

This repository contains exercises and scripts related to Python exceptions, created as part of Holberton School projects.

## What are Exceptions?

**Exceptions** in Python are errors detected during execution. They can be handled using `try`, `except`, `else`, and `finally` blocks to make your programs more robust and prevent crashes.

Example:
```python
try:
    result = 10 / 0
except ZeroDivisionError:
    print("You can't divide by zero!")
```

## Project Structure

Each file in this directory demonstrates or practices a concept related to Python exception handling.

```
python-exceptions/
├── 0-safe_print_list.py
├── 1-safe_print_integer.py
├── 2-safe_print_list_integers.py
├── 3-safe_print_division.py
├── 4-list_division.py
├── 5-raise_exception.py
├── 6-raise_exception_msg.py
├── ... (other scripts)
└── README.md
```

## Topics Covered

- Using `try` and `except` to handle exceptions
- Handling specific exception types (e.g., `ZeroDivisionError`, `TypeError`)
- Using `else` and `finally` blocks
- Raising exceptions with `raise`
- Writing safe and robust code

## How to Use

1. Clone this repository or download the files.
2. Run any script with Python 3:
   ```
   python3 <script_name.py>
   ```
3. Read the code and comments to understand how exceptions work in Python.

## Requirements

- Basic knowledge of Python
- Python 3.x installed on your system

## Author

Lucas - Holberton School Student