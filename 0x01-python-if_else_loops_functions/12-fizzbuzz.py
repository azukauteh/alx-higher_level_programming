#!/usr/bin/python3

def fizzbuzz():
    # Print the numbers from 1 to 100 separated by a space.
    for number in range(1, 101):
        # For multiples of three and five, print FizzBuzz instead of the number
        if number % 3 == 0 and number % 5 == 0:
            print("FizzBuzz ", end="")
        # For multiples of three, print Fizz instead of the number.
        elif number % 3 == 0:
            print("Fizz ", end="")
        # For multiples of five, print Buzz instead of the number.
        elif number % 5 == 0:
            print("Buzz ", end="")
        else:
            print("{} ".format(number), end="")
