# 0x05. Python - Exceptions

## Table of Contents
* [Description](#description)
* [Python Exceptions](#python-exceptions)
* [Handling Exceptions](#handling-exceptions)
* [The `try-except` Block](#the-try-except-block)
* [Raising Exceptions](#raising-exceptions)
* [Cleaning Up with `finally`](#cleaning-up-with-finally)
* [Custom Exceptions](#custom-exceptions)
* [Conclusion](#conclusion)

## Description
Exceptions are events that occur during the execution of a program that disrupt the normal flow of instructions. Python provides a robust exception handling mechanism to handle and manage exceptions. This allows you to gracefully handle errors, perform cleanup operations, and control the flow of your program.

This README aims to provide an overview of Python exceptions, how to handle them, and various techniques related to exception handling.

## Python Exceptions
In Python, an exception is an object that represents an error condition. Exceptions can occur during runtime due to various reasons such as incorrect input, division by zero, file not found, etc. When an exception occurs, it interrupts the normal flow of the program and transfers control to the nearest exception handler.

Python has a built-in hierarchy of exception classes, with the base class being `BaseException`. Commonly encountered exceptions include `SyntaxError`, `TypeError`, `ValueError`, `ZeroDivisionError`, and `FileNotFoundError`, among others.

## Handling Exceptions
Exception handling allows you to catch and handle exceptions gracefully, preventing the program from terminating abruptly. By handling exceptions, you can provide alternative logic or error messages, perform cleanup operations, or log errors for debugging purposes.

## The `try-except` Block
The `try-except` block is used to catch and handle exceptions in Python. It allows you to specify a block of code that might raise an exception and define how to handle the exception if it occurs. The general syntax of a `try-except` block is as follows:

```python
try:
    # Code that may raise an exception
except ExceptionType:
    # Code to handle the exception
```

You can have multiple `except` clauses to handle different types of exceptions, or a single `except` clause to handle multiple exceptions.

## Raising Exceptions
In addition to handling built-in exceptions, you can also raise exceptions explicitly using the `raise` statement. This allows you to create your own custom exceptions or raise built-in exceptions with specific messages.

```python
raise ExceptionType("Error message")
```

Raising an exception allows you to signal exceptional conditions in your code and transfer control to an appropriate exception handler.

## Cleaning Up with `finally`
The `finally` block is used to specify cleanup code that must be executed regardless of whether an exception occurred or not. It is typically used to release resources, close files, or perform other cleanup operations that should always occur.

```python
try:
    # Code that may raise an exception
except ExceptionType:
    # Code to handle the exception
finally:
    # Cleanup code
```

The `finally` block is executed after the `try` block and any associated `except` blocks, regardless of whether an exception occurred or was handled.

## Custom Exceptions
Python allows you to define your own custom exceptions by creating a new class that inherits from the `Exception` class or one of its subclasses. Custom exceptions can be used to represent specific error conditions in your program and provide meaningful error messages.

```python
class CustomException(Exception):
    pass

# Raise custom exception
raise CustomException("Custom error message")
```

By creating custom exceptions, you can make your code more expressive and provide better error handling and reporting.

## Conclusion
Exception handling is an essential aspect of writing
