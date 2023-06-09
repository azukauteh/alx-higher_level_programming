#!/usr/bin/python3.8
import sys


def print_names():
    """Print all names defined in the hidden_4 module."""
    import hidden_4
    names = dir(hidden_4)
    for name in sorted(names):
        if not name.startswith("__"):
            print(name + "\n")


if __name__ == "__main__":
    print_names()
