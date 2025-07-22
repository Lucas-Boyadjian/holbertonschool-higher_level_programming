# Python: Everything is Object – Deep Dive into Mutability, Identity, and Function Arguments

## Introduction

In this project, I explored the core concept that **everything in Python is an object**. Through a series of hands-on exercises, I learned how Python handles object identity, mutability, and the subtleties of passing arguments to functions. These concepts are fundamental for writing robust, bug-free Python code and for understanding how Python manages memory and variables under the hood.

## id and type

Python provides two essential built-in functions: `type()` and `id()`.  
- `type(obj)` returns the type of the object, for example, `int`, `str`, `list`, etc.
- `id(obj)` returns the unique identifier (the memory address in CPython) of the object.

**Example:**
```python
a = 42
print(type(a))  # <class 'int'>
print(id(a))    # e.g., 140711303059120
```
These tools help you understand what kind of object you are working with and whether two variables point to the same object in memory.

## Mutable objects

**Mutable objects** can be changed after they are created. Lists, dictionaries, and sets are the most common mutable types in Python. When you modify a mutable object, its `id` does not change.

**Example:**
```python
l1 = [1, 2, 3]
print(id(l1))  # e.g., 140711303059120
l1.append(4)
print(l1)      # [1, 2, 3, 4]
print(id(l1))  # Same as before
```
If you assign one list to another variable (`l2 = l1`), both variables point to the same object.

## Immutable objects

**Immutable objects** cannot be changed after creation. Integers, floats, strings, and tuples are immutable. Any operation that seems to modify them actually creates a new object with a new `id`.

**Example:**
```python
a = 1
print(id(a))  # e.g., 140711303059120
a += 1
print(a)      # 2
print(id(a))  # Different from before
```
Assigning one immutable object to another variable (`b = a`) makes both variables point to the same object, but any "modification" creates a new object.

## Why does it matter and how differently does Python treat mutable and immutable objects?

Understanding mutability is crucial because it affects how variables behave when passed to functions or assigned to new variables.  
- **Mutable objects**: Changes made inside a function or via another variable are reflected everywhere.
- **Immutable objects**: Changes create new objects, so the original variable remains unchanged.

**Example:**
```python
def add_item(lst):
    lst.append(4)

l = [1, 2, 3]
add_item(l)
print(l)  # [1, 2, 3, 4]  # Changed globally

def increment(n):
    n += 1

a = 1
increment(a)
print(a)  # 1  # Unchanged
```

## How arguments are passed to functions and what does that imply for mutable and immutable objects

Python passes arguments **by assignment** (sometimes called "pass by object reference").  
- If you pass a mutable object to a function and modify it, the change is visible outside the function.
- If you pass an immutable object, any "modification" inside the function does not affect the original object.

**Example:**
```python
def assign_value(n, v):
    n = v

l1 = [1, 2, 3]
l2 = [4, 5, 6]
assign_value(l1, l2)
print(l1)  # [1, 2, 3]  # Unchanged

def add_item(lst):
    lst.append(4)

l = [1, 2, 3]
add_item(l)
print(l)  # [1, 2, 3, 4]  # Changed
```
This distinction is essential for avoiding unexpected bugs in your code.

## Advanced: Interning, Tuples, and the `is` Operator

Python sometimes "interns" small integers and strings, meaning identical values may share the same memory address. For example, `a = 89; b = 89; a is b` is `True` because of interning. However, for larger objects like lists or most tuples, `is` will usually be `False` unless they are explicitly the same object.

**Example:**
```python
a = ()
b = ()
print(a is b)  # True (empty tuples are interned)

a = (1, 2)
b = (1, 2)
print(a is b)  # False (usually, not interned)
```
Always use `==` to compare values, and `is` only to check if two variables point to the exact same object.

---

**In summary**, this project taught me how Python handles objects, identity, mutability, and function arguments. Mastering these concepts is key to writing efficient and bug-free Python code.

---
