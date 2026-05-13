#!/usr/bin/env python3
"""This module defines a Square."""
Rectangle = __import__('2-rectangle').Rectangle


class Square(Rectangle):
    """A class representing a Square, inheriting from Rectangle"""
    def __init__(self, size):
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """Return the area of Square"""
        return self.__size * self.__size
