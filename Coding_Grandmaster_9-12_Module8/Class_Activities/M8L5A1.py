# M8L5A1: Employee Details (Inheritance)
# Coding Grandmaster (Grades 9-12) - Module 8 Lesson 5 Activity 1

# Parent Class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_person_details(self):
        print(f"Name: {self.name}, Age: {self.age}")

# Child Class inheriting from Person
class Employee(Person):
    def __init__(self, name, age, emp_id, salary, department):
        super().__init__(name, age) # Call parent constructor
        self.emp_id = emp_id
        self.salary = salary
        self.department = department

    def display_employee_details(self):
        self.display_person_details()
        print(f"Employee ID: {self.emp_id}")
        print(f"Department: {self.department}")
        print(f"Monthly Salary: ${self.salary}")

emp = Employee("Ashkam Anwar", 25, "EMP-108", 4500, "Software Engineering")
emp.display_employee_details()
