# Python Operators - I
# In this lesson, you will learn about Python operators and how to use them in real programs. You will work with arithmetic, floor division, modulus, comparison, and assignment operators — and apply all of them by building a Farm Harvest Calculator.

# Overview
# Activities
# Outcome
# Agenda
# Overview
# List of Topics

# 1.  What is an Operator?

# 2.  Arithmetic Operators

# 3.  Floor Division and Modulus

# 4.  Comparison Operators

# 5.  Assignment Operators

# 6.  Activity Explanation

 

# 1. What is an Operator?

# WHAT IT IS

# An operator is a special symbol in Python that tells the computer to perform a specific action on one or more values. The values that an operator works on are called operands. Think about a calculator app on your phone — when you type 45 + 18, the + symbol is the operator and the numbers 45 and 18 are the operands. The calculator reads the operator, understands what action to take, performs it, and gives you the answer. Python works exactly the same way — operators are the instructions, and operands are the values those instructions act on. Without operators, a program could store data but could never do anything useful with it — no adding, no comparing, no updating.


 

# HOW IT WORKS

# In Python, you write an operator between two operands to perform an operation. For example, 3 + 4 adds the numbers 3 and 4 together and produces 7. Here, + is the operator and 3 and 4 are the operands. Operators are grouped into types depending on what they do — arithmetic operators do maths, comparison operators check relationships between values, and assignment operators store or update values in variables. Python evaluates the expression and returns a result that you can print, store in a variable, or use in the next step of your program.

# result = 3 + 4   # + is the operator
#                  # 3 and 4 are the operands
# print(result)    # Output: 7
 

# 🎯  Think of it this way

# Think of a recipe instruction: "Add 2 cups of flour to 1 cup of sugar." Here, "Add" is the operator — the action to perform. "2 cups of flour" and "1 cup of sugar" are the operands — the values being acted on. The result is the mixture. Python operators work the same way: they are the cooking instructions that tell Python exactly what to do with the ingredients (operands) you give it.

 

# ✅  Remember

# An operator is the action symbol (+, -, *, /) and an operand is the value it acts on. Every expression in Python has at least one operator and one or more operands.

 

# 2. Arithmetic Operators

# WHAT IT IS

# Arithmetic operators perform the standard mathematical calculations you use every day — addition, subtraction, multiplication, division, and more. You use arithmetic operators constantly in real life without even thinking about it: splitting a restaurant bill equally among friends, calculating how much change you get at a shop, working out the total cost of items in a cart, or finding the average score in a cricket match. Python has seven arithmetic operators, and each one maps directly to a maths operation you already know from school. Once you learn them in Python, you can automate any calculation that would otherwise take paper and pencil.


 

# HOW IT WORKS

# The seven arithmetic operators are: + for addition, - for subtraction, * for multiplication, / for division (gives a decimal answer), ** for exponentiation (power of), // for floor division (whole number answer only), and % for modulus (the remainder after division). You write them between two values or variables just like a maths equation. Division using / always returns a float (decimal number) even if the answer is a whole number — for example, 8 / 4 gives 2.0, not 2. To get only the whole number part of a division, use // instead. Exponentiation with ** is very useful for scientific calculations — 2 ** 10 gives 1024.

# total    = 120 + 85 + 150 + 95 + 110  # addition
# earnings = total * 15                  # multiplication
# average  = total / 5                   # division (float)
# print(total, earnings, average)
# # Output: 560  8400  112.0
 

# 🎯  Think of it this way

# Imagine you are the cashier at your school tuck shop at the end of the day. You use addition to total up all the sales, subtraction to calculate the change you gave customers, multiplication to work out how much 6 samosas at ₹5 each cost (6 * 5 = ₹30), and division to split the day's profit equally among two shop helpers. Python arithmetic operators do all of these calculations instantly — no paper, no calculator, just code.

 

# ✅  Remember

# Division with / always returns a float. Use // when you only want the whole number part of the answer.

 

# 3. Floor Division and Modulus

# WHAT IT IS

# Floor division (//) and modulus (%) are two special arithmetic operators that are extremely useful whenever you need to divide things into equal groups in real life. Floor division tells you how many complete groups you can make — it throws away any leftover and gives you only the whole number. Modulus tells you exactly how much is left over after you have made as many complete groups as possible. Together they answer the two most common real-life sharing questions: "How many full portions can I make?" and "How much is left over?" You use this logic every time you pack bags of groceries, split chocolates among friends, or figure out how many buses are needed for a school trip.


 

# HOW IT WORKS

