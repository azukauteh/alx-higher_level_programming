# 0x08. Python - More Classes and Objects

This directory contains solutions to the tasks and exercises for the "0x08. Python - More Classes and Objects" project in the higher-level programming track of ALX_afric Software Engineering School.

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

- Python 3.4 or later
- All files are executed with the Python interpreter using the following command: `python3 file.py`

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

## Authors

- azuka uteh (@aazure263@gmail.com)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

Please note that the content of this README file is for demonstration purposes only, and you should tailor it to fit the specific requirements and details of your project.
