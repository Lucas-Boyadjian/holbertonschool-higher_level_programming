# Python Object Relational Mapping (ORM)

This repository contains exercises and scripts related to Object Relational Mapping (ORM) in Python, created as part of Holberton School projects.

## What is Object Relational Mapping?

**Object Relational Mapping (ORM)** is a technique that allows you to interact with a relational database (like MySQL or SQLite) using Python objects instead of writing raw SQL queries.  
ORM libraries, such as SQLAlchemy, make it easier to create, read, update, and delete database records using Python code.

## Project Structure

Each file in this directory demonstrates or practices a concept related to Python ORM.

```
python-object_relational_mapping/
├── 0-select_states.py
├── 1-filter_states.py
├── 2-my_filter_states.py
├── 3-my_safe_filter_states.py
├── 4-cities_by_state.py
├── 5-filter_cities.py
├── 6-model_state.py
├── 7-model_state_fetch_all.py
├── 8-model_state_fetch_first.py
├── 9-model_state_filter_a.py
├── ... (other scripts)
└── README.md
```

## Topics Covered

- Connecting to a database using Python (MySQLdb, SQLAlchemy)
- Executing SQL queries from Python
- Using ORM libraries (like SQLAlchemy) to map classes to database tables
- Creating, reading, updating, and deleting records using ORM
- Preventing SQL injection and writing safe queries

## How to Use

1. Clone this repository or download the files.
2. Make sure you have Python 3.x and the required libraries installed (`mysqlclient`, `SQLAlchemy`, etc.).
3. Set up your database (MySQL or SQLite) as needed for each script.
4. Run any script with:
   ```
   python3 <script_name.py> <db_user> <db_password> <db_name>
   ```
5. Read the code and comments to understand how ORM works in Python.

## Requirements

- Basic knowledge of Python and SQL
- Python 3.x installed on your system
- MySQL or SQLite database
- Required Python libraries (`mysqlclient`, `SQLAlchemy`, etc.)

## Author

Lucas - Holberton School Student