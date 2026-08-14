# M4L4A1: Value Error
# Activity 1: Exception Handling - Catching ValueError with try and except

# Using a try and except block
try:
    number = int(input("Enter a number: "))
    print("The number entered is", number)
# Using ValueError exception object
except ValueError as ex:
    print("Exception:", ex)
