#!/usr/bin/env python3
"""Module that contains the last digit function"""


def print_last_digit(number):
    """Displays and returns the last digit of a number."""
    last_digit = abs(number) % 10
    print(last_digit, end="")
    return last_digit
