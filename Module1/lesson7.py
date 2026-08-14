# Python Operators III
# In this lesson, you learn about identity, membership, and bitwise operators in Python. You explore how identity operators compare objects in memory, how membership operators check if items exist in lists or strings, and how bitwise operators work with binary numbers. By the end, you confidently use each operator in the right situations.

# Overview
# Activities
# Outcome
# Agenda
# Overview
# Topics Covered
# What are Identity Operators?
# Understanding 'is' and 'is not'
# What are Membership Operators?
# Using 'in' and 'not in'
# What are Bitwise Operators?
# Binary Numbers and Bits
# Hands-On Activities


# Topics in Details

# 1. Identity Operators
# What It Is
# Identity operators are special tools in Python that help you check if two variables are pointing to the EXACT SAME object in the computer's memory. This is different from checking if two things are equal!

# Think of it like this: You and your friend might have the same type of phone (equal), but you each have your own separate phone (different identity). Or, you might both be looking at the SAME phone together (same identity).



 

# Python gives us two identity operators:
 

# Operator

# Description

# Example

# is

# Returns True if both variables point to the same object in memory

# x is y

# is not

# Returns True if both variables point to different objects

# x is not y



 

# ANALOGY: The Twin Houses

# Imagine two houses that look exactly the same from outside - same color, same windows, same door.

# If you ask 'Are these houses EQUAL?' the answer is YES because they look the same.

# But if you ask 'Are these the SAME house?' the answer is NO - they are two different buildings!

# The 'is' operator checks if two things are literally the SAME object, not just look-alike copies.

 

# How It Works
# When you create a variable in Python, the computer stores its value somewhere in memory. The 'is' operator checks if two variables are stored at the EXACT same location.
 

# Here's a simple example:
 

# a = [1, 2, 3, 4, 5]    # Create a list

# b = [1, 2, 3, 4, 5]    # Create another list with same values

# c = a                   # c points to the SAME list as a


# print(a is c)          # True - same object!

# print(a is b)          # False - different objects

# print(a is not c)      # False

# print(a is not b)      # True
 

# Output:
 

# True

# False

# False

# True


 

 

# REAL-WORLD EXAMPLE: Social Media Accounts

# Imagine you have an Instagram account. Your best friend also has an Instagram account.

# Both accounts can have the same profile picture (equal content), but they are DIFFERENT accounts.

# However, if you share your login with your sibling, you're both using the SAME account (same identity).

# In programming: same values ≠ same object, just like same photo ≠ same account!

 

# WHY THIS MATTERS:

# Understanding identity operators is crucial when working with lists, dictionaries, and other complex data types.

# Sometimes you want to check if two variables point to the SAME object (not just equal values).

# This helps prevent bugs where changing one variable accidentally changes another!

# Professional programmers use this to write safer, more predictable code.

 

# 2. Membership Operators
# What It Is
# Membership operators are like detectives that help you find out if something exists inside a collection. They search through lists, strings, tuples, and other sequences to tell you if a value is there or not.


 

# These operators are super useful when you need to check if a word is in a sentence, if a number is in a list, or if a character is in a string!
 

# Operator

# Description

# Example

# in

# Returns True if a value is found in the sequence

# a in b

# not in

# Returns True if a value is NOT found in the sequence

# a not in b


 

 

# ANALOGY: The Guest List

# Imagine you're at a party and there's a guest list at the door.

# The bouncer checks: 'Is your name IN the list?' If yes, you can enter!

# The 'in' operator works exactly like this - it checks if something is on the list.

# And 'not in' is like asking 'Is this person NOT on the guest list?'

 

# How It Works
# You can use membership operators with strings, lists, tuples, and other sequences. Python will search through the entire sequence to find a match.
 

# # Checking in a list

# a = [1, 2, 3, 4, 5]

# b = [1, 2, 3, 4, 5]

# c = a


# print(a in c)          # Checking if list a is in c

# print(a not in b)      # Checking if a is NOT in b

# print(a in c)          # False - because c IS a

# print(a not in b)      # True - a is not inside b
 

# Output:
 

# False

# True

# False

# True

 

# More practical example with strings:
 

# # Checking in strings

# sentence = 'Hello World'


# print('Hello' in sentence)      # True - 'Hello' is found!

