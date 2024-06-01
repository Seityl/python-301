# Create two classes that model a rectangle and a circle.
# The rectangle class should be constructed by length and width
# while the circle class should be constructed by radius.
#
# Write methods in the appropriate class so that you can calculate
# the area of both the rectangle and the circle, the perimeter
# of the rectangle, and the circumference of the circle.
import math

class Rectangle:
    """Calculate area of a rectangle."""
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def calcArea(self):
        area = self.length * self.width
        return area
    def calcPerimeter(self):
        perimeter = (self.length * 2) + (self.width * 2)
        return perimeter
    def __repr__(self):
        return f"Rectanle(length={self.length}, width= {self.width}, area={self.calcArea()}, perimeter={self.calcPerimeter()})"

class Circle:
    """Calculate area of a circle."""
    def __init__(self, radius):
        self.radius = radius
    def calcArea(self):
        area = math.pi * self.radius * self.radius
        return area
    def calcCirumference(self):
        cirucmference = 2 * math.pi * self.radius
        return cirucmference
    def __repr__(self):
        return f"Circle(radius={self.radius}, area={self.calcArea()}, circumference={self.calcCirumference()})"

r = Rectangle(5, 10)
c = Circle(5)

print(f"{r}\n{c}")