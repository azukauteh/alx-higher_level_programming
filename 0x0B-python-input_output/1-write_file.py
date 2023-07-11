#!/usr/bin/python3
"""Defines a text file line-counting function."""


def write_file(filename="", text=""):
    """Writes a string to a text file,returns number of characters written."""
    with open(filename, mode='w', encoding='utf-8') as f:
        f.write(text)
        return len(text)