# print('Python' in sentence)     # False - 'Python' not found

# print('xyz' not in sentence)    # True - 'xyz' is NOT there
 

# REAL-WORLD EXAMPLE: Search Engines

# When you search on Google, it uses membership-like operations to find your search words.

# Google checks: 'Is the word "pizza" IN this website?' - similar to Python's 'in' operator!

# Spam filters also use this: 'Is the word "free money" in this email?' If yes, mark as spam!

# Video games check: 'Is the player's username in the banned list?' before allowing login.


 

 

# WHY THIS MATTERS:

# Membership operators make searching super easy and readable in Python.

# Instead of writing loops to search through items, you can simply use 'in' or 'not in'.

# This is used everywhere: validating user input, filtering data, checking passwords!

# Games use this to check if a player has a specific item in their inventory.

 

# 3. Bitwise Operators
# What It Is
# Bitwise operators are special operators that work directly with the 0s and 1s (called bits) that computers use to store numbers. While we see numbers like 5 or 10, computers actually store them as patterns of 0s and 1s!

# These operators are like tiny switches that can flip, compare, and move these 0s and 1s around. They're super fast because they work at the most basic level of how computers think!


 

# Understanding Binary (0s and 1s)
# Before we learn bitwise operators, let's understand how computers see numbers:

# • Number 5 in binary: 0101

# • Number 3 in binary: 0011

# Each 0 or 1 is called a "bit" - the smallest piece of data a computer can handle!
 

# ANALOGY: Light Switches

# Imagine a row of 4 light switches in your room. Each switch can be ON (1) or OFF (0).

# The pattern of ON/OFF switches represents a number! Like: OFF-ON-OFF-ON = 0101 = 5

# Bitwise AND is like checking: 'Are BOTH switches ON?' - only then result is ON.

# Bitwise OR is like: 'Is AT LEAST ONE switch ON?' - then result is ON.

# This is exactly how computers work with numbers at the deepest level!




 

# Operator

# Name

# Description

# &

# AND

# Result is 1 only if BOTH bits are 1

# |

# OR

# Result is 1 if at least ONE bit is 1

# ^

# XOR

# Result is 1 if bits are DIFFERENT

# ~

# NOT

# Flips all bits (0 becomes 1, 1 becomes 0)

# <<

# Left Shift

# Moves bits to the left, adds 0s on right

# >>

# Right Shift

# Moves bits to the right, removes rightmost bits





 

# How It Works
# Let's see bitwise operators in action:
 

# a = 5    # Binary: 0101

# b = 3    # Binary: 0011


# print(a & b)    # AND: 0101 & 0011 = 0001 = 1

# print(a | b)    # OR:  0101 | 0011 = 0111 = 7

# print(a ^ b)    # XOR: 0101 ^ 0011 = 0110 = 6

# print(~b)       # NOT: flips all bits of 3 = -4

# print(a << b)   # Left shift: 5 shifted left by 3 = 40

# print(a >> b)   # Right shift: 5 shifted right by 3 = 0
 

# Output:
 

# 1

# 7

# 6

# -4

# 40

# 0

 

# Visual Breakdown of AND (&):
 
#   5 = 0 1 0 1

#   3 = 0 0 1 1

#   -----------

# AND = 0 0 0 1  = 1

 
# (Both must be 1 to get 1)


 

# REAL-WORLD EXAMPLE: Permission Systems

# Video games use bitwise operators to manage player permissions efficiently!

# Imagine: Read=1, Write=2, Execute=4. A user with permission 7 (binary 111) has ALL permissions!

# To check if someone can write: if (permission & 2) - checks if the write bit is ON.

# This is why file permissions in computers look like: rwx (read-write-execute) = 7

# Minecraft uses similar systems for block states and entity flags!

 

# WHY THIS MATTERS:

# Bitwise operators are incredibly fast because they work at the computer's native level.

# They're used in game development for flags, states, and efficient data storage.

# Encryption and security systems rely heavily on bitwise operations.

# Understanding bits helps you understand how computers really think and process data!

 

# 4. Hands-On Activities
# Activity 1: Identity Operator
 

# Objective: Write a program to illustrate the use of 'is' identity operator

 

# Code:
 

# # Python program to illustrate the use

