# Data types in python
# In this lesson, you will explore core Python concepts including fundamental data types, typecasting, and capturing user input. You will also learn to manipulate text using string indexing, slicing, and concatenation, culminating in a hands-on activity to build a custom Secret Agent Name Badge.

# Overview
# Activities
# Outcome
# Agenda
# Overview
# List of Topics

# 1. Data Types

# 2. Typecasting

# 3. Taking User Input

# 4. String Indexing and Slicing

# 5. String Concatenation

# 6. Activity Explanation

# ------------------------------------------------------------

# 1. Data Types

 

# WHAT IT IS

# A data type tells Python what kind of value is stored inside a variable. Every value used in a program belongs to some type, like a whole number, a decimal, some text, or a true-false answer. Knowing the data type helps Python understand what actions can be performed on that value.



# HOW IT WORKS

# Python has four data types used most often - integer for whole numbers, float for decimal numbers, string for text, and boolean for True or False answers. The type() command checks and displays which data type a stored value belongs to, right inside the program.

# a = 5

# print(type(a))
# b = 2.5
# print(type(b))
# c = "coding"
# print(type(c))
# d = True
# print(type(d))
 

# Think of it this way

# A fruit basket holds many different kinds of fruit together - apples, bananas, and grapes all sitting side by side in one basket. Data types work in exactly the same way. Numbers, text, and true-false answers are simply different kinds of values, just like different kinds of fruit.

 

# Remember

# Always use type() whenever unsure what kind of value is stored inside a variable, since every value in Python belongs to one specific data type.

 

# ------------------------------------------------------------

# 2. Typecasting

 

# WHAT IT IS

# Typecasting means changing a value from one data type into a completely different data type. A number can be turned into text, or text can sometimes be turned into a number, depending entirely on what the program needs to do with that particular value next.



# HOW IT WORKS

# Python provides ready-made commands - str(), int(), and float() - that convert a value's data type into a new one. Once converted, the value keeps its original meaning completely, but it now behaves differently inside the program, following the rules of its brand new data type.

# f = 10.18
# i = int(f
# print(i)
 

# Think of it this way

# A toy car can be repainted from bright red into cool blue, yet it still remains the exact same toy car underneath its new paint. Typecasting works the same way. It repaints a value into a new type, without ever changing what that value actually means.

 

# Remember

# str(), int(), and float() are the three most common commands used to change a value from one data type into a completely different one.

 

# ------------------------------------------------------------

# 3. Taking User Input

 

# WHAT IT IS

# User input means Python pauses the program to ask a question, then waits patiently for a person to type an answer on the keyboard. This lets programs collect real information directly from people, instead of using only fixed values that are already written inside the code.



# HOW IT WORKS

# The input() command displays a message on the screen and waits until an answer gets typed and confirmed. Whatever gets typed by the person is always stored as a string, which means even numbers typed in must be converted before being used in any calculations.

# name = input("Enter your name: ")
# print("Hello", name)
 

# Think of it this way

# A bike shop always asks a customer which color bike they would like before building it, and then waits for their answer before starting any work. Python asks a question using input() and waits for an answer to be typed, in that very same way.

 

# Remember

# input() always stores whatever gets typed as a string, even if the person types numbers, so it may need typecasting before being used.

 

# ------------------------------------------------------------

# 4. String Indexing and Slicing

 

# WHAT IT IS

# A string is simply a row of characters lined up one after another, and every single character sits at its own position, called an index. Indexing means picking out just one character, while slicing means picking out a whole group of characters together at once.



# HOW IT WORKS

# Indexing in Python always starts counting from 0, never from 1, which can feel surprising at first. Square brackets are used to pick one character or a whole range of characters together, and a negative index counts backward starting from the very last character.

# word = "mango"
# print(word[0]
# print(word[1:4])
# print(word[-1])
 

# Think of it this way

# A fruit tray lines up different fruits in a neat row, and the very first fruit always sits at position 0, with the next fruit sitting at position 1, and so on. Indexing points to one single letter of a string in that exact same way.

 

# Remember

# Indexing always starts counting from 0, and slicing picks out a whole range of characters using a start position and an end position.

 

# ------------------------------------------------------------

# 5. String Concatenation

 

# WHAT IT IS

# Concatenation means joining two or more separate strings together so they become one single, longer string. This is useful whenever a program needs to combine pieces of text, like joining someone's name together with a greeting message to build one complete sentence for display.



# HOW IT WORKS

# The plus sign is used to join strings together, one right after another, in the exact order they are written in the code. Numbers must always be changed into strings first using typecasting, before they can be joined together with any other piece of text.

# fruit1 = "apple"
# fruit2 = "banana"
# print(fruit1 + " and " + fruit2)
 

# Think of it this way

# A bike frame and a bike wheel get joined together carefully, piece by piece, to build one single, complete, working bike. Concatenation works in that exact same way. It joins two separate strings together carefully to build one single, complete string for the program.

 

# Remember

# Use the plus sign to join strings together, but always change any numbers into strings first before joining them together with text.

 

