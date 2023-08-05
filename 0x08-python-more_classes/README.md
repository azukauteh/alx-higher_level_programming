# 0x08. Python - More Classes and Objects

![Author](https://img.shields.io/badge/Author-AzukaUteh-blue.svg)


This directory contains solutions to the tasks and exercises for the "0x08. Python - More Classes and Objects" project in the higher-level programming track of ALX_afric Software Engineering.

## Description

The "0x08. Python - More Classes and Objects" project covers various topics related to object-oriented programming (OOP) in Python. It explores advanced concepts and techniques for defining classes, creating objects, and working with class attributes and methods. The project also delves into topics such as class inheritance, method overriding, class composition, and static methods.

## Files

- `0-rectangle.py`: This file contains the implementation of the `Rectangle` class. The class represents a rectangle shape and provides functionality for calculating its area and perimeter.

- `1-rectangle.py`: This file builds on `0-rectangle.py` and adds functionality to the `Rectangle` class to validate and set the width and height attributes.

- `2-rectangle.py`: This file builds on `1-rectangle.py` and adds functionality to the `Rectangle` class to implement string representation of the rectangle using `__str__` method.

- `3-rectangle.py`: This file builds on `2-rectangle.py` and adds functionality to the `Rectangle` class to implement representation of the rectangle that can be used to recreate a new instance of the class using `__repr__` method.

- `4-rectangle.py`: This file builds on `3-rectangle.py` and adds functionality to the `Rectangle` class to delete instances of the class and track the number of instances using `__del__` method.

- `5-rectangle.py`: This file builds on `4-rectangle.py` and adds functionality to the `Rectangle` class to print a message when an instance of the class is deleted using `__del__` method.

- `6-rectangle.py`: This file builds on `5-rectangle.py` and adds functionality to the `Rectangle` class to implement static methods that compare two rectangles based on their areas.

## Requirements


Allowed editors: vi, vim, emacs

All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)

All your files should end with a new line

The first line of all your files should be exactly #!/usr/bin/python3

Your code should use the pycodestyle (version 2.8.*)

All your files must be executable

The length of your files will be tested using wc

## Usage

To use the `Rectangle` class, follow these steps:

1. Import the class into your Python script:
    ```python
    from rectangle import Rectangle
    ```

2. Create an instance of the `Rectangle` class:
    ```python
    rectangle = Rectangle(5, 3)
    ```

3. Use the available methods to interact with the rectangle object. For example:
    ```python
    # Calculate the area of the rectangle
    area = rectangle.area()
    print("Area:", area)

    # Calculate the perimeter of the rectangle
    perimeter = rectangle.perimeter()
    print("Perimeter:", perimeter)

    # Print the string representation of the rectangle
    print(rectangle)

    # Recreate a new instance of the rectangle
    new_rectangle = eval(repr(rectangle))
    print(new_rectangle)

    # Delete the rectangle instance
    del rectangle
    ```

4. Run your Python script and observe the output.
