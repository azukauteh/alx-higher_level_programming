#!/usr/bin/python3

import sys

if __name__ == "__main__":
    """Prints the sum of all arguments as a string."""

    total = 0
    for i in range(len(sys.argv) - 1):
        total += int(sys.argv[i + 1])
    print("The sum of the arguments is: {}".format(total) + "\n")
