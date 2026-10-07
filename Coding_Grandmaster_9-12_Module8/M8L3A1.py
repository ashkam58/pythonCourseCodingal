# M8L3A1: Class Student
# Coding Grandmaster (Grades 9-12) - Module 8 Lesson 3 Activity 1

# Defining the Student class
class Student:
    # Class attribute
    school_name = "Codingal Academy"
    
    # Instance attributes inside constructor
    def __init__(self, name, roll_no, grade):
        self.name = name
        self.roll_no = roll_no
        self.grade = grade

    # Method to display student details
    def display_info(self):
        print(f"Student: {self.name} | Roll No: {self.roll_no} | Grade: {self.grade} | School: {Student.school_name}")

# Creating instances of Student class
student1 = Student("Ashkam", 101, 10)
student2 = Student("Rohan", 102, 10)

# Calling methods
student1.display_info()
student2.display_info()
