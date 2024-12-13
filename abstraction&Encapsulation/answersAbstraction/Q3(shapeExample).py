from abc import ABC, abstractmethod
import math

# Abstract class
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

# Concrete classes
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return math.pi * (self.radius ** 2)

class Square(Shape):
    def __init__(self, side):
        self.side = side
    
    def area(self):
        return self.side ** 2

# Testing the classes
circle = Circle(5)
square = Square(4)
print(f"Circle Area: {circle.area()}")
print(f"Square Area: {square.area()}")
