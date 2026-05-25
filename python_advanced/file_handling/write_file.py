#!/usr/bin/env python3


def write_file(filename="", text=""):
    """This module provides a function to write file contents."""
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
