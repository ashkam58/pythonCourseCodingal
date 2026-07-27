# M2L4A3: Multi-level Multiplication Grid
# Activity 3: Nested Loops - Generating NxN multiplication table grid

rows = int(input("Enter grid size N for NxN table: "))

print(f"\n--- {rows}x{rows} Multiplication Grid ---")
for i in range(1, rows + 1):
    for j in range(1, rows + 1):
        print(f"{i*j:4d}", end="")
    print()