# # of 'is' identity operator


# x = 5

# if (type(x) is int):

#     print("true")

# else:

#     print("false")

 
# x = 5.5

# if (type(x) is not float):

#     print("true")

# else:

#     print("false")

 
# x = 20

# y = 20

# if (x is y):

#     print("x & y SAME identity")

 
# y = 30

# if (x is not y):

#     print("x & y have DIFFERENT identity")

# Sample Output:

# # Output

 
# true

# false

# x & y SAME identity

# x & y have DIFFERENT identity

 

# Activity 2: Bitwise Operator
 

# Objective: Write a program to apply the right shift and left shift bitwise operator

 

# Code:
 

# a = 10

# b = -10


# # print bitwise right shift operator

# print("a >> 1 =", a >> 1)

# print("b >> 1 =", b >> 1)

 
# a = 5

# b = -10

 
# # print bitwise left shift operator

# print("a << 1 =", a << 1)

# print("b << 1 =", b << 1)

# Sample Output:

# # Output

 
# a >> 1 = 5

# b >> 1 = -5

# a << 1 = 10

# b << 1 = -20

 

# Activity 3: Grading System
 

# Objective: Write a program to show students' grades by entering five subject marks and then calculating average marks and grades. If the average is between 91 to 100, A2 is between 81 to 90, and so on, do it till grade E2

 

# Code:
 

# print("Enter Marks Obtained in 5 Subjects:")

# markOne = int(input())
# markTwo = int(input())
# markThree = int(input())
# markFour = int(input())
# markFive = int(input())

# tot = markOne + markTwo + markThree + markFour + markFive
# avg = int(tot / 5)

# validRange = range(0, 101)

# if avg not in validRange:
#     print("Invalid Input!")

# elif avg in range(91, 101):
#     print("Your Grade is A1")

# elif avg in range(81, 91):
#     print("Your Grade is A2")

# elif avg in range(71, 81):
#     print("Your Grade is B1")

# elif avg in range(61, 71):
#     print("Your Grade is B2")

# elif avg in range(51, 61):
#     print("Your Grade is C1")

# elif avg in range(41, 51):
#     print("Your Grade is C2")

# elif avg in range(33, 41):
#     print("Your Grade is D")

# elif avg in range(21, 33):
#     print("Your Grade is E1")

# elif avg in range(0, 21):
#     print("Your Grade is E2")

# Sample Output:

# # Output

 
# Enter Marks Obtained in 5 Subjects: 

# 55

# 66

# 95

# 98

# 90

# Your Grade is B1

# Activity 1
# Title
# Identity operator
# Short description:
# Write a program to illustrate the use of 'is' identity operator
# Link
# Identity operator
# Solution
# Python Code:
 

# # Python program to illustrate the use

# # of 'is' identity operator


# x = 5

# if (type(x) is int):

#     print("true")

# else:

#     print("false")

 
# x = 5.5

# if (type(x) is not float):

#     print("true")

# else:

#     print("false")

 
# x = 20

# y = 20

# if (x is y):

#     print("x & y SAME identity")

 
# y = 30

# if (x is not y):

#     print("x & y have DIFFERENT identity")

# Sample Output:

# # Output

 
# true

# false

# x & y SAME identity

# x & y have DIFFERENT identity

# Activity 2
# Title
# Bitwise operator
# Short description:
# Write a program to apply the right shift and left shift bitwise operator.
# Link
# Bitwise operator
# Solution
# Python Code:

# a = 10

# b = -10


# # print bitwise right shift operator

# print("a >> 1 =", a >> 1)

# print("b >> 1 =", b >> 1)

 
# a = 5

# b = -10

 
# # print bitwise left shift operator

# print("a << 1 =", a << 1)

# print("b << 1 =", b << 1)

# Sample Output:

# # Output

 
# a >> 1 = 5

# b >> 1 = -5

# a << 1 = 10

# b << 1 = -20

# Activity 3
# Title
# Membership operator
# Short description:
# Write a program to show students’ grades by entering marks for five subjects, calculating the average, and checking the grade range using membership operators in and not in. For example, use in to check whether the average is in the range 91 to 100, 81 to 90, and so on, and use not in to validate marks outside the allowed range.
# Link
# Membership operator
# Solution
# Python Code:
 

