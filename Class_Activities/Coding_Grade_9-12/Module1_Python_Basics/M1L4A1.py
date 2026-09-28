# M1L4A1: Profit or Loss Calculator
# Activity 1: Using if-else to determine profit or loss

cost_price = 500
selling_price = 650

if selling_price > cost_price:
    profit = selling_price - cost_price
    print("Profit made! Profit Amount: $", profit)
elif cost_price > selling_price:
    loss = cost_price - selling_price
    print("Loss incurred! Loss Amount: $", loss)
else:
    print("No profit, no loss.")
