# ================================================================
# Course: AI & Coding Grandmaster Course training (Grades 9-12)
# Module 7: Introduction to Python
# Lesson 3: Conditional Statements and Date Time Module
# After-Class Project (ACP): My Daily Mood Advisor
# File: M7L3ACP.py
# ================================================================

import datetime

# PART 1 - USER INPUT
name = input("Enter your name: ")
mood = input("How are you feeling today? happy/sad/tired/stressed/excited: ")
energy = int(input("Enter your energy level from 1 to 10: "))

# PART 2 - THE if STATEMENT
if energy < 3:
    print("Alert: Your energy seems low today. Take some rest if needed.")

# PART 3 - if-else STATEMENT
if energy >= 5:
    print("You have enough energy to do something productive today!")
else:
    print("Take it slow today and do something relaxing.")

# PART 4 - if-elif-else STATEMENT
if mood == "happy":
    advice = "Keep spreading your positive energy!"
elif mood == "sad":
    advice = "Talk to someone you trust or do something that makes you feel better."
elif mood == "tired":
    advice = "Drink water, take a short break, and rest your mind."
elif mood == "stressed":
    advice = "Try deep breathing or make a small to-do list."
elif mood == "excited":
    advice = "Use your excitement to start something creative!"
else:
    advice = "Every mood is okay. Take care of yourself today."

# PART 5 - datetime MODULE
today = datetime.datetime.now()

# FINAL OUTPUT
print("\n================================")
print("DAILY MOOD ADVISOR REPORT")
print("================================")
print("Name:", name)
print("Mood:", mood)
print("Energy Level:", energy)
print("Date and Time:", today)
print("Advice:", advice)
print("================================")
