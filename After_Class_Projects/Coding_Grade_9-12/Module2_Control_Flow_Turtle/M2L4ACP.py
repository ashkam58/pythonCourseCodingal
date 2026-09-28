# M2L4ACP: Grocery Billing Queue
# After Class Project: Nested Loops Billing Queue

print("=== Grocery Billing Queue ===\n")

total_sales = 0
billing = True

while billing:
    name = input("Enter customer name (or 'done' to stop): ")
    if name.lower() == 'done':
        break

    item_count = int(input(f"Hello {name}! How many items are in your cart? "))
    bill_total = 0

    for item_idx in range(1, item_count + 1):
        price = float(input(f"  Enter price for item #{item_idx}: $"))
        bill_total += price

    print(f"Total bill for {name}: ${bill_total:.2f}\n")
    total_sales += bill_total

print(f"Queue Closed! Total Sales Today: ${total_sales:.2f}")
