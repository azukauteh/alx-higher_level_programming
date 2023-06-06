#!/usr/bin/python3

# Appends each letter and concatenate
output = ""
# Prints numbers from 0 to 99, separated by ", ", with the last number followed by a new line
for number in range(100):
    if number == 99:
        output += "{:02}".format(number)
    else:
        output += "{:02}".format(number)
    print( "{:02},".format(number), end="")
