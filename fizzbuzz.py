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
    result = ""
    if n % 3 == 0:
        result += "fizz"
    if n % 5 == 0:
        result += "buzz"
    if len(result) == 0:
        result = str(n)
    return result