# ================================================================
# Course: AI & Coding Grandmaster Course training (Grades 9-12)
# Module 7: Introduction to Python
# Lesson 4: Loops
# After-Class Project (ACP): Armstrong Number
# File: M7L4ACP.py
# ================================================================

# ================================
# ARMSTRONG NUMBER CHECKER
# ================================

# Take input from the user
num = int(input("Enter a number to check: "))

# Calculate the order (number of digits)
order = len(str(num))

# Initialize sum variable
total_sum = 0

# Use a temporary variable to hold the original number during the loop
temp = num

# Loop to extract each digit and add its nth power to the sum
while temp > 0:
    digit = temp % 10
    total_sum += digit ** order
    temp //= 10

# Compare the total sum with the original number
if num == total_sum:
    print(f"{num} is an Armstrong Number.")
else:
    print(f"{num} is not an Armstrong Number.")