# Write // between two numbers to get floor division — Python divides and drops the decimal part completely, keeping only the whole number. For example, 17 // 5 gives 3 because you can fit three complete groups of 5 into 17. Write % between two numbers for modulus — Python divides and gives you only the remainder. 17 % 5 gives 2 because after three groups of 5 (which use up 15), there are 2 left over. A very common pattern is using // and % together: first use // to find how many complete portions, then % to find what is left over. This is exactly how an ATM decides how many ₹500, ₹100, and ₹50 notes to dispense for a withdrawal.

# total    = 560       # total harvest in kg
# bag_size = 25        # each bag holds 25 kg

# bags     = total // bag_size  # 560 // 25 = 22 full bags
# leftover = total % bag_size   # 560 % 25  = 10 kg left over

# print("Full bags:", bags)      # Output: 22
# print("Leftover:", leftover)   # Output: 10
 

# 🎯  Think of it this way

# Imagine you have 17 chocolates and 5 friends. You want to give everyone the same number without cutting any chocolate. 17 // 5 = 3 — each friend gets 3 chocolates. 17 % 5 = 2 — two chocolates are left over for you! Floor division tells you the fair share, and modulus tells you what is left after sharing. This is exactly what Python does when a farmer packs grain into bags or an ATM counts notes for a withdrawal.

 

# ✅  Remember

# // gives the whole number quotient. % gives the remainder. Use them together whenever you need to split things into equal groups and find what is left over.

 

# 4. Comparison Operators

# WHAT IT IS

# Comparison operators compare two values and always return one of two results: True or False. They are the decision-makers of Python — they let your program ask questions about data and act differently depending on the answer. You use comparisons in real life constantly without realising it: "Is my score higher than 35 to pass?", "Is the price less than my budget?", "Did I save exactly ₹500 this week?", "Is today's temperature greater than or equal to yesterday's?" Every time a website checks whether your password is correct, or a game checks whether your score beats the high score, or a shop checks whether you have enough loyalty points for a discount — comparison operators are running behind the scenes.



# HOW IT WORKS

# Python has six comparison operators. == checks if two values are equal (note: this is double equals, not single). != checks if two values are not equal. > checks if the left value is greater than the right. < checks if the left value is less than the right. >= checks if the left value is greater than or equal to the right. <= checks if the left value is less than or equal to the right. The result is always a Boolean — either True or False. A very common mistake is using = instead of == when checking equality — remember, = assigns a value, while == compares two values.

# total     = 560
# last_year = 500

# print(total > last_year)   # True  — 560 is greater than 500
# print(total == last_year)  # False — 560 is not equal to 500
# print(total >= last_year)  # True  — 560 is at least as good
# print(total < 400)         # False — 560 is not less than 400
 

# 🎯  Think of it this way

# Think of the security guard at a school sports event who checks your entry ticket. He asks one question — "Is your ticket number valid?" — and the answer is simply Yes or No. Comparison operators are exactly like that security guard: they ask one question about two values and give back only True (yes, valid) or False (no, invalid). Your program then uses that True or False to decide what to do next — just like the guard lets you in or turns you away.

 

# ✅  Remember

# = assigns a value. == compares two values. Never use a single = when you want to check if two things are equal — always use ==.

 

# 5. Assignment Operators

# WHAT IT IS

# Assignment operators store values into variables or update the value already stored in a variable. The simplest assignment operator is = which stores a value for the first time. But the real power comes from the shorthand operators like += and -= which let you update a variable's value without having to rewrite it fully. Think about a bank passbook — your balance starts at some amount, and every deposit increases it while every withdrawal reduces it. Each transaction updates the same balance rather than creating a new one from scratch. Assignment operators work exactly like that — they modify the existing value in a variable and store the result back into the same variable in one short step.

# HOW IT WORKS

# The simple assignment operator = stores a value: total = 560 puts 560 into the variable total. The shorthand operator += adds a value to what is already in the variable: total += 30 is exactly the same as writing total = total + 30. Similarly, -= subtracts, *= multiplies, /= divides, //= floor-divides, %= applies modulus, and **= raises to a power — all in one step. These shorthand operators save you from rewriting the variable name twice and make code much cleaner and easier to read. They are especially useful in loops and programs that keep a running total — like a score counter in a game or a savings tracker.

# total = 560        # = stores 560 into total
# total += 30        # same as: total = total + 30
# print(total)       # Output: 590
# total -= 15        # same as: total = total - 15
# print(total)       # Output: 575
# bags = total // 25 # recalculate bags after update
# print(bags)        # Output: 23
 

# 🎯  Think of it this way

# Imagine your pocket money piggy bank. You start the month with ₹200 (total = 200). Your grandfather gives you ₹50 as a gift — you add it: total += 50, so now you have ₹250. You spend ₹30 on a notebook — you subtract it: total -= 30, leaving ₹220. You don't start a brand new piggy bank each time — you update the same one. Assignment operators do exactly this in Python: they update the existing variable instead of creating a new one every time.

 

# ✅  Remember

