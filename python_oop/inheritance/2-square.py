#!/usr/bin/env python3
"""Module that defines a Square class based on 1-square.py"""
Square = __import__('1-square').Square


class Square(Square):
    """A class Square that inherits from Square (the previous version)"""
    def __str__(self):
        """
        Returns the square description: [Square] <width>/<height>
        This method is called by print() and str()
        """
        return f"[Square] {self.__size}/{self.__size}"