# print("Enter Marks Obtained in 5 Subjects:")

# markOne = int(input())
# markTwo = int(input())
# markThree = int(input())
# markFour = int(input())
# markFive = int(input())

# tot = markOne + markTwo + markThree + markFour + markFive
# avg = int(tot / 5)

# validRange = range(0, 101)

# if avg not in validRange:
#     print("Invalid Input!")

# elif avg in range(91, 101):
#     print("Your Grade is A1")

# elif avg in range(81, 91):
#     print("Your Grade is A2")

# elif avg in range(71, 81):
#     print("Your Grade is B1")

# elif avg in range(61, 71):
#     print("Your Grade is B2")

# elif avg in range(51, 61):
#     print("Your Grade is C1")

# elif avg in range(41, 51):
#     print("Your Grade is C2")

# elif avg in range(33, 41):
#     print("Your Grade is D")

# elif avg in range(21, 33):
#     print("Your Grade is E1")

# elif avg in range(0, 21):
#     print("Your Grade is E2")

# Sample Output:

# # Output

 
# Enter Marks Obtained in 5 Subjects: 

# 55

# 66

# 95

# 98

# 90

# Your Grade is B1

# Outcome

# Learning Outcomes

# After completing this lesson, students will be able to:

# Understand and use identity operators ('is' and 'is not') to compare object identities
# Explain the difference between equality (==) and identity (is) in Python
# Use membership operators ('in' and 'not in') to search for values in sequences
# Understand how binary numbers work and what bits are
# Apply bitwise operators (AND, OR, XOR, NOT, shifts) to manipulate numbers at the bit level
# Write Python programs using all three types of operators confidently
# Agenda
# Teacher's Agenda 

# This section is for teacher reference only and should not be shared with students.

# Complete Code: Download Now

# Segment 1: Warm-up & Revision (8 minutes)
# Start with a quick revision of the previous lesson on operators
# Ask students: 'What operators have we learned so far?'
# Check if they completed any after-class projects
# Introduce today's topic: 'Three NEW types of operators!'
 

# Segment 2: Identity Operators (10 minutes)
# Use the Twin Houses analogy to explain identity vs equality
# Demonstrate with live coding: create two lists with same values
# Show that == returns True but 'is' returns False
# Complete Activity 1 together with students (5 minutes)
 

# Segment 3: Membership Operators (8 minutes)
# Use the Guest List analogy to explain 'in' and 'not in'
# Show examples with strings: 'Hello' in 'Hello World'
# Show examples with lists: checking if number is in a list
# Let students try their own examples
 

# Segment 4: Bitwise Operators (12 minutes)
# Start with the Light Switches analogy - make it visual!
# Explain binary briefly: how 5 becomes 0101
# Demonstrate AND, OR operations with visual bit comparison
# Show shift operators and their effect on numbers
# Complete Activity 2 together (10 minutes)
 

# Segment 5: Independent Practice & Wrap-up (7 minutes)
# Give overview of Activity 3 (Grading System) - let students try independently
# Walk around and help students who are stuck
# Buffer Activity: SI and Compound Interest program
# End with questions: 'Did you enjoy today's lesson?' 'Any doubts?'
 

# Common Issues and Solutions
 
# Issue

# Solution

# Confusion between 'is' and '=='

# Use the twin houses analogy - same appearance vs same building

# Struggling with binary numbers

# Use the light switch visualization - ON/OFF patterns

# Bitwise operators seem confusing

# Focus on AND and OR first, draw the bit comparisons

 

# Resources
# Activity : Click the Copy button to copy the activity code.
# Buffer Activity: View Now
# Assignment: ASCII value
# In this After Class Project, you will create an ASCII Value Checker that reveals the secret numeric code behind every character. Every letter, digit, and symbol on your keyboard has a unique number assigned to it in the ASCII system.

# Open project link
# →
# Goal
# Goal

# By the end of this activity, you will:

# Understand what ASCII values are and how they work
# Use ord() function to get ASCII values
# Apply type() and is operator to validate input
# Use conditional statements to categorize characters
 
# Success Criteria:

# Program accepts a single character from user
# Displays the ASCII value correctly
# Validates that input is exactly one character
# Correctly identifies character type (uppercase/lowercase/digit/special)
 

