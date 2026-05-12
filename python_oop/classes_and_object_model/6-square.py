#!/usr/bin/env python3
"""This module defines a Square class."""


class Square:
    """A class that defines a square by its size."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize the square with a private size attribute."""
        self.size = size
        self.position = position

    def area(self):
        """Calculates the current square area."""
        return self.__size * self.__size

    @property
    def size(self):
        """recovers size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter pour la taille."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @position.setter
    def position(self, value):
        """Setter pour la position."""
        if (not isinstance(value, tuple) or len(value) != 2 or
                not isinstance(value[0], int) or value[0] < 0 or
                not isinstance(value[1], int) or value[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value


    def my_print(self):
        "Display square whit #"
        if self.size == 0:
            print("")

        for i in range(self.position):
            print("")
        
        for i in range(self.size):
            print(" " * self.position[0] + "#" * self.size)

        def __str__(self):
            """Transforme l'objet Square en une chaîne de caractères."""
            if self.size == 0:
                return ""
        
            lignes = []

            for i in range(self.position[1]):
                lignes.append("")

            for i in range(self.size):

                one_ligne = (" " * self.position[0]) + ("#" * self.size)
                lignes.append(one_ligne)

            return "\n".join(lignes)
