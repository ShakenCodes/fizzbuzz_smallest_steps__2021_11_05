# -*- coding: utf-8 -*-
import unittest
from fizzbuzz import fizzbuzz_thirty

class TestFizzBuzz(unittest.TestCase):

    def test_fizzbuzz_thirty(self):
        expected = \
            "1\n" \
            "2\n" \
            "fizz\n" \
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
        self.assertEqual(fizzbuzz_thirty(), expected)

if __name__ == '__main__':
    unittest.main()