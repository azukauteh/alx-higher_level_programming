# 0x0A. Python - Inheritance

## Description
This directory contains Python programs written for ALX_africa software engoneering 0x0A. Python - Inheritance project. The code in this project demonstrates the concept of inheritance in Python.

## Learning Objectives
- What is a superclass, baseclass, or parentclass?
- What is a subclass?
- How to list all attributes and methods of a class or instance?
- When can an instance have new attributes?
- How to inherit class from another?
- How to define a class with multiple base classes?
- What is the default class every class inherit from?
- How to override a method or attribute inherited from the base class?
- Which attributes or methods are available by heritage to subclasses?
- What is the purpose of inheritance?

## Files
- `0-lookup.py`: A function that returns the list of available attributes and methods of an object.
- `1-my_list.py`: A class `MyList` that inherits from the built-in `list` class and adds a method to print the sorted list.
- `2-is_same_class.py`: A function that checks if an object is an instance of a specified class.
- `3-is_kind_of_class.py`: A function that checks if an object is an instance of a class or a class that inherited from the specified class.
- `4-inherits_from.py`: A function that checks if an object is an instance of a class that inherited (directly or indirectly) from the specified class.
- `5-base_geometry.py`: An empty class `BaseGeometry`.
- `6-base_geometry.py`: A class `BaseGeometry` with a public instance method `area()` that raises an `Exception` with the message "area() is not implemented".
- `7-base_geometry.py`: A class `BaseGeometry` with a public instance method `area()` that raises a `NotImplementedError` with the message "area() is not implemented"
- `8-rectangle.py`: A class `Rectangle` that inherits from `BaseGeometry` and adds `width` and `height` attributes validation.
- `9-rectangle.py`: A class `Rectangle` that inherits from `BaseGeometry` and overrides the `area()` method.
- `10-square.py`: A class `Square` that inherits from `Rectangle` and adds a `size` attribute validation.

## Usage
```python
$ ./main_files/0-main.py
```

## Author
This project is authored by Azuka Uteh.
