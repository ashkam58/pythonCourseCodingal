# M1L6A2: Right Triangle Star Pattern
# Activity 2: Printing star patterns using nested loops

rows = 5

print("Right Triangle Pattern:")
for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print("*", end=" ")
    print()
