# M4L3A3: Early Function Termination with return
# Activity 3: Demonstrating how return ends function execution immediately

def check_age_for_discount(age):
    if age < 0:
        print("Invalid age entered.")
        return "ERROR"  # Function terminates immediately here

    print("Age is valid. Calculating discount category...")

    if age >= 60:
        return "Senior Discount (20%)"
    elif age <= 12:
        return "Child Discount (30%)"
    else:
        return "Standard Price (No Discount)"

# Calling function with different inputs
print("Age -5 :", check_age_for_discount(-5))
print("Age 65 :", check_age_for_discount(65))
print("Age 25 :", check_age_for_discount(25))
