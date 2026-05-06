#!/usr/bin/env python3
"""Module that contains the uppercase function"""


def uppercase(string):
    """print the string in uppercase followed by a new line."""
    for char in string:
        if char >= 'a' and char <= 'z':
            ascii = ord(char)
            code_uppercase = ascii - 32
            char = chr(code_uppercase)

        print("{}".format(char), end="")

    print()
