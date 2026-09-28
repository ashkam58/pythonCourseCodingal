# ================================================================
# Course: AI & Coding Grandmaster Course training (Grades 9-12)
# Module 7: Introduction to Python
# Lesson 4: Loops
# Activity 2: Star Pattern
# File: M7L4A2.py
# ================================================================

# Python program to print a star pattern based on the number of rows specified by the user

# Get the number of rows from user
n = int(input("Enter the number of rows: "))

# Outer loop for each row
for i in range(1, n + 1):
    # Inner loop for each column in the row
    for j in range(i):
        # Print star, end with space instead of new line
        print('*', end=' ')
    # After each row, print a new line
    print()
