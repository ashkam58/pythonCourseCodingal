# Conditional Statements
# In this lesson, you explore conditional statements in Python. You use indentation to group code into blocks, write an if statement that runs only when a condition is true, and write an if-else statement that chooses between two blocks, while building an interactive weather outfit picker.

# Overview
# Activities
# Outcome
# Agenda
# Overview
# List of Topics

# 1. What Is Indentation?

# 2. What Is a Conditional Statement?

# 3. The if Statement

# 4. The if-else Statement

# 5. Activity Explanation

# ------------------------------------------------------------

# 1. What Is Indentation?

 

# WHAT IT IS

# Indentation means adding blank spaces at the beginning of a line to show that it belongs inside a block of code. Python uses indentation instead of curly braces to group related lines together, so every single line inside the same block must line up exactly the same way.



# HOW IT WORKS

# You press the space bar or tab key at the start of a line to push it inward, showing it belongs to the block above it. Every line inside that same block must be indented by exactly the same amount, or Python raises an error immediately.

# if 5 > 0:
#     print("5 is positive")
# print("This line is outside the block")
 

# Think of it this way

# A recipe card lists ingredients slightly indented under the step they belong to, so you know exactly which ingredients go with which cooking step. Indentation groups lines of code together in that same lined-up, organized way, so Python always knows exactly what belongs where on the page.

 

# Remember

# Every line inside the same block must be indented by exactly the same amount.

 

# ------------------------------------------------------------

# 2. What Is a Conditional Statement?

 

# WHAT IT IS

# A conditional statement is a decision Python makes by first checking whether something is true or false, like a number being bigger than another number. Python then chooses exactly which block of code to run next, based entirely on that one true or false answer.



# HOW IT WORKS

# Python tests a condition, like whether a number is bigger than zero, and gets back either the value True or the value False as the answer. Depending entirely on that one answer, Python then decides whether to run the block of code written directly underneath it.

# temperature = 15
# print(temperature < 20)
 

# Think of it this way

# Deciding whether to bring an umbrella outside today depends entirely on checking one simple thing first, whether it is actually raining right now outside. A conditional statement checks exactly one true or false question in that same simple way, before deciding calmly what should happen next.

 

# Remember

# A conditional statement checks whether something is true or false before deciding what to do next.

 

# ------------------------------------------------------------

# 3. The if Statement

 

# WHAT IT IS

# The if statement runs a block of code only when its condition turns out to be true, and it simply skips that entire block completely whenever the condition instead turns out to be false, moving straight on to the next line of code below it.



# HOW IT WORKS

# You write the word if, followed by a condition, followed by a colon, then indent every line that should run whenever that condition turns out true. If the condition instead turns out false, Python skips the entire indented block completely and moves calmly on to the next line.

# is_raining = "yes"
# if is_raining == "yes":
#     print("Bring an umbrella!")
 

# Think of it this way

# Bringing an umbrella outside only happens on the days when it is actually raining, and it stays home safely in the closet every other day. The if statement runs its block of code only on the days its condition is true, in that same simple way.

 

# Remember

# The if statement runs its indented block only when the condition is true, and skips it otherwise.

 

# ------------------------------------------------------------

# 4. The if-else Statement

 

# WHAT IT IS

# The if-else statement lets Python choose between two completely different blocks of code, running the first block whenever the condition turns out to be true, and running the second block instead whenever that same condition turns out to be false, never running both blocks together at once.

# HOW IT WORKS

# You write an if block first, followed immediately by an else block placed right underneath it, both indented the exact same amount. Python always runs exactly one of the two blocks, never both, depending entirely on whether the condition turns out to be true or false.

# temperature = 15
# if temperature < 20:
#     print("Wear a jacket")
# else:
#     print("Wear a t-shirt")
 

# Think of it this way

# Choosing between wearing a warm jacket and a light t-shirt depends entirely on whether today feels cold or pleasantly warm outside. The if-else statement chooses between two separate blocks of code in that same either-or way, always picking exactly one and never picking both at once.

 

# Remember

# The if-else statement always runs exactly one of its two blocks, never both, and never neither.

 

# ------------------------------------------------------------

# 5. Activity - Weather Outfit Picker

# WHAT YOU WILL BUILD


# A Weather Outfit Picker that asks about temperature, rain, wind, and puddles, then uses if and if-else statements to decide what outfit, umbrella, windbreaker, and shoes to wear, all while keeping every block properly indented.

