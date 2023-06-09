#!/usr/bin/python3
from calculator_1 import add, sub, mul, div

if __name__ == "__main__":
    # int args:
    a = 10
    b = 5

    # Perform calculations
    sum_result = add(a, b)
    diff_result = sub(a, b)
    mul_result = mul(a, b)
    div_result = div(a, b)

    # Print the results
    print("{} + {} = {}".format(a, b, sum_result))
    print("{} - {} = {}".format(a, b, diff_result))
    print("{} * {} = {}".format(a, b, mul_result))
    print("{} / {} = {}".format(a, b, div_result))
