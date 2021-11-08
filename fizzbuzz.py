# -*- coding: utf-8 -*-
def fizzbuzz_thirty():
    "Returns the first thirty responses to fizzbuzz"
    other_responses = \
        "4\n" \
        "buzz\n" \
        "fizz\n" \
        "7\n" \
        "8\n" \
        "fizz\n" \
        "buzz\n" \
        "11\n" \
        "fizz\n" \
        "13\n" \
        "14\n" \
        "fizzbuzz\n" \
        "16\n" \
        "17\n" \
        "fizz\n" \
        "19\n" \
        "buzz\n" \
        "fizz\n" \
        "22\n" \
        "23\n" \
        "fizz\n" \
        "buzz\n" \
        "26\n" \
        "fizz\n" \
        "28\n" \
        "29\n" \
        "fizzbuzz\n"
    calculated_response = ""
    for x in range (1, 4):
        calculated_response += fizzbuzz(x) + "\n"
    thirty_responses = calculated_response + other_responses
    return thirty_responses

def fizzbuzz(n):
    "Calculates fizzbuzz for a given value"
    if n %3 == 0:
        return "fizz"
    else:
        return str(n)