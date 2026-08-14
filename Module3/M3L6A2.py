# M3L6A2: Calendar Module
# Activity 2: Date, Time, and Calendar Module - Generating Calendar Views

import calendar

year = int(input("Enter year (e.g. 2026): "))
month = int(input("Enter month (1-12): "))

print(f"\n--- Calendar for {calendar.month_name[month]} {year} ---")
print(calendar.month(year, month))

# Check if the year is a leap year
if calendar.isleap(year):
    print(f"{year} is a Leap Year!")
else:
    print(f"{year} is NOT a Leap Year.")
