#!/usr/bin/env python3
"""Module that contains the pow function."""


def pow(a, b):
    """Return the value of a raised to the power of b."""
    result = 1
    # _ to avoid reading a variable
    for _ in range(abs(b)):
        result = result * a
    # For negative exponents
    if b < 0:
        result = 1 / result
    return result
