#!/usr/bin/python3
"""Appends a string to end of file function."""


def append_write(filename="", text=""):
    """Appends a string to the end of a text file and
    returns the number of characters added."""
    with open(filename, mode='a', encoding='utf-8') as f:
        f.write(text)
        return len(text)
