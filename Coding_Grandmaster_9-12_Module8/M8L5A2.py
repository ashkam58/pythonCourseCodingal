# M8L5A2: Student Details (Multilevel Inheritance)
# Coding Grandmaster (Grades 9-12) - Module 8 Lesson 5 Activity 2

# Base class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# Intermediate class
class AcademicRecord(Person):
    def __init__(self, name, age, stream, year):
        super().__init__(name, age)
        self.stream = stream
        self.year = year

# Derived class
class Student(AcademicRecord):
    def __init__(self, name, age, stream, year, marks):
        super().__init__(name, age, stream, year)
        self.marks = marks

    def display_full_profile(self):
        print("=" * 40)
        print(f"Student: {self.name} (Age: {self.age})")
        print(f"Stream: {self.stream}, Year: {self.year}")
        print(f"Percentage: {self.marks}%")
        print("=" * 40)

student = Student("Ashkam", 17, "Computer Science", 12, 94.5)
student.display_full_profile()
