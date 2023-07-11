#!/usr/bin/python3
"""defines a function that returns an object"""
import json


def from_json_string(my_str):
    """Returns the object (Python data structure)

    represented by a JSON string."""
    return json.loads(my_str)