# SKILLS PRACTISED

# This single activity practises every topic covered in this lesson together - indentation, conditional statements, the if statement, and the if-else statement, alongside taking input about the weather.

# HOW IT WORKS

# Step 1: Ask for today's temperature and use if-else to decide between a jacket and a t-shirt.

# Step 2: Ask whether it is raining, and use an if statement to print an umbrella reminder.

# Step 3: Ask for the wind speed and use if-else to decide if a windbreaker is needed.

# Step 4: Ask whether there are puddles and use if-else to decide between boots and sneakers.

# Step 5: Print a message that sits outside every if and else block.

# Step 6: Print the final outfit summary with every decision made.

# Remember

# The final picker combines every topic learned in this lesson - indentation, conditional statements, the if statement, and the if-else statement.

# Activity 1
# Title
# Weather Outfit Picker
# Short description:
# A Weather Outfit Picker that asks about temperature, rain, wind, and puddles, then uses if and if-else statements to decide what outfit, umbrella, windbreaker, and shoes to wear, all while keeping every block properly indented.
# Link
# Weather Outfit Picker
# Solution
# Python Code: 

# # PART 1: Ask for today's temperature
# temperature = int(input("Enter today's temperature in Celsius: "))

# # PART 2: Decide between a jacket and a t-shirt
# if temperature < 20:
#     outfit = "jacket"
#     print("It is cold today.")
#     print("Wear a", outfit)
# else:
#     outfit = "t-shirt"
#     print("It is warm today.")
#     print("Wear a", outfit)

# # PART 3: Ask whether it is raining
# is_raining = input("Is it raining today? (yes/no): ")

# # PART 4: Add an umbrella reminder only if it is raining
# if is_raining == "yes":
#     print("Bring an umbrella!")

# # PART 5: Ask for the wind speed
# wind_speed = int(input("Enter the wind speed in km/h: "))

# # PART 6: Decide whether a windbreaker is needed
# if wind_speed > 30:
#     needs_windbreaker = "yes"
#     print("It is windy today.")
#     print("Wear a windbreaker over your", outfit)
# else:
#     needs_windbreaker = "no"
#     print("It is calm today.")
#     print("No windbreaker needed over your", outfit)

# # PART 7: Ask whether there are puddles on the ground
# has_puddles = input("Are there puddles on the ground? (yes/no): ")

# # PART 8: Decide between boots and sneakers
# if has_puddles == "yes":
#     shoes = "boots"
#     print("The ground is wet.")
#     print("Wear", shoes)
# else:
#     shoes = "sneakers"
#     print("The ground is dry.")
#     print("Wear", shoes)

# # PART 9: This message always prints, no matter what was chosen above
# print("")
# print("Weather check complete!")

# # PART 10: Print the final outfit summary
# print("===== WEATHER OUTFIT PICKER =====")
# print("Temperature:", temperature)
# print("Outfit Chosen:", outfit)
# print("Raining:", is_raining)
# print("Windbreaker Needed:", needs_windbreaker)
# print("Shoes Chosen:", shoes)
# print("===================================")
 

# Activity screenshots


# Outcome

# Learning Outcomes of Conditional Statements:

# Indented code blocks correctly under if and else statements.
# Used an if statement to print a message conditionally.
# Used if-else statements to choose between two outfits.
# Took input about the weather to make decisions.
# Printed a final summary combining every weather decision.
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
# Conditional Statements
#  · Warm-Up · Topics · Activity · Wrap-Up · ACP
# Teacher Only
# 0:00 – 2:00
# 2 mins · Scripted
# Warm-Up
# Prior knowledge · Hook · Set the scene
# 2:00 – 14:00
# 12 mins · Topics
# Topics
# Indentation Conditional Statement if Statement if-else Statement
# 14:00 – 15:00
# 1 min · Scripted
# Screen Share & Activity Framing
# Share boilerplate · Confirm setup · Show what we're building
# 15:00 – 33:00
# 18 mins · Activity
# Activity: Weather Outfit Picker
# Indentation · if · if-else · Input · 6 steps Python
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
# Assignment: Daily Activity Planner
# In this assignment, you will build a Daily Activity Planner using Python. You will use indentation, conditional statements, if statements, and if-else statements to suggest daily activities based on temperature, rain, homework time, and free time.

# Open project link
# →
# Goal
# Goal

# By the end of this activity, you will be able to:

