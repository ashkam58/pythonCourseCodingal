# M3L6A3: Time Differences & Execution Time
# Activity 3: Measuring Execution Time and Calculating Date Differences

import time
import datetime

# Calculate date difference (Days remaining in current year)
today = datetime.date.today()
end_of_year = datetime.date(today.year, 12, 31)
days_left = (end_of_year - today).days

print("Today's Date:", today)
print("Days remaining in the year:", days_left)

# Measuring code execution time using time module
start_time = time.time()
print("\nMeasuring loop performance...")

total = 0
for i in range(1, 1000000):
    total += i

end_time = time.time()
execution_time = end_time - start_time
print(f"Loop completed in {execution_time:.4f} seconds.")
