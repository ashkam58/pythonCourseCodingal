# ================================================================
# Course: AI & Coding Grandmaster Course training (Grades 9-12)
# Module 7: Introduction to Python
# Lesson 3: Conditional Statements and Date Time Module
# Class Activity: My Weather Reporter
# File: M7L3A1.py (my-weather-reporter.py)
# ================================================================

import datetime
import calendar

# PART 1 - USER INPUT
city = input("Enter your city name: ")
temp = float(input("Enter today's temperature in C: "))

# PART 2 - if STATEMENT
if temp > 35:
    print("Warning: It is very hot today!")

# PART 3 - if-else
if temp > 25:
    print("Great day to go outside!")
else:
    print("Grab a jacket before you go out!")

# PART 4 - if-elif-else
if temp > 35:
    print("Weather: Scorching Hot")
elif temp > 25:
    print("Weather: Warm and Sunny")
elif temp > 15:
    print("Weather: Cool and Breezy")
else:
    print("Weather: Cold - stay warm!")

# PART 5 - datetime MODULE
now = datetime.datetime.now()
print("City:", city)
print("Time now:", now)
print(calendar.calendar(now.year))
