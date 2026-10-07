# M8L5A3: Animal Class (Abstraction)
# Coding Grandmaster (Grades 9-12) - Module 8 Lesson 5 Activity 3
from abc import ABC, abstractmethod

# Abstract Base Class
class Animal(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def make_sound(self):
        pass

    @abstractmethod
    def move(self):
        pass

# Concrete Child Classes
class Dog(Animal):
    def make_sound(self):
        return f"{self.name} says: Woof! Woof!"

    def move(self):
        return f"{self.name} runs energetically on 4 legs."

class Bird(Animal):
    def make_sound(self):
        return f"{self.name} says: Chirp! Chirp!"

    def move(self):
        return f"{self.name} flies gracefully in the sky."

dog = Dog("Buddy")
bird = Bird("Sky")

print(dog.make_sound())
print(dog.move())
print(bird.make_sound())
print(bird.move())
