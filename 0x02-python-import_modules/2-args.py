#!/usr/bin/python3

import sys

# Display the count and list of arguments.
count = len(sys.argv) - 1
if count == 0:
    print("There are no arguments.")
elif count == 1:
    print("There is 1 argument:")
else:
    print("There are {} arguments:".format(count))
for i in range(count):
    print("{}: {}".format(i + 1, arg))
