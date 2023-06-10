# Python - Data Structures: Lists, Tuples

This page  contains Python code examples and explanations for two fundamental data structures in Python: lists and tuples. The code samples provided demonstrate various operations and manipulations that can be performed on these data structures.

## Table of Contents

1. [Introduction](#introduction)
2. [Lists](#lists)
   - [Creating a List](#creating-a-list)
   - [Accessing Elements](#accessing-elements)
   - [Modifying Elements](#modifying-elements)
   - [List Operations](#list-operations)
   - [List Methods](#list-methods)
3. [Tuples](#tuples)
   - [Creating a Tuple](#creating-a-tuple)
   - [Accessing Elements](#accessing-elements-1)
   - [Modifying Elements](#modifying-elements-1)
   - [Tuple Operations](#tuple-operations)
   - [Tuple Methods](#tuple-methods)
4. [Conclusion](#conclusion)
5. [Contributing](#contributing)

## Introduction

Data structures are essential components of any programming language, as they provide a way to store, organize, and manipulate data efficiently. Python offers several built-in data structures, and two of the most commonly used ones are lists and tuples.

Lists are mutable sequences, meaning they can be modified after creation. They can contain elements of different data types and allow duplicates. Lists are often used when the order and the ability to modify elements are important.

Tuples, on the other hand, are immutable sequences, which means they cannot be modified once created. Tuples can also contain elements of different types and allow duplicates. Tuples are commonly used when the order of elements is important, but immutability is desired.

This repository provides examples and explanations of various operations that can be performed on lists and tuples, including creation, accessing elements, modifying elements, and performing common operations.

## Lists

### Creating a List

To create a list in Python, enclose the elements in square brackets ([]). Elements can be of any data type, and they can be separated by commas.

```python
my_list = [1, 2, 3, 'a', 'b', 'c']
```

### Accessing Elements

Elements in a list can be accessed using indexing. The index starts from 0 for the first element and increments by 1 for each subsequent element. Negative indexing can also be used, where -1 refers to the last element, -2 refers to the second-to-last element, and so on.

```python
my_list = [1, 2, 3, 4, 5]

print(my_list[0])   # Output: 1
print(my_list[3])   # Output: 4
print(my_list[-1])  # Output: 5
```

### Modifying Elements

Lists are mutable, meaning you can modify their elements after creation. You can assign new values to specific indices or use list methods to manipulate the list.

```python
my_list = [1, 2, 3, 4, 5]

my_list[2] = 'new value'
print(my_list)  # Output: [1, 2, 'new value', 4, 5]
```

### List Operations

Python provides several operations that can be performed on lists, including concatenation, repetition, and slicing.

```python
list1 = [1, 2, 3]
list2 = [4, 5, 6]

concatenated = list1 + list2
print(concatenated)  # Output: [1, 2,