# Explain how indentation shows which code belongs inside a condition.
# Use conditional statements to make decisions in a Python program.
# Use an if statement to run a reminder only when a condition is true.
# Use if-else statements to choose between two possible actions.
# Print a final activity summary based on the choices made by the program.
# Getting started
# Getting Started

# Prerequisites
# Basic understanding of Python variables, input(), and print().
# Basic understanding of numbers and text values.
# A Python editor or notebook where you can run Python code.
# Comfort with entering input values while a program is running.
# Project Overview
# You will create a planner that asks for the temperature, rain status, homework time, and free time. The program will choose an activity, give a rain reminder when needed, decide whether a study break is required, and print a final daily activity summary.

 

# Instructions
# Instructions

# Step 1: Ask for the Temperature Use input() to ask for today's temperature. Convert the answer into an integer using int() so it can be compared with a number.

# Step 2: Choose an Activity with if-else Use an if-else statement to choose indoor reading when the temperature is below 20, or outdoor play when it is 20 or higher.

# Step 3: Ask About Rain Ask whether it is raining. Use an if statement to print a reminder only when the answer is yes.

# Step 4: Check Homework Time Ask for the homework time in minutes. Use an if-else statement to decide whether a study break is needed.

# Step 5: Ask About Free Time Ask whether there is free time. Use another if-else statement to choose between hobby time and planning time.

# Step 6: Print the Final Summary Print the temperature, chosen activity, rain status, study break status, and final task so the complete plan is easy to read.

# Step 7: Run and Explore Run the program with different temperatures, rain answers, homework times, and free-time answers. Notice how the output changes each time.

# Success Criteria
# The program asks for temperature, rain status, homework time, and free time.
# The program uses correct indentation inside each if and else block.
# The program uses an if statement to show a rain reminder only when needed.
# The program uses if-else statements to choose activities, break status, and final task.
# The program prints a clear final Daily Activity Planner summary.
# The program runs without syntax or indentation errors.
# Complete Code
# Below is the full Python code for the activity:

# # PART 1: Ask for today's temperature
# temperature = int(input("Enter today's temperature in Celsius: "))
 
# # PART 2: Decide between outdoor and indoor activity
# if temperature < 20:
#     activity = "indoor reading"
#     print("It is cool today.")
#     print("Do", activity)
# else:
#     activity = "outdoor play"
#     print("It is warm today.")
#     print("Do", activity)
 
# # PART 3: Ask whether it is raining
# is_raining = input("Is it raining today? (yes/no): ")
 
# # PART 4: Add a rain reminder only if it is raining
# if is_raining == "yes":
#     print("Choose an indoor activity or carry an umbrella!")
 
# # PART 5: Ask for the homework time
# homework_time = int(input("Enter homework time in minutes: "))
 
# # PART 6: Decide whether study break is needed
# if homework_time > 60:
#     needs_break = "yes"
#     print("You have a long homework session today.")
#     print("Take a short break before your", activity)
# else:
#     needs_break = "no"
#     print("Homework time is short today.")
#     print("No long break needed before your", activity)
 
# # PART 7: Ask whether there is free time
# has_free_time = input("Do you have free time today? (yes/no): ")
 
# # PART 8: Decide between hobby time and planning time
# if has_free_time == "yes":
#     final_task = "hobby time"
#     print("You have free time today.")
#     print("Enjoy your", final_task)
# else:
#     final_task = "planning time"
#     print("You do not have much free time today.")
#     print("Use some time for", final_task)
 
# # PART 9: This message always prints, no matter what was chosen above
# print("")
# print("Daily activity check complete!")
 
# # PART 10: Print the final activity summary
# print("===== DAILY ACTIVITY PLANNER =====")
# print("Temperature:", temperature)
# print("Activity Chosen:", activity)
# print("Raining:", is_raining)
# print("Study Break Needed:", needs_break)
# print("Final Task:", final_task)
# print("==================================")
 

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

# Hint 1: Indentation: Python uses indentation to understand which lines belong inside an if or else block.

# Hint 2: Conditional Statements: A conditional statement checks whether something is true before running a block of code.

# Hint 3: if Statement: Use if when you want a message to appear only when a condition is true.

# Hint 4: if-else Statement: Use if-else when the program must choose between two possible actions.

# Hint 5: Input Values: Use int(input(...)) when the answer needs to be compared with a number.

 

# How was this lesson?
# Your feedback helps us make lessons better.

# Share your feedback
