# M8L5ACP: Polygon Area Calculator
# Coding Grandmaster (Grades 9-12) - Module 8 Lesson 5 After Class Project
from abc import ABC, abstractmethod

class Polygon(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Rectangle(Polygon):
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth

    def perimeter(self):
        return 2 * (self.length + self.breadth)

class Triangle(Polygon):
    def __init__(self, base, height, side1, side2):
        self.base = base
        self.height = height
        self.side1 = side1
        self.side2 = side2

    def area(self):
        return 0.5 * self.base * self.height

    def perimeter(self):
        return self.base + self.side1 + self.side2

if __name__ == "__main__":
    rect = Rectangle(10, 5)
    print("Rectangle Area:", rect.area())
    print("Rectangle Perimeter:", rect.perimeter())

    tri = Triangle(6, 4, 5, 5)
    print("Triangle Area:", tri.area())
    print("Triangle Perimeter:", tri.perimeter())
