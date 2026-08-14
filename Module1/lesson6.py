# Python Operator II
# In this lesson, you learn how to make programs that take decisions. You explore the if-elif-else statement to handle multiple outcomes, and the logical operators AND, OR, and NOT to combine conditions. You build the Smart School Day Planner — a program that reads three simple inputs and uses all five topics to print a personalised plan for the day.

# Overview
# Activities
# Outcome
# Agenda
# Overview
# List of Topics

# 1.  if-elif-else Statements

# 2.  AND Operator

# 3.  OR Operator

# 4.  NOT Operator

# 5.  Combining Logical Operators

# 6.  Activity Explanation

 

# 1. if-elif-else Statements

# WHAT IT IS

# An if-elif-else statement lets Python choose between more than two outcomes. Python checks each condition from top to bottom. It runs only the first block that is True. If none match, the else block runs as a fallback. Think of a teacher marking a test: above 90 is Grade A, above 75 is Grade B, above 60 is Grade C, otherwise Fail. Python checks from the top and stops at the first match - just like the teacher stops at the first correct grade band.


 

# HOW IT WORKS

# Write if and the first condition, then a colon. Indent the code that runs when that condition is True. Write elif and the next condition, then a colon. Add as many elif blocks as needed - there is no strict limit. Write else with a colon at the end. The else block runs when every condition above it is False. You cannot write elif without a starting if.

# # Smart School Day Planner - Topic 1
# if day in ("Saturday", "Sunday"):
#     print("Day type : Weekend - enjoy your free time!")
# elif day == "Monday":
#     print("Day type : First day of the week.")
# elif day == "Friday":
#     print("Day type : Last school day.")
# elif day in ("Tuesday", "Wednesday", "Thursday"):
#     print("Day type : Regular school day.")
# else:
#     print("Day type : Day not recognised.")
# Think of it this way

# Think of a traffic light. It checks green first. If not green, it checks amber. If not amber, it shows red. Python's if-elif-else works the same way - top to bottom, stops at the first condition that is True.

# Remember

# elif cannot be used without a starting if. Always end the chain with else so there is always a default outcome.

 

# 2. AND Operator

# WHAT IT IS

# The and operator joins two conditions together. Both conditions must be True for the whole expression to be True. If even one condition is False, the result is False. Use and when all rules must be met at the same time. Imagine a school computer lab: students need an ID card AND a permission slip to enter. Forgetting either one means no entry. The and operator works exactly the same way.


 

# HOW IT WORKS

# Write the first condition, then the word and, then the second condition. Python checks the left condition first. If it is False, Python stops immediately and returns False. It does not check the right condition at all. Only when both conditions are True does and return True.

# # Topic 2 - AND operator
# if weather == "sunny" and homework == "yes":
#     print("After school: Head to the park!")
# Think of it this way

# Think of a phone lock screen. It needs the correct PIN AND face recognition. Failing either one keeps the phone locked. The and operator works the same - every condition must pass.

# Remember

# If the first condition is False, Python stops checking immediately. Every single condition must be True for and to return True.

 

# 3. OR Operator

# WHAT IT IS

# The or operator joins two conditions together. At least one condition must be True for the result to be True. The result is only False when every condition is False. Use or when any one of several options is acceptable. Think of a school canteen: it accepts payment by cash OR by school card. Students are only turned away if they have neither.


 

# HOW IT WORKS

# Write the first condition, then the word or, then the second condition. Python checks the left condition first. If it is True, Python stops immediately and returns True. It does not check the rest. Only when both conditions are False does or return False.

# # Topic 3 - OR operator
# if weather == "rainy" or weather == "cloudy":
#     print("Weather tip : Pack your umbrella!")
# Think of it this way

# Think of a school gate. It opens if a student scans their card OR if a teacher presses the button. Only one is needed. The or operator works the same - any one True condition is enough.

# Remember

# or returns True if at least one condition is True. It only returns False when every condition is False.

 

# 4. NOT Operator

# WHAT IT IS

# The not operator flips a Boolean value. It turns True into False and False into True. Use not when it is easier to describe the opposite of a condition. Python also has a not-equal symbol != that returns True when two values are different. Think of a Do Not Disturb sign on a classroom door. It means the opposite of the normal open state. The not operator does exactly the same - it flips whatever comes after it.


 

# HOW IT WORKS

# Place not directly before a condition or a Boolean value. Python instantly flips it: not True becomes False, not False becomes True. The != symbol compares two values. If they are different it returns True. If they are the same it returns False. Use not to check for the absence of something - like homework not being done.

