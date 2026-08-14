# M4L4A2: Set Intersection & Difference
# Activity 2: Sets - Finding shared fruits between two baskets

basket1 = {"apple", "banana", "cherry", "orange"}
basket2 = {"banana", "kiwi", "apple", "mango"}

print("Basket 1:", basket1)
print("Basket 2:", basket2)

shared_fruits = basket1.intersection(basket2)
print("Shared Fruits (Intersection):", shared_fruits)

all_fruits = basket1.union(basket2)
print("All Unique Fruits (Union):", all_fruits)

only_in_b1 = basket1.difference(basket2)
print("Fruits only in Basket 1:", only_in_b1)
