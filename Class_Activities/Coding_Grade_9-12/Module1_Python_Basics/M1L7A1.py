# M1L7A1: Functions & Parameters
# Activity 1: Defining simple user-defined functions and passing parameters

def greet_user(name):
    print(f"Hello, {name}! Welcome to Python programming.")

def add_numbers(num1, num2):
    return num1 + num2

greet_user("Alice")
result = add_numbers(12, 18)
print("Sum of 12 and 18 is:", result)
