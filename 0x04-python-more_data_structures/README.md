# README - 0x04 Python - More Data Structures: Set, Dictionary

This README provides an overview and examples of working with two important data structures in Python: sets and dictionaries. These data structures are commonly used for efficient manipulation and organization of data in various Python applications.

## Table of Contents

- [Sets](#sets)
  - [Creating a Set](#creating-a-set)
  - [Adding and Removing Elements](#adding-and-removing-elements)
  - [Set Operations](#set-operations)
- [Dictionaries](#dictionaries)
  - [Creating a Dictionary](#creating-a-dictionary)
  - [Accessing and Modifying Values](#accessing-and-modifying-values)
  - [Dictionary Operations](#dictionary-operations)

## Sets

A set is an unordered collection of unique elements. It is useful when you want to store multiple items without any particular order and ensure that each item is unique.

### Creating a Set

In Python, you can create a set by enclosing comma-separated values inside curly braces `{}` or by using the `set()` constructor.

```python
# Creating a set using curly braces
fruits = {'apple', 'banana', 'orange'}

# Creating a set using set() constructor
fruits = set(['apple', 'banana', 'orange'])
```

### Adding and Removing Elements

You can add elements to a set using the `add()` method or remove elements using the `remove()` or `discard()` methods.

```python
fruits.add('grape')    # Adding a single element
fruits.update(['kiwi', 'melon'])    # Adding multiple elements

fruits.remove('banana')    # Removing an element (raises an error if not found)
fruits.discard('watermelon')    # Removing an element (no error if not found)
```

### Set Operations

Sets support various operations like union, intersection, difference, and more.

```python
set1 = {1, 2, 3}
set2 = {3, 4, 5}

set_union = set1.union(set2)        # Union of set1 and set2
set_intersection = set1.intersection(set2)    # Intersection of set1 and set2
set_difference = set1.difference(set2)    # Difference of set1 and set2

# Checking if a set is a subset or superset of another set
is_subset = set1.issubset(set2)
is_superset = set1.issuperset(set2)
```

## Dictionaries

A dictionary is an unordered collection of key-value pairs. Each key in the dictionary must be unique, and it allows efficient retrieval and modification of values based on their keys.

### Creating a Dictionary

In Python, dictionaries can be created by enclosing key-value pairs inside curly braces `{}` or by using the `dict()` constructor.

```python
# Creating a dictionary using curly braces
student = {'name': 'John', 'age': 20, 'major': 'Computer Science'}

# Creating a dictionary using dict() constructor
student = dict(name='John', age=20, major='Computer Science')
```

### Accessing and Modifying Values

You can access the values in a dictionary using their respective keys. Additionally, you can modify values or add new key-value pairs.

```python
name = student['name']    # Accessing value using key

student['age'] = 21    # Modifying value
student['gpa'] = 3.8    # Adding a new key-value pair
```

### Dictionary Operations

Dictionaries provide several operations for manipulating and retrieving data.

```python
student = {'name': 'John', 'age': 20, 'major
