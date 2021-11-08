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
    return if_length_is_zero_result_is_number(n, result)

def if_length_is_zero_result_is_number(n, result):
    if len(result) == 0:
        return str(n)
    return result