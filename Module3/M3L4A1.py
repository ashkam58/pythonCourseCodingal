# M3L4A1: Value Error
# Activity 1: Exception Handling - Catching ValueError with try and except

try:
    number = int(input("Enter a number: "))
    print("The number entered is", number)
except ValueError as ex:
    print("Exception:", ex)
