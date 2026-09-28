# M3L6ACP: Trip Date & Time Planner
# After Class Project: Date, Time, and Calendar Module

import datetime
import calendar

print("===== TRIP DATE & TIME PLANNER =====")

# PART 1: Get current date and display calendar
today = datetime.date.today()
print(f"Current Date: {today.strftime('%d-%m-%Y (%A)')}")

year = today.year
month = today.month

print(f"\n--- Current Month Calendar ({calendar.month_name[month]} {year}) ---")
print(calendar.month(year, month))

# PART 2: Ask for trip start date
print("\n--- Enter Trip Details ---")
trip_days = int(input("How many days will your trip last? "))

# Calculate return date using timedelta
trip_duration = datetime.timedelta(days=trip_days)
return_date = today + trip_duration

print("\n===== TRIP SUMMARY =====")
print(f"Departure Date : {today.strftime('%B %d, %Y (%A)')}")
print(f"Duration       : {trip_days} days")
print(f"Return Date    : {return_date.strftime('%B %d, %Y (%A)')}")
print("========================")
print("Have a safe and wonderful trip!")
