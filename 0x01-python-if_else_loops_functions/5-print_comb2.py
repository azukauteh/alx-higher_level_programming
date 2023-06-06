#!/usr/bin/python3
# prints numbers from 0 to 99.separated by ,, followed by a space
for number in range(100):
    if number == 99:
        print("{:02}".format(number) + "\n")
    else:
        print("{:02}".format(number), end=", ")
