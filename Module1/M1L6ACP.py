# M1L6ACP: Mirrored Triangle Pattern ACP
# After Class Project: Printing a mirrored right-angled triangle pattern

rows = 5

print("Mirrored Triangle Pattern:")
for i in range(1, rows + 1):
    print("  " * (rows - i) + "* " * i)
