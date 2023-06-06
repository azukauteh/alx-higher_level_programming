#!/usr/bin/python3
import random
# Generate a random number between -10000 and 10000
number = random.randint(-10000, 10000)
# Calculate the last digit of the number
digit = abs(number) % 10
digit = -digit
# Print the output statement
print("Last digit of {} is {} and is ".format(number, digit), end="")
# Check the value of the last digit and print the appropriate statement
if digit > 5:
    print("greater than 5")
elif digit == 0:
    print("0")
else:
    print("less than 6 and not 0" + "\n")
