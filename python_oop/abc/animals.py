#!/usr/bin/env python3
from abc import ABC, abstractmethod


class Animal(ABC):
    """Abstract class for all animals"""
    @abstractmethod
    def sound(self):
        """Abstract method that subclasses MUST implement"""
        pass

class Dog(Animal):
    """Dog class inheriting from Animal"""
    
    def sound(self):
        """Returns the specific sound of a dog"""
        return "Bark"
    
class Cat(Animal):
    """Cat class inheriting from Animal"""

    def sound(self):
        """Returns the specific sound of a cat"""
        return "Meow"
