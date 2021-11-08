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
    result = if_divisible_by_three_then_fizz(n)
    result = if_divisible_by_five_append_buzz(n, result)
    return if_length_is_zero_result_is_number(n, result)

def if_divisible_by_three_then_fizz(n):
    if n % 3 != 0: return ""
    return "fizz"
def if_divisible_by_five_append_buzz(n, result):
    if n % 5 != 0: return result
    return result + "buzz"
def if_length_is_zero_result_is_number(n, result):
    if len(result) == 0: return str(n)
    return result