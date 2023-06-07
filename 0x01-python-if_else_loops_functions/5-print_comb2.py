#!/usr/bin/python3

# Appends each number and concatenates them
output = ""
# Prints numbers from 0 to 99, separated by a comma followed by a new line
for number in range(100):
    output += "{:02}".format(number)
    if number != 99:
        output += ", "
print(output)
