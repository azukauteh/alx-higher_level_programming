#!/usr/bin/python3

# Appends each letter and concatenate
output = ""
# Print all the alphabet letters except 'q' and 'e'
for letter in range(97, 123):
    if chr(letter) != 'q' and chr(letter) != 'e':
        output += chr(letter)
        print("{}".format(chr(letter)), end="")
