# M8L6ACP: Polygon Area Calculator & Shape Hierarchy
# Coding Grandmaster (Grades 9-12) - Module 8 Lesson 6 After Class Project
import math

class Shape:
    def area(self):
        raise NotImplementedError("Subclasses must implement area()")

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

class RegularPentagon(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        # Area = (1/4) * sqrt(5*(5+2*sqrt(5))) * side^2
        return 0.25 * math.sqrt(5 * (5 + 2 * math.sqrt(5))) * (self.side ** 2)

if __name__ == "__main__":
    shapes = [
        ("Square with side 6", Square(6)),
        ("Circle with radius 4", Circle(4)),
        ("Regular Pentagon with side 5", RegularPentagon(5))
    ]

    print("=" * 45)
    print(" POLYGON & SHAPES AREA CALCULATOR ")
    print("=" * 45)
    for name, s in shapes:
        print(f"{name:32} -> Area: {s.area():.2f} sq units")
    print("=" * 45)
