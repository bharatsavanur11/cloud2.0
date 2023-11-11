# A module in python is predefined set of functions and variables of all types
import math


def find_gct(a, b):
    return math.gcd(a, b)


print(find_gct(15, 3))


def max_num(a, b):
    return max(a, b)


print(max_num(10, 12))


def sum_natural_nos(n):
    if n <= 1:
        return 1
    else:
        return n + sum_natural_nos(n - 1)


print(sum_natural_nos(10))
