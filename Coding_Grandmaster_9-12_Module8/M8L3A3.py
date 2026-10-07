# M8L3A3: Parrot Bird
# Coding Grandmaster (Grades 9-12) - Module 8 Lesson 3 Activity 3

class Parrot:
    # Class attribute
    species = "Bird"

    # Instance attributes
    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color

    # Instance method
    def sing(self, song):
        return f"{self.name} sings '{song}'!"

    def dance(self):
        return f"{self.name} is now dancing joyfully!"

# Instantiate the Parrot class
blu = Parrot("Blu", 3, "Blue")
woo = Parrot("Woo", 5, "Green")

print(f"{blu.name} is a {blu.species} with {blu.color} feathers and is {blu.age} years old.")
print(f"{woo.name} is a {woo.species} with {woo.color} feathers and is {woo.age} years old.")

print(blu.sing("Happy Tunes"))
print(woo.dance())
