#!/usr/bin/python3

import hidden_4

if __name__ == "__main__":
    """Print all names defined by hidden_4 module."""
    names = dir(hidden_4)
    for name in names:
        if not name.startswith("__"):
            print(name + "\n")
