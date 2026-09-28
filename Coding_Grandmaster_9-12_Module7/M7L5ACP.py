# ================================================================
# Course: AI & Coding Grandmaster Course training (Grades 9-12)
# Module 7: Introduction to Python
# Lesson 5: Functions
# After-Class Project (ACP): Fibonacci Series
# File: M7L5ACP.py
# ================================================================

# ================================
# FIBONACCI SERIES USING RECURSION
# ================================

# Recursive function to find the nth Fibonacci number
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# Take input from the user for the number of terms
terms = int(input("Enter the number of terms: "))

# Check if the number of terms is valid
if terms <= 0:
    print("Please enter a positive integer.")
else:
    print("Fibonacci sequence:")
    # Loop to print the series up to the specified number of terms
    for i in range(terms):
        print(fibonacci(i), end=" ")
    print()
