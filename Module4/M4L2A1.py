# M4L2A1: Tip, the Waiter
# Activity 1: Positional Arguments - Calculating Restaurant Bill & Tip

def total_calc(bill_amount, tip_perc):
    # Calculate the tip on bill
    total = bill_amount * (1 + 0.01 * tip_perc)
    total = round(total, 2)
    print(f"Please pay ${total}")

# Calling function using positional arguments
total_calc(150, 20)
