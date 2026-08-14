# M4L1A2: Built-in & User-Defined Functions
# Activity 2: Exploring Built-in vs User-Defined Functions and Passing Arguments

# Built-in Functions Examples
num_list = [12.456, 45.891, 3.14159]
print("Built-in len():", len(num_list))
print("Built-in round():", round(num_list[0], 2))

# User-Defined Function: Multiply Price & Items
def multiply_items(unit_price, quantity):
    return unit_price * quantity

# User-Defined Function: Discount Calculator
def apply_discount(total_amount, discount_percent):
    discount = (total_amount * discount_percent) / 100
    final_amount = total_amount - discount
    return round(final_amount, 2)

# Calling functions
price = 15.50
qty = 4
subtotal = multiply_items(price, qty)
final_price = apply_discount(subtotal, 10)

print("Subtotal:", subtotal)
print("Final Price after 10% discount:", final_price)
