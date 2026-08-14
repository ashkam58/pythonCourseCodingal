# M3L1A2: Built-in & User-Defined Functions
# Activity 2: Built-in vs User-Defined Functions and Passing Arguments

num_list = [12.456, 45.891, 3.14159]
print("Built-in len():", len(num_list))
print("Built-in round():", round(num_list[0], 2))

def multiply_items(unit_price, quantity):
    return unit_price * quantity

def apply_discount(total_amount, discount_percent):
    discount = (total_amount * discount_percent) / 100
    return round(total_amount - discount, 2)

subtotal = multiply_items(15.50, 4)
final_price = apply_discount(subtotal, 10)

print("Subtotal:", subtotal)
print("Final Price (10% off):", final_price)
