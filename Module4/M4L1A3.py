# M4L1A3: Return Statements & Conditional Logic
# Activity 3: Function Return Values and Custom Status Messages

def calculate_change(paid, total):
    return paid - total

def get_order_feedback(item_count):
    if item_count >= 10:
        return "Bulk Order - 15% VIP Discount Applied!"
    elif item_count >= 5:
        return "Medium Order - Free Beverage Included!"
    else:
        return "Standard Order - Thank you for shopping!"

amount_paid = 100.0
total_bill = 67.50
items = 6

change = calculate_change(amount_paid, total_bill)
feedback = get_order_feedback(items)

print("Bill Total:", total_bill)
print("Amount Paid:", amount_paid)
print("Change Due:", round(change, 2))
print("Order Status:", feedback)
