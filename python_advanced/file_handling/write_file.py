#!/usr/bin/env python3
"""This module provides a function to write file contents."""


def write_file(filename="", text=""):
    """Writes a string to a UTF-8 text file and returns the
    number of characters."""
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
