# M4L4A1: Set Operations Basics
# Activity 1: Sets and Arrays - Creating sets, adding items, removing duplicates

my_set = {1, 2, 3, 4, 3, 2}
print("Set automatically removes duplicates:", my_set)

my_set.add(5)
print("After adding 5:", my_set)

my_set.discard(2)
print("After discarding 2:", my_set)

print("Check if 3 in set:", 3 in my_set)