# # Topic 4 - NOT operator
# if not (homework == "yes"):
#     print("Homework : Not done yet. Finish it before going out!")
# # not-equal operator
# if day != "Saturday":
#     print("It is a school week day.")
# Think of it this way

# Think of a Do Not Disturb sign on a classroom door. It means the room is the opposite of available. The not operator does the same - whatever was True becomes False and vice versa.

# Remember

# not reverses True to False and False to True. != returns True only when two values are different from each other.

 

# 5. Combining Logical Operators

# WHAT IT IS

# You can use and, or, and not together inside one condition. Python checks them in a fixed order: not first, then and, then or. Brackets can be added to control the order and keep the logic clear. Real programs need complex conditions. The Smart School Day Planner combines all three operators to give a personalised Best Plan message. Think of a hospital checking age AND temperature AND symptoms together to decide priority. Combining operators lets Python make the same kind of layered decision.


 

# HOW IT WORKS

# Write conditions using and, or, and not as needed. Python evaluates them in priority order: not first, then and, then or. Use brackets when mixing operators to make the logic easy to read. In the planner, the Best Plan section checks weather AND homework AND day all together. Each elif handles a different combination so the program always prints the most useful advice.

# # Topic 5 - Combining AND + OR + NOT
# if weather == "rainy" and not (homework == "yes"):
#     print("Best plan : Stay in, finish homework first.")
# elif weather == "sunny" and homework == "yes" and not (day in ("Saturday", "Sunday")):
#     print("Best plan : All set for a great school day!")
# elif day in ("Saturday", "Sunday") and weather == "sunny":
#     print("Best plan : Perfect weekend - head outside!")
# else:
#     print("Best plan : Take it one step at a time!")
# Think of it this way

# Think of a hospital triage system. It checks age AND temperature AND symptoms together. Combining and, or, and not lets Python make the same kind of careful, multi-condition decision.

# Remember

# Python checks not first, then and, then or. Add brackets when mixing operators to keep the logic clear and avoid mistakes.

 

# 6. Activity — Smart School Day Planner

# You will build a Python program that takes three inputs — day, weather, and homework status — and uses if-elif-else, AND, OR, NOT, and combined conditions to print a personalised plan for the day.

# WHAT YOU WILL BUILD


# A Python program that asks the user three questions. It classifies the day using if-elif-else. It uses AND to check sunny weather and homework done together. It uses OR to check rainy or cloudy weather. It uses NOT to catch homework not done. It combines all three operators to print the best plan for the day.

# SKILLS PRACTISED

# if-elif-else chaining, AND operator, OR operator, NOT operator, combining logical operators, string comparison, and user input with input().

# STEPS

# Step 1:  Print the welcome message: "=== Smart School Day Planner ===".

# Step 2:  Use input() to ask for the day, weather, and homework status. Store each in a variable.

# Step 3:  Print the plan header using the day variable in an f-string.

# Step 4:  Write if-elif-else to classify the day type (weekend / Monday / Friday / other school day).

# Step 5:  Write an if statement using AND to check sunny weather and homework done together.

# Step 6:  Write an if statement using OR to check rainy or cloudy weather.

# Step 7:  Write an if statement using NOT to catch when homework is not done.

# Step 8:  Write if-elif-else using AND, OR, and NOT combined to print the best plan message.

# Step 9:  Print the closing message: "Plan complete! Have a wonderful day!"

# Step 10:  Run the program with three different combinations of inputs to test all branches.

 

# Activity 1
# Title
# Smart School Day Planner
# Short description:
# A Python program that asks the user three questions. It classifies the day using if-elif-else. It uses AND to check sunny weather and homework done together. It uses OR to check rainy or cloudy weather. It uses NOT to catch homework not done. It combines all three operators to print the best plan for the day.
# Link
# Smart School Day Planner
# Solution
# Python Code: 

# # Smart School Day Planner

# print("=== Smart School Day Planner ===")
# print("Answer 3 quick questions and I will plan your day!\n")

# day      = input("What day is it? (Monday to Sunday): ").strip().capitalize()
# weather  = input("What is the weather? (sunny / rainy / cloudy): ").strip().lower()
# homework = input("Is your homework done? (yes / no): ").strip().lower()

# print()
# print(f"=== Your Plan for {day} ===")
# print("-" * 35)

