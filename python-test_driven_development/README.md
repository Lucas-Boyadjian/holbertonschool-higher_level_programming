# Python Test Driven Development (TDD)

This repository contains exercises and scripts related to Test Driven Development (TDD) in Python, created as part of Holberton School projects.

## What is Test Driven Development?

**Test Driven Development (TDD)** is a software development process where you write tests for your code before writing the actual code itself.  
The typical cycle is:
1. Write a test that fails (because the feature isn't implemented yet).
2. Write the minimum code needed to make the test pass.
3. Refactor the code while keeping the tests green.

TDD helps ensure your code works as expected and makes it easier to maintain and refactor.

## Project Structure

Each file in this directory demonstrates or practices a concept related to TDD in Python.

```
python-test_driven_development/
├── 0-add_integer.py
├── 0-add_integer.txt
├── 2-matrix_divided.py
├── 2-matrix_divided.txt
├── 3-say_my_name.py
├── 3-say_my_name.txt
├── 4-print_square.py
├── 4-print_square.txt
├── 5-text_indentation.py
├── 5-text_indentation.txt
├── tests/
│   ├── 0-add_integer.txt
│   └── ... (other test files)
└── README.md
```

## Topics Covered

- Writing and running Python unit tests (using `doctest` and/or `unittest`)
- Writing documentation and test cases for your functions
- Developing code by first writing tests (TDD cycle)
- Refactoring code while keeping tests passing

## How to Use

1. Clone this repository or download the files.
2. Run any script with Python 3:
   ```
   python3 <script_name.py>
   ```
3. To run doctests included in the `.py` files:
   ```
   python3 -m doctest <script_name.py> -v
   ```
4. Read the code, comments, and test files to understand how TDD works in Python.

## Requirements

- Basic knowledge of Python
- Python 3.x installed on your system

## Author

Lucas - Holberton School Student