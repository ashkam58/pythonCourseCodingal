# M2L1A3: Vending Machine Selection
# Activity 3: Nested Conditional Statements - Multi-level Drink Selector

print("=== VENDING MACHINE ===")
print("1 - Cold Drinks")
print("2 - Hot Drinks")

category = int(input("Select category (1 or 2): "))

if category == 1:
    print("\nCold Drink Options:")
    print("1 - Fruit Juice")
    print("2 - Iced Tea")
    drink = int(input("Select drink (1 or 2): "))
    if drink == 1:
        print("Dispensing Fresh Fruit Juice. Enjoy!")
    else:
        print("Dispensing Chilled Iced Tea. Enjoy!")
elif category == 2:
    print("\nHot Drink Options:")
    print("1 - Coffee")
    print("2 - Hot Chocolate")
    drink = int(input("Select drink (1 or 2): "))
    if drink == 1:
        print("Dispensing Hot Coffee. Enjoy!")
    else:
        print("Dispensing Rich Hot Chocolate. Enjoy!")
else:
    print("Invalid selection. Please try again.")
