#!/usr/bin/env python3
"""Module that contains the uppercase function"""


def uppercase(string):
    """print the string in uppercase followed by a new line."""
    for char in string:
        if ord(char) >= 97 and ord(char) <= 122:
            ascii_code = ord(char)
            upper_code = ascii_code - 32
            char = chr(upper_code)
        print("{}".format(char), end="")
    print("")
