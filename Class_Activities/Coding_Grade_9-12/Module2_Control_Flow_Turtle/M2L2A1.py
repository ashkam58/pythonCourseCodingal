# M2L2A1: Sum of Whole Numbers
# Activity 1: Calculating sum of first N whole numbers using for loop

n = int(input("Enter the number whose sum you want to find: "))
total_sum = 0

for i in range(1, n + 1):
    total_sum += i
    print(f"Step {i}: Current Sum = {total_sum}")

print(f"\nFinal Sum of first {n} numbers = {total_sum}")
