#!/usr/bin/env python3
"""This module defines a Square class."""


class Square:
    """A class that defines a square by its size."""

    def __init__(self, size=0):
        """Initialize the square with a private size attribute."""
        self.size = size

    def area(self):
        """Calculates the current square area."""
        return self.__size * self.__size

    @property
    def size(self):
        """recovers size"""
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
