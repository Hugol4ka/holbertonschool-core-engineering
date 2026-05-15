#!/usr/bin/env python3
"""Module that defines shapes using ABC and duck typing"""
from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """Abstract class for shapes"""
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Circle(Shape):
    """Concrete class representing a circle"""
    def __init__(self, radius):
        self.__radius = radius

    def area(self):
        return math.pi * (self.__radius ** 2)

    def perimeter(self):
        return 2 * math.pi * self.__radius


class Rectangle(Shape):
    """Concrete class representing a rectangle"""
    def __init__(self, width, height):
        self.__width = width
        self.__height = height

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        return 2 * (self.__width + self.__height)


def shape_info(shape):
    """Prints info about a shape using duck typing"""
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")
