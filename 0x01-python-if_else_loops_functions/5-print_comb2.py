#!/usr/bin/python3

# Appends each letter and concatenate
output = ""
# prints numbers from 0 to 99.separated by ,, followed by a space
for number in range(100):
    if number == 99:
        output += "{:02}".format(number)
    else:
        output += "{:02}, ".format(number)
    print("{0:02}".format(number), end=", ")
