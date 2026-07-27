# M2L5A3: Diamond Pattern of Numbers
# Activity 3: Pattern Printing - Number Diamond Pattern

row_size = int(input("Enter number of rows: "))

if row_size % 2 == 0:
    half_rows = int(row_size / 2)
else:
    half_rows = int(row_size / 2) + 1

space = half_rows - 1

print("\nNumber Diamond Pattern:")

# Upper Half
for i in range(1, half_rows + 1):
    for j in range(1, space + 1):
        print(end=" ")
    space -= 1
    num = 1
    for j in range(2 * i - 1):
        print(end=str(num))
        num += 1
    print()

# Lower Half
space = 1
for i in range(1, half_rows):
    for j in range(1, space + 1):
        print(end=" ")
    space += 1
    num = 1
    for j in range(1, 2 * (half_rows - i)):
        print(end=str(num))
        num += 1
    print()
