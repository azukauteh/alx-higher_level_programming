#!/usr/bin/python3

def safe_print_integer(value):
    """Print an integer using "{:d}".format().

    Args:
        value: The value to be printed.

    Returns:
        True if the value is an integer and has been printed correctly.
        False otherwise.
    """
    try:
        print("{:d}".format(value))
        return (True)
    except (ValueError, TypeError):
        return (False)
