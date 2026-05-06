#!/usr/bin/env python3
"""Module that contains the islower function"""


def islower(c):
    """Check if the c character is lowercase"""
    ascii_value = ord(c)

    if ascii_value >= 97 and ascii_value <= 122:
        return True
    else:
        return False