# Story
 


 

# Getting started
# Getting Started

# Project Structure
# Create a single Python file for this activity:
 

# ascii_checker/

# └── ascii_value.py  # Main program file

 

# Prerequisites
# Python installed
# Understanding of conditional statements (if-elif-else)
# Knowledge of type checking and identity operators
# Text editor (IDLE, VS Code, etc.)
 
# ASCII Table - Quick Reference
# Understanding ASCII value ranges:
 

# Character Type

# Range

# Example

# Digits (0-9)

# 48 - 57

# '5' = 53

# Uppercase (A-Z)

# 65 - 90

# 'A' = 65

# Lowercase (a-z)

# 97 - 122

# 'a' = 97

# Space

# 32

# ' ' = 32

# Special Characters

# Varies

# '@' = 64

# Instructions
# Instructions

# Step 1: Understanding ASCII and ord()
# Learn how to convert characters to ASCII values using the ord() function:
 

# # ord() function returns ASCII value

# print(ord('A'))     # Output: 65

# print(ord('a'))     # Output: 97

# print(ord('0'))     # Output: 48

# print(ord('@'))     # Output: 64


# # chr() function converts ASCII back to character

# print(chr(65))      # Output: A

# print(chr(97))      # Output: a
 

# Note:

# ord() = character to number | chr() = number to character. They are opposite functions!

 

# Step 2: Get Input and Validate
# Create the input section with validation:
 

# # Get input from user

# char = input("Enter a single character: ")


# # Validate: Check if exactly one character

# if type(char) is str and len(char) == 1:

#     print("Valid input!")

# else:

#     print("Please enter exactly ONE character!")
 

# How Validation Works:

# type(char) is str → Checks if input is a string
# len(char) == 1 → Checks if length is exactly 1
# Both must be True for valid input!

 

# Step 3: Display ASCII Value
# Get and display the ASCII value:
 

# # Get ASCII value

# ascii_val = ord(char)


# # Display the result

# print(f"Character: {char}")

# print(f"ASCII Value: {ascii_val}")
 

# Example:

# If user enters 'A':

# Character: A

# ASCII Value: 65

 

# Step 4: Identify Character Type
# Use conditional statements to categorize the character:
 

# # Identify character type using ASCII ranges

# if ascii_val >= 65 and ascii_val <= 90:

#     print("Type: Uppercase Letter")

# elif ascii_val >= 97 and ascii_val <= 122:

#     print("Type: Lowercase Letter")

# elif ascii_val >= 48 and ascii_val <= 57:

#     print("Type: Digit")

# elif ascii_val == 32:

#     print("Type: Space")

# else:

#     print("Type: Special Character")
 

# How It Works:

# Checking ASCII ranges:

# 65-90: 'A' to 'Z' (uppercase)
# 97-122: 'a' to 'z' (lowercase)
# 48-57: '0' to '9' (digits)
# 32: Space character
# Everything else: Special characters (@, #, !, etc.)
 

# Step 5: Complete Program
# Here's the complete optimized program:
 

# # ASCII Value Checker - Complete Program


# print("ASCII Value Checker")

# print("=" * 40)

 
# # Get input

# char = input("Enter a single character: ")

 
# # Validate input

# if type(char) is str and len(char) == 1:

#     # Get ASCII value

#     ascii_val = ord(char)

    

#     # Display results

#     print(f"\nCharacter: '{char}'")

#     print(f"ASCII Value: {ascii_val}")

    

#     # Identify type

#     print("\nCharacter Type: ", end="")

#     if ascii_val >= 65 and ascii_val <= 90:

#         print("Uppercase Letter")

#     elif ascii_val >= 97 and ascii_val <= 122:

#         print("Lowercase Letter")

#     elif ascii_val >= 48 and ascii_val <= 57:

#         print("Digit")

#     elif ascii_val == 32:

#         print("Space")

#     else:

#         print("Special Character")

# else:

#     print("\nError: Please enter exactly ONE character!")
 

# Step 6: Test Your Program
# Run and test with different characters:
 

# # Test Case 1: Uppercase letter

# # Input: A

# # Expected: ASCII = 65, Type = Uppercase Letter

 
# # Test Case 2: Lowercase letter

