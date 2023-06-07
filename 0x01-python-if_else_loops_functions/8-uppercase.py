#!/usr/bin/python3

# Function to convert a string to uppercase
def uppercase(string):
    uppercase_str = ""

    # Iterate through each character in the string
    for char in string:
        # Convert lowercase character to uppercase
        uppercase_char = chr(ord(char) - 32) if 'a' <= char <= 'z' else char
        uppercase_str += uppercase_char

    # Print the uppercase string
    print(uppercase_str)
