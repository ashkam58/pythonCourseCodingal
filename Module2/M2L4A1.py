# M2L4A1: ATM Cash Dispenser
# Activity 1: Nested Loops - Outer loop per customer, inner loop for bill calculation

print("=== ATM Cash Dispenser ===\n")

serving = True
while serving:
    name = input("Enter customer name (or 'exit' to quit): ")
    if name.lower() == 'exit':
        break

    amount = int(input(f"Hello {name}! Enter withdrawal amount ($): "))
    if amount <= 0:
        print("Invalid amount. Please enter a positive number.\n")
        continue

    print(f"\nDispensing ${amount} for {name}:")
    remaining = amount

    for bill in [100, 50, 20, 10, 5, 1]:
        count = remaining // bill
        if count > 0:
            print(f"  ${bill} bills : {count}")
            remaining %= bill

    print("\nTransaction Complete!\n")
