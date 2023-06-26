#!/usr/bin/python3

import sys


def safe_print_integer_err(value):
    """Prints an integer with "{:d}".format().

    If a ValueError message is caught, a corresponding
    message is printed to standard error.

    Args:
        value: The value to be printed.

    Returns:
        True if the value is an integer and has been printed correctly.
        False otherwise.
    """
    try:
        print("{:d}".format(value))
        return (True)
    except (TypeError, ValueError) as e:
        print("Exception: {}".format(e), file=sys.stderr)
        return (False)
