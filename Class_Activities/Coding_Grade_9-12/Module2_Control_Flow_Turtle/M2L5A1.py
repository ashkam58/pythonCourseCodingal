# M2L5A1: Right Angle Triangle Star Pattern
# Activity 1: Pattern Printing - Half Pyramid of Stars

n = int(input("Enter number of rows: "))

print("\nHalf Pyramid Pattern of Stars (*):")
for i in range(n):
    for j in range(i + 1):
        print("* ", end="")
    print()