# total += 30 is a shortcut for total = total + 30. Use shorthand assignment operators whenever you are updating a variable that already has a value.

 

# 6. Activity — Farm Harvest Calculator

 

# WHAT YOU WILL BUILD


# A Python program that tracks a farmer's harvest across 5 fields. You will calculate the total and average yield, pack the harvest into 25 kg bags, find the leftover grain, compare this year's harvest with last year's, and update the total with a bonus crop and seed reserve.

# SKILLS PRACTISED

# Assignment (=), arithmetic (+, *, /), floor division (//), modulus (%), comparison (>, ==, >=), and shorthand assignment (+=, -=).

# STEPS

# Step 1:  Store the yield in kg for each of the 5 fields in separate variables using =.

# Step 2:  Use + to add all 5 fields and store the result in total. Print total.

# Step 3:  Calculate average using total / 5. Print average.

# Step 4:  Set price_per_kg = 15 and calculate earnings = total * price_per_kg. Print earnings.

# Step 5:  Use // to find how many full 25 kg bags can be packed. Store in bags. Print bags.

# Step 6:  Use % to find the leftover grain after packing. Store in leftover. Print leftover.

# Step 7:  Set last_year = 500. Use >, ==, >= to compare total with last_year. Print each result.

# Step 8:  Use += to add 30 kg bonus crop to total. Print the updated total.

# Step 9:  Use -= to subtract 15 kg saved as seeds. Print the updated total.

# Step 10:  Recalculate bags = total // 25 after all updates. Print the final bag count.

 

# ✅  Remember

# = stores a value. == compares two values. Never mix them up — = in a comparison will cause an error.

 

# Activity 1
# Title
# Farm Harvest Calculator
# Short description:
# A Python program that tracks a farmer's harvest across 5 fields. You will calculate the total and average yield, pack the harvest into 25 kg bags, find the leftover grain, compare this year's harvest with last year's, and update the total with a bonus crop and seed reserve.
# Link
# Farm Harvest Calculator
# Solution
# # ============================================================
# # Farm Harvest Calculator
# # ============================================================

# # --- Assignment Operator (=) ---
# # Store the harvest in kg from each of the 5 fields
# field1 = 120
# field2 = 85
# field3 = 150
# field4 = 95
# field5 = 110

# # --- Arithmetic Operators (+, -, *, /) ---
# # Calculate total and average harvest
# total   = field1 + field2 + field3 + field4 + field5
# average = total / 5

# print("Total harvest      :", total, "kg")
# print("Average per field  :", average, "kg")

# # Price per kg is 15 rupees — calculate total earnings
# price_per_kg = 15
# earnings = total * price_per_kg
# print("Total earnings     : Rs.", earnings)

# # --- Floor Division (//) and Modulus (%) ---
# # Pack the harvest into bags of 25 kg each
# bags     = total // 25
# leftover = total % 25

# print("Full bags packed   :", bags)
# print("Leftover grain     :", leftover, "kg")

# # --- Comparison Operators (>, <, ==, >=) ---
# # Compare this year's harvest with last year
# last_year = 500
# print("Better than last year?  :", total > last_year)
# print("Same as last year?      :", total == last_year)
# print("At least as good?       :", total >= last_year)

# # --- Assignment Operators (+=, -=) ---
# # A bonus field adds 30 kg to the total
# total += 30
# print("After bonus crop   :", total, "kg")

# # Subtract 15 kg saved as seeds for next season
# total -= 15
# print("After seed reserve :", total, "kg")

# # Final bag count after all adjustments
# bags = total // 25
# print("Final bags packed  :", bags)
 

# Activity screenshots


# Outcome

# Learning Outcomes of Python Operators - I

 

# •  Understood what operators and operands are in Python.

# •  Used arithmetic operators (+, -, *, /) to perform calculations.

# •  Applied floor division (//) to find how many complete groups fit into a total.

# •  Used modulus (%) to find the remainder after dividing into equal groups.

# •  Compared values using comparison operators and interpreted True/False results.

# •  Distinguished clearly between the assignment operator (=) and the equality operator (==).

# •  Updated variables efficiently using shorthand assignment operators (+=, -=).

 

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
# Python Operators - I
# · Warm-Up · Topics · Activity · Wrap-Up · ACP
# Teacher Only
# 0:00 – 2:00
# 2 mins · Scripted
# Warm-Up
# Prior knowledge · Hook · Set the scene
# 2:00 – 14:00
# 12 mins · Topics
# Topics
# What is an Operator? Arithmetic Operators Floor Division & Modulus Comparison Operators Assignment Operators
# 14:00 – 15:00
# 1 min · Scripted
# Screen Share & Activity Framing
# Share boilerplate · Confirm setup · Show what we're building
# 15:00 – 33:00
# 18 mins · Activity
# Activity: Farm Harvest Calculator
# Arithmetic · Floor div · Modulus · Comparison · Assignment · 10 steps Python
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
# Assignment: Classroom Points Calculator
# In this assignment, you will build a Classroom Points Calculator using Python. You will store team points, calculate total and average points, pack reward stars into boxes, compare scores with last week, and update totals using assignment operators.

