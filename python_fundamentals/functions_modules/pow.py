#!/usr/bin/env python3
"""Module that contains the pow function."""


def pow(a, b):
    """Return the value of a raised to the power of b."""
    result = 1
    # _ pour ne pas lire une varible
    for _ in range(b):
        result = result * a
    return result
