# M2L5A2: Floyd's Triangle Pattern
# Activity 2: Pattern Printing - Consecutive Numbers Triangle

rows = int(input("Please Enter total Number of Rows: "))
number = 1

print("\nFloyd's Triangle Pattern:")
for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print(number, end="  ")
        number += 1
    print()