# Open project link
# →
# Goal
# Goal

# By the end of this activity, you will be able to:

# Explain how operators help Python perform calculations and comparisons.
# Use arithmetic operators to find total points, averages, and reward stars.
# Use floor division and modulus to calculate full boxes and leftovers.
# Use comparison operators to compare this week's points with last week's points.
# Use assignment operators such as =, +=, and -= to store and update values.
# Getting started
# Getting Started

# Prerequisites
# Basic understanding of Python variables and print().
# Basic familiarity with numbers and simple calculations.
# A Python editor or notebook where you can run Python code.
# Ability to read simple outputs printed in the console.
# Project Overview
# You will create a calculator for classroom team points. The program will store points for five teams, calculate the total and average, convert points into reward stars, pack stars into boxes, compare the result with last week, and update the total after bonus and penalty changes.

 

# Instructions
# Instructions

# Step 1: Store Team Points
# Create variables for five classroom teams. Use the assignment operator = to store each team's points.

# Step 2: Calculate Total and Average
# Use arithmetic operators to add all team points and divide the total by 5 to find the average points per team.

# Step 3: Calculate Reward Stars
# Create a variable for stars_per_point, then multiply the total points by this value to find the total reward stars.

# Step 4: Use Floor Division and Modulus
# Use // to find how many full boxes of 25 reward stars can be packed. Use % to find how many stars are left over.

# Step 5: Compare with Last Week
# Create a last_week variable and use >, ==, and >= to compare this week's total with last week's score.

# Step 6: Update the Total
# Use += to add bonus points and -= to subtract missed-task points. Print the updated total after each change.

# Step 7: Run and Explore
# Run the program and read each output. Change the team points, reward stars per point, or box size, then run it again to see how the results change.

# Success Criteria
# The program stores points for five teams using variables.
# The program calculates total points and average points correctly.
# The program uses multiplication to calculate total reward stars.
# The program uses floor division and modulus to show full boxes and leftover stars.
# The program uses comparison operators to compare scores with last week.
# The program updates the total using += and -= assignment operators.
# Complete Code
# Below is the full Python code for the activity

# # ============================================================
# # Classroom Points Calculator
# # ============================================================
 
# # --- Assignment Operator (=) ---
# # Store the points earned by 5 classroom teams
# team1 = 120
# team2 = 95
# team3 = 140
# team4 = 110
# team5 = 85
 
# # --- Arithmetic Operators (+, -, *, /) ---
# # Calculate total and average points
# total = team1 + team2 + team3 + team4 + team5
# average = total / 5
 
# print("Total points       :", total)
# print("Average per team   :", average)
 
# # Each point gives 2 reward stars
# stars_per_point = 2
# reward_stars = total * stars_per_point
# print("Total reward stars :", reward_stars)
 
# # --- Floor Division (//) and Modulus (%) ---
# # Pack reward stars into boxes of 25 stars each
# boxes = reward_stars // 25
# leftover = reward_stars % 25
 
# print("Full boxes packed  :", boxes)
# print("Leftover stars     :", leftover)
 
# # --- Comparison Operators (>, <, ==, >=) ---
# # Compare this week's points with last week's points
# last_week = 500
 
# print("Better than last week? :", total > last_week)
# print("Same as last week?     :", total == last_week)
# print("At least as good?      :", total >= last_week)
 
# # --- Assignment Operators (+=, -=) ---
# # Bonus challenge adds 30 points to the total
# total += 30
# print("After bonus points :", total)
 
# # 15 points are removed for missed tasks
# total -= 15
# print("After missed tasks :", total)
 
# # Final reward box count after all changes
# reward_stars = total * stars_per_point
# boxes = reward_stars // 25
 
# print("Final boxes packed :", boxes)
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

# Hint 1: Assignment Operator
# Use = to store a value in a variable. For example, team1 = 120 stores 120 points in team1.

# Hint 2: Arithmetic Operators
# Use + to add numbers, * to multiply, and / to divide. These help you calculate totals, reward stars, and averages.

# Hint 3: Floor Division and Modulus
# Use // when you want only the number of full groups. Use % when you want the leftover amount.

# Hint 4: Comparison Operators
# Comparison operators such as >, ==, and >= return either True or False.

# Hint 5: Assignment Updates
# Use += to add to an existing value and -= to subtract from an existing value without rewriting the full expression.

 

# How was this lesson?
# Your feedback helps us make lessons better.

# Share your feedback
