#!/usr/bin/env python3
"""This module provides a function to read and print file contents."""


def read_file(filename=""):
    """Reads a UTF-8 text file and prints its content to stdout."""
    with open(filename, encoding="utf-8") as r:
        print(r.read(), end="")