# # Topic 1 -- if-elif-else: classify the day
# if day in ("Saturday", "Sunday"):
#     print("Day type    : Weekend - enjoy your free time!")
# elif day == "Monday":
#     print("Day type    : First day of the week. Pack your weekly planner.")
# elif day == "Friday":
#     print("Day type    : Last school day. Return library books today.")
# elif day in ("Tuesday", "Wednesday", "Thursday"):
#     print("Day type    : Regular school day. Stay focused!")
# else:
#     print("Day type    : Day not recognised. Please check the spelling.")

# # Topic 2 -- AND operator: sunny AND homework done
# if weather == "sunny" and homework == "yes":
#     print("After school: Head to the park - great weather and homework is done!")

# # Topic 3 -- OR operator: rainy OR cloudy
# if weather == "rainy" or weather == "cloudy":
#     print("Weather tip : Pack your umbrella - it may get wet outside.")

# # Topic 4 -- NOT operator: homework NOT done
# if not (homework == "yes"):
#     print("Homework    : Not done yet. Finish it before going out!")

# # Topic 5 -- Combining AND + OR + NOT together
# if weather == "rainy" and not (homework == "yes"):
#     print("Best plan   : Stay in, finish homework, then watch your favourite show.")
# elif weather == "sunny" and homework == "yes" and not (day in ("Saturday", "Sunday")):
#     print("Best plan   : All set for a great school day - you are prepared!")
# elif day in ("Saturday", "Sunday") and weather == "sunny":
#     print("Best plan   : Perfect weekend weather - head outside and have fun!")
# else:
#     print("Best plan   : Take it one step at a time - you have got this!")

# print()
# print("Plan complete! Have a wonderful day!")
 

# Activity screenshots


# Outcome

# Learning Outcomes of Python Operators II:

# Used if-elif-else to handle multiple conditions in one chain.
# Applied the AND operator to check two conditions at the same time.
# Used the OR operator to accept any one of several valid inputs.
# Applied NOT and != to check for the absence of a condition.

 

# Agenda
# ⛔ Teacher eyes only. Do not share this screen.

# Important Links / Resources
# 📦 Complete Code	Download Now ↗
# 🗂️ Boilerplate Code	Download Now ↗
# Legend
# ✅ DO
# 🙋 ASK
# 💡 SILENCE
# 🌐 ONLINE TIP
# ⚠️ WATCH
# 👥 GROUP
# Coral = Scripted
# Blue = Topics
# Amber = Activity
# 45 min
# 1:1 Class
# Python Operator II
#  Warm-Up · Topics · Activity · Wrap-Up · ACP
# Teacher Only
# 0:00 – 2:00
# 2 mins · Scripted
# Warm-Up
# Prior knowledge · Hook · Set the scene
# 2:00 – 14:00
# 12 mins · Topics
# Topics
# if-elif-else AND Operator OR Operator NOT Operator Combining Logical Operators
# 14:00 – 15:00
# 1 min · Scripted
# Screen Share & Activity Framing
# Share boilerplate · Confirm setup · Show what we're building
# 15:00 – 33:00
# 18 mins · Activity
# Activity: Smart School Day Planner
# if-elif-else · AND · OR · NOT · Combined Operators · 10 steps Python
# 33:00 – 40:00
# 7 mins · Scripted
# Wrap-Up
# Rapid recall · Key rules · Real-world connection · Celebrate
# 40:00 – 43:00
# 3 mins · Scripted
# ACP & Quiz Explanation
# After-class project · Quiz reminder · Submission deadline
# 43:00 – 45:00
# 2 mins · Scripted
# Closing
# Doubts · Celebration · Sign off
# Assignment: Library Visit Planner
# In this assignment, you will build a Library Visit Planner using Python. You will use if-elif-else statements and logical operators to suggest a plan based on the day, weather, and whether a book needs to be returned.

# Open project link
# →
# Goal
# Goal

# By the end of this activity, you will be able to:

# Use if-elif-else statements to give different outputs for different days.
# Use the AND operator to check when two conditions are true at the same time.
# Use the OR operator to check when at least one condition is true.
# Use the NOT operator to check when a condition is not true.
# Combine logical operators to create a final library visit plan.
# Getting started
# Getting Started

# Prerequisites
# Basic understanding of Python variables, input(), and print().
# Basic understanding of if statements and indentation.
# A Python editor or notebook where you can run Python code.
# Comfort with entering input values while a program is running.
# Project Overview
# You will create a planner that asks three questions: the day of the week, the weather, and whether a book is due for return. The program will classify the day, give weather and book-return tips, and suggest the best library plan using combined logical conditions.

 

