# -*- coding: utf-8 -*-
from unittest import result


def fizzbuzz_thirty():
    "Returns the first thirty responses to fizzbuzz"
    result = ""
    for x in range (1, 31):
        result += fizzbuzz(x) + "\n"
    return result

def fizzbuzz(n):
    "Calculates fizzbuzz for a given value"
    if n % 15 == 0:
        return "fizzbuzz"
    elif n % 3 == 0:
        return "fizz"
    elif n % 5 == 0:
        return "buzz"
    else:
        return str(n)