# M3L6A1: Current Date and Time
# Activity 1: Date, Time, and Calendar Module - Working with datetime

import datetime

# Using datetime.now() to get current local date and time
now = datetime.datetime.now()

print("Current Date and Time:", now)
print("Year:", now.year)
print("Month:", now.month)
print("Day:", now.day)
print("Hour:", now.hour)
print("Minute:", now.minute)
print("Formatted Date:", now.strftime("%B %d, %Y (%A)"))
