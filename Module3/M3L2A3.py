# M3L2A3: Factorial
# Activity 3: Recursion, Base Case, Recursive Case, and Docstring

def factorial(x):
    '''this is a recursive function to find the factorial of an integer'''
    if x == 0 or x == 1:
        return 1
    else:
        # Calling function inside itself (Recursion)
        return x * factorial(x - 1)

# Display docstring using __doc__
print("Docstring Explanation:")
print(factorial.__doc__)
print()

# Display factorial results
print("The factorial of 0:", factorial(0))
print("The factorial of 1:", factorial(1))
print("The factorial of 2:", factorial(2))
print("The factorial of 5:", factorial(5))
print("The factorial of 10:", factorial(10))