# ------------------------------------------------------------

# 6. Activity - Secret Agent Name Badge

# WHAT YOU WILL BUILD


# A Secret Agent Name Badge that displays a made-up agent ID card on screen, built using your own real name and their favorite gadget. The badge combines a code name, an agent number, a speed rating, and an active status into one final message.

# SKILLS PRACTISED

# This single activity practises every topic covered in this lesson together - checking data types, converting values using typecasting, taking user input, slicing parts of a string to build a code name, and joining several strings together to print the final complete badge.

# HOW IT WORKS

# Step 1: Type in a real name and a favorite gadget when asked.

# Step 2: Store the agent's number, speed rating, mission count, height, and active status.

# Step 3: Print each stored value along with its data type.

# Step 4: Typecast the numbers and the true/false value into text.

# Step 5: Slice the name to build a secret code name.

# Step 6: Join everything together and print the final secret agent badge.

# Remember

# The final badge combines every topic learned in this lesson - data types, typecasting, input, slicing, and joining strings.

# Activity 1
# Title
# Secret Agent Name Badge
# Short description:
# A Secret Agent Name Badge that displays a made-up agent ID card on screen, built using your own real name and their favorite gadget. The badge combines a code name, an agent number, a speed rating, and an active status into one final message.
# Link
# Secret Agent Name Badge
# Solution
# # PART 1: Ask the agent for their details
# name = input("Enter your real name, Agent: ")
# gadget = input("Enter your favorite gadget: ")

# # PART 2: Store the agent's details using different data types
# agent_number = 7
# speed_rating = 9.5
# mission_count = 12
# height_m = 1.65
# is_active = True

# # PART 3: Print each detail along with its data type
# print("Name:", name, "-> type:", type(name))
# print("Gadget:", gadget, "-> type:", type(gadget))
# print("Agent Number:", agent_number, "-> type:", type(agent_number))
# print("Speed Rating:", speed_rating, "-> type:", type(speed_rating))
# print("Mission Count:", mission_count, "-> type:", type(mission_count))
# print("Height (m):", height_m, "-> type:", type(height_m))
# print("Is Active:", is_active, "-> type:", type(is_active))

# # PART 4: Typecast the numbers and true/false value into text
# agent_number_text = str(agent_number)
# mission_count_text = str(mission_count)
# speed_rating_text = str(speed_rating)
# status_text = str(is_active)

# print("Agent Number as text:", agent_number_text, "-> type:", type(agent_number_text))
# print("Mission Count as text:", mission_count_text, "-> type:", type(mission_count_text))
# print("Speed Rating as text:", speed_rating_text, "-> type:", type(speed_rating_text))
# print("Status as text:", status_text, "-> type:", type(status_text))

# # PART 5: Slice the name to create a secret code name
# first_three = name[0:3]
# last_letter = name[-1:]
# code_name = first_three + last_letter
# print("First 3 letters of name:", first_three)
# print("Last letter of name:", last_letter)
# print("Secret Code Name:", code_name)

# # PART 6: Reverse the gadget name using slicing
# reversed_gadget = gadget[::-1]
# print("Reversed Gadget Name:", reversed_gadget)

# # PART 7: Join everything together to build the final badge message
# badge_line_1 = "AGENT " + code_name.upper()
# badge_line_2 = "ID: " + agent_number_text + " | MISSIONS: " + mission_count_text
# badge_line_3 = "SPEED: " + speed_rating_text + " | ACTIVE: " + status_text
# badge_line_4 = "SECRET GADGET CODE: " + reversed_gadget.upper()

# # PART 8: Print the complete secret agent badge
# print("")
# print("===== SECRET AGENT BADGE =====")
# print(badge_line_1)
# print(badge_line_2)
# print(badge_line_3)
# print(badge_line_4)
# print("===============================")
 

# Activity screenshots


# Outcome

# Learning Outcomes of Data Types in Python:

# Checked the data type of numbers, text, and true/false values.
# Converted values from one data type into another using typecasting.
# Took input from a user and stored it as a string.
# Sliced parts of a string using index positions.
# Joined multiple strings together using concatenation.
 

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
# Data Types in Python
# · Warm-Up · Topics · Activity · Wrap-Up · ACP
# Teacher Only
# 0:00 – 2:00
# 2 mins · Scripted
# Warm-Up
# Prior knowledge · Hook · Set the scene
# 2:00 – 14:00
# 12 mins · Topics
# Topics
# Data Types Typecasting User Input String Indexing & Slicing String Concatenation
# 14:00 – 15:00
# 1 min · Scripted
# Screen Share & Activity Framing
# Share boilerplate · Confirm setup · Show what we're building
# 15:00 – 33:00
# 18 mins · Activity
# Activity: Secret Agent Name Badge
# Data types · Typecasting · input() · Indexing & Slicing · Concatenation · 6 steps Python
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
# Assignment: School Club Member Badge
# In this assignment, you will build a School Club Member Badge using Python. You will collect a member name and club name, store details using different data types, convert values into text, slice strings to create a badge code, and join text to print a complete badge.

