#!/usr/bin/python3
"""Add all arguments to a Python list and save them to a file."""

import sys
import json


def save_to_json_file(obj, filename):
    with open(filename, 'w') as file:
        json.dump(obj, file)


def load_from_json_file(filename):
    with open(filename, 'r') as file:
        return json.load(file)


if __name__ == "__main__":
    # Load existing list from file if it exists
    try:
        my_list = load_from_json_file("add_item.json")
    except FileNotFoundError:
        my_list = []

    # Add command-line arguments to the list
    my_list.extend(sys.argv[1:])

    # Save the updated list to the file
    save_to_json_file(my_list, "add_item.json")
