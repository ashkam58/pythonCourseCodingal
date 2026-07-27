# M1L5A1: For Loop & Range Function (Sum of Natural Numbers)
# Activity 1: Calculating sum of first N natural numbers using for loop

n = 10
total_sum = 0

for i in range(1, n + 1):
    total_sum += i

print("Sum of natural numbers from 1 to", n, "is:", total_sum)