# # Input: z

# # Expected: ASCII = 122, Type = Lowercase Letter

 
# # Test Case 3: Digit

# # Input: 5

# # Expected: ASCII = 53, Type = Digit

 
# # Test Case 4: Special character

# # Input: @

# # Expected: ASCII = 64, Type = Special Character

 
# # Test Case 5: Invalid input

# # Input: ABC

# # Expected: Error message

# How to submit?
#    HOW TO SUBMIT YOUR AFTER CLASS PROJECT

# Once you have completed the After Class Project, Navigate to the VS Code Sidebar > Click on Source Control

 
# Click on Initialize Repository

 
# Write the Commit message describing your after class project & Click on commit

 
# Click on yes to Stage all changes

 
# Click on Publish

 
# Click on Publish to GitHub public repository & wait for the files to upload

 
# Click on Open on GitHub

 
# Click on code button

 
# Click on Copy to clipboard to copy the link

 
# Open your dashboard > Click on My projects


 
# Click on Submit now button

 
#  Scroll down > navigate your mouse to the right side of the screen
# right click on  enter the project url

 
# Click on the paste to paste the link

 
# Click on Submit project button to submit the project
 
 

 






 

 



 

# Paste this link on the student dashboard—Press Ctrl+V for Windows and Command + V in Mac.



# A window will pop up. Click on the copy button.

# HOW TO SUBMIT (LEGACY)

 

# How to submit?

 

 

# After completing, click on the Share button in the top right corner.

# Hints
# Hints

# Hint 1: Using ord() and chr()
 
# # ord() converts character to ASCII

# print(ord('A'))    # 65

# print(ord('B'))    # 66

# print(ord('a'))    # 97


# # chr() converts ASCII to character

# print(chr(65))     # A

# print(chr(97))     # a

 
# # They are opposites:

# char = 'X'

# ascii = ord(char)        # 88

# back = chr(ascii)        # X (same as original)
 

# Hint 2: Type Checking with 'is'
 
# # Check if variable is a string

# x = "hello"

# if type(x) is str:

#     print("x is a string")


# # Check if NOT a string

# y = 123

# if type(y) is not str:

#     print("y is NOT a string")

 
# # For our program:

# char = input("Enter: ")  # input() always returns string

# print(type(char))         # <class 'str'>
 

# Hint 3: Understanding ASCII Ranges
 
# # Uppercase: A=65 to Z=90

# print(ord('A'))    # 65 (start)

# print(ord('Z'))    # 90 (end)


# # Lowercase: a=97 to z=122

# print(ord('a'))    # 97 (start)

# print(ord('z'))    # 122 (end)

 
# # Digits: 0=48 to 9=57

# print(ord('0'))    # 48 (start)

# print(ord('9'))    # 57 (end)

 
# # Check if uppercase:

# if ord(char) >= 65 and ord(char) <= 90:

#     print("Uppercase!")
 

# Hint 4: Conditional Logic Pattern
 
# # Pattern for checking ranges:

# value = 75


# if value >= 90:

#     print("A grade")

# elif value >= 80:      # 80-89

#     print("B grade")

# elif value >= 70:      # 70-79

#     print("C grade")

# else:                  # Below 70

#     print("D grade")

 
# # Same pattern for ASCII:

# if ascii >= 65 and ascii <= 90:

#     print("Uppercase")

# elif ascii >= 97 and ascii <= 122:

#     print("Lowercase")
 

# Hint 5: Input Validation
 
# # Check multiple conditions:

# char = input("Enter: ")


# # Method 1: Using 'and'

# if type(char) is str and len(char) == 1:

#     print("Valid")

 
# # Breakdown:

# # type(char) is str  → Is it a string? (Always True for input())

# # len(char) == 1     → Is length exactly 1?

 
# # Examples:

# # Input: "A"   → len=1 → Valid

# # Input: "AB"  → len=2 → Invalid

# # Input: ""    → len=0 → Invalid
 

# Key Takeaways:

# Every character has a unique ASCII number
# ord() converts character to ASCII value
# chr() converts ASCII value back to character
# Use 'is' operator to check types
# Conditional statements categorize data into ranges
# How was this lesson?
# Your feedback helps us make lessons better.

# Share your feedback
