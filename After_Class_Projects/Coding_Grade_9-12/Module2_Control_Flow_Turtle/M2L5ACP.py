# M2L5ACP: Loop Art Designer ACP
# After Class Project: Multi-pattern Art Generator

print("===== STAR PYRAMID PATTERN =====")
rows = int(input("Enter number of rows for star pattern: "))

for i in range(rows):
    for j in range(i + 1):
        print("* ", end="")
    print()

print("\n===== FLOYD'S TRIANGLE PATTERN =====")
rows_floyd = int(input("Enter number of rows for Floyd's triangle: "))
num = 1
for i in range(1, rows_floyd + 1):
    for j in range(1, i + 1):
        print(num, end=" ")
        num += 1
    print()
