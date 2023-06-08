#!/usr/bin/python3

import sys
from decimal import Decimal

if __name__ == "__main__":
    """Prints the sum of all valid integer or decimal arguments as a string."""

    total = Decimal(0)
    for i in range(len(sys.argv) - 1):
        try:
            arg = sys.argv[i + 1]
            number = Decimal(arg)
            total += number
        except ValueError:
            print("Invalid argument: {}. Skipping...".format(arg))

    print("The sum of the valid numeric arguments is: {}".format(total))