# Open project link
# →
# Goal
# Goal

# By the end of this activity, you will be able to:

# Identify common data types such as string, integer, float, and Boolean.
# Use typecasting to convert numbers and Boolean values into strings.
# Use input() to collect information from the user.
# Use string indexing and slicing to create short text codes.
# Use string concatenation to build a final badge message.
# Getting started
# Getting Started

# Prerequisites

# Basic understanding of Python variables and print().
# Basic understanding of text values and numbers.
# A Python editor or notebook where you can run Python code.
# Comfort with entering input values while a program is running.
# Project Overview

# You will create a badge generator for a school club member. The program will ask for the member name and club name, display different data types, convert values into text, use string slicing to create a badge code, reverse the club name, and print a final school club member badge.

 

# Instructions
# Instructions

# Step 1: Ask for Member Details Use input() to ask for the club member name and school club name. Store both answers in variables.

# Step 2: Store Details Using Different Data Types Create variables for member number, points earned, event count, meeting hours, and active status. These values should use integer, float, and Boolean data types.

# Step 3: Print Values and Their Data Types Use type() to show the data type of each value. This helps you see how Python stores different kinds of information.

# Step 4: Typecast Values into Text Use str() to convert the member number, event count, points, and active status into strings so they can be joined with other text.

# Step 5: Use String Indexing and Slicing Use name[0:3] to get the first three letters of the name and name[-1:] to get the last letter. Join them to create a badge code.

# Step 6: Reverse the Club Name Use club[::-1] to reverse the club name and create a secret club code.

# Step 7: Concatenate the Badge Lines Use the + operator to join text values and build each line of the final badge.

# Step 8: Run and Explore Run the program with different names and club names. Check how the badge code and secret club code change each time.

# Success Criteria

# The program asks for the member name and school club name.
# The program stores and prints values with different data types.
# The program uses str() to convert values into text.
# The program uses string slicing to create a badge code and reverse the club name.
# The program joins text values to print a complete school club member badge.
 

# Complete Code

# Below is the full Python code for the activity:

# # PART 1: Ask the club member for their details
# name = input("Enter your real name, Club Member: ")
# club = input("Enter your school club name: ")
 
# # PART 2: Store the member's details using different data types
# member_number = 8
# points_earned = 9.5
# event_count = 6
# meeting_hours = 1.5
# is_active = True
 
# # PART 3: Print each detail along with its data type
# print("Name:", name, "-> type:", type(name))
# print("Club:", club, "-> type:", type(club))
# print("Member Number:", member_number, "-> type:", type(member_number))
# print("Points Earned:", points_earned, "-> type:", type(points_earned))
# print("Event Count:", event_count, "-> type:", type(event_count))
# print("Meeting Hours:", meeting_hours, "-> type:", type(meeting_hours))
# print("Is Active:", is_active, "-> type:", type(is_active))
 
# # PART 4: Typecast the numbers and true/false value into text
# member_number_text = str(member_number)
# event_count_text = str(event_count)
# points_text = str(points_earned)
# status_text = str(is_active)
 
# print("Member Number as text:", member_number_text, "-> type:", type(member_number_text))
# print("Event Count as text:", event_count_text, "-> type:", type(event_count_text))
# print("Points as text:", points_text, "-> type:", type(points_text))
# print("Status as text:", status_text, "-> type:", type(status_text))
 
# # PART 5: Slice the name to create a badge code
# first_three = name[0:3]
# last_letter = name[-1:]
# badge_code = first_three + last_letter
 
# print("First 3 letters of name:", first_three)
# print("Last letter of name:", last_letter)
# print("Badge Code:", badge_code)
 
# # PART 6: Reverse the club name using slicing
# reversed_club = club[::-1]
# print("Reversed Club Name:", reversed_club)
 
# # PART 7: Join everything together to build the final badge message
# badge_line_1 = "CLUB MEMBER " + badge_code.upper()
# badge_line_2 = "ID: " + member_number_text + " | EVENTS: " + event_count_text
# badge_line_3 = "POINTS: " + points_text + " | ACTIVE: " + status_text
# badge_line_4 = "SECRET CLUB CODE: " + reversed_club.upper()
 
# # PART 8: Print the complete school club badge
# print("")
# print("===== SCHOOL CLUB MEMBER BADGE =====")
# print(badge_line_1)
# print(badge_line_2)
# print(badge_line_3)
# print(badge_line_4)
# print("====================================")
 

 

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

# Hint 1: Data Types: Use type(value) to check whether a value is a string, integer, float, or Boolean.

# Hint 2: Typecasting: Use str(value) when you need to join a number or Boolean with text.

# Hint 3: User Input: input() always gives a text value, even when the user types a number.

# Hint 4: String Slicing: Use name[0:3] for the first three characters and name[-1:] for the last character.

# Hint 5: Concatenation: Use + to join strings together. Convert non-string values before joining them.

 

# How was this lesson?
# Your feedback helps us make lessons better.

# Share your feedback
