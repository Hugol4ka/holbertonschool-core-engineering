#!/usr/bin/env python3
"""This module provides a function to append text to a file."""


def append_write(filename="", text=""):
    """Appends a string at the end of a UTF-8 text file and returns characters added."""
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