# Instructions
# Instructions

# Step 1: Set Up the Program Create a new Python file. Add the title messages using print() so the user knows they are using the Library Visit Planner.

# Step 2: Collect User Inputs Use input() to ask for the day, weather, and whether a book needs to be returned. Use strip(), capitalize(), and lower() to clean the answers.

# Step 3: Classify the Day with if-elif-else Use if, elif, and else to check whether the day is a weekend, Monday, Friday, a regular school day, or an unrecognised day.

# Step 4: Use the AND Operator Use weather == "sunny" and book_due == "yes" to give a tip when both conditions are true.

# Step 5: Use the OR Operator Use weather == "rainy" or weather == "cloudy" to give an umbrella reminder when either weather condition is true.

# Step 6: Use the NOT Operator Use not (book_due == "yes") to show a message when there is no book that needs to be returned.

# Step 7: Combine Logical Operators Use AND, OR-style choices, and NOT together in the final decision block to suggest the best library visit plan.

# Step 8: Run and Explore Run the program with different days, weather conditions, and book-return answers. Notice how the output changes for each combination.

# Success Criteria
# The program asks for the day, weather, and book return status.
# The program uses if-elif-else statements to classify the day.
# The program uses the AND operator to check two true conditions together.
# The program uses the OR operator to handle rainy or cloudy weather.
# The program uses the NOT operator to check when no book is due.
# The program combines logical operators to print a final best plan.
# Complete Code
# Below is the full Python code for the activity

# # Library Visit Planner

# print("=== Library Visit Planner ===")
# print("Answer 3 quick questions and I will plan your library visit!\n")

# day       = input("What day is it? (Monday to Sunday): ").strip().capitalize()
# weather   = input("What is the weather? (sunny / rainy / cloudy): ").strip().lower()
# book_due  = input("Do you have a book to return? (yes / no): ").strip().lower()

# print()
# print(f"=== Your Library Plan for {day} ===")
# print("-" * 35)

# # Topic 1 -- if-elif-else: classify the day
# if day in ("Saturday", "Sunday"):
#     print("Day type    : Weekend - a good time for a relaxed library visit!")
# elif day == "Monday":
#     print("Day type    : Start of the week. Check your reading list.")
# elif day == "Friday":
#     print("Day type    : Last school day. Return books before the weekend.")
# elif day in ("Tuesday", "Wednesday", "Thursday"):
#     print("Day type    : Regular school day. Plan a short library visit.")
# else:
#     print("Day type    : Day not recognised. Please check the spelling.")

# # Topic 2 -- AND operator: sunny AND book due
# if weather == "sunny" and book_due == "yes":
#     print("Library tip : Great weather! Return your book and borrow a new one.")

# # Topic 3 -- OR operator: rainy OR cloudy
# if weather == "rainy" or weather == "cloudy":
#     print("Weather tip : Carry an umbrella if you are going to the library.")

# # Topic 4 -- NOT operator: book NOT due
# if not (book_due == "yes"):
#     print("Book status : No book return needed today. You can browse new books.")

# # Topic 5 -- Combining AND + OR + NOT together
# if weather == "rainy" and book_due == "yes":
#     print("Best plan   : Visit the library carefully and return your book on time.")
# elif weather == "sunny" and book_due == "yes" and not (day in ("Saturday", "Sunday")):
#     print("Best plan   : Stop by the library after school and return your book.")
# elif day in ("Saturday", "Sunday") and weather == "sunny":
#     print("Best plan   : Perfect day for a longer reading session at the library!")
# else:
#     print("Best plan   : Check your schedule and plan a simple library visit.")

# print()
# print("Library plan complete! Happy reading!")
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
 
# HOW TO SUBMIT (LEGACY)

 

# How to submit?

 

 

# After completing, click on the Share button in the top right corner.


# A window will pop up. Click on the copy button.


 

# Paste this link on the student dashboard—Press Ctrl+V for Windows and Command + V in Mac.
 






 

 

# Hints
# Hints

# Hint 1: if-elif-else: Use if for the first condition, elif for extra conditions, and else for the final fallback.

# Hint 2: AND: Use and when both conditions must be true for the message to run.

# Hint 3: OR: Use or when at least one of the conditions can be true.

# Hint 4: NOT: Use not to reverse a condition, such as checking when book_due is not yes.

# Hint 5: Combining Conditions: Use parentheses to make combined logical conditions easier to read.

 

# How was this lesson?
# Your feedback helps us make lessons better.

# Share your feedback
