#!/usr/bin/python3
"""defines JSON representation of a string object"""


def to_json_string(my_obj):
    """Returns the JSON representation of a string object."""
    json_string = '"' + my_obj.replace('"', r'\"') + '"'
    return json_string
