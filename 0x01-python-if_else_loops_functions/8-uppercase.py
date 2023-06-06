#!/usr/bin/python3

def uppercase(string):
    """Print a string in uppercase."""
    for char in string:
        if ord(char) >= 97 and ord(char) <= 122:
            char = chr(ord(char) - 32)
        print(char, end="")
    print()
