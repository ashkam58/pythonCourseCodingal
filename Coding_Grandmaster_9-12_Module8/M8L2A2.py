# M8L2A2: Operations on Set
# Coding Grandmaster (Grades 9-12) - Module 8 Lesson 2 Activity 2

# Creating a set with duplicate values
numbers_set = {1, 2, 3, 4, 3, 2, 1, 5, 6}
print("Original Set (duplicates auto-removed):", numbers_set)

# Adding elements to a set
numbers_set.add(7)
numbers_set.add(8)
print("After adding 7 and 8:", numbers_set)

# Removing elements using remove() and discard()
numbers_set.remove(1)
numbers_set.discard(100) # discard doesn't raise error if element not found
print("After removing 1:", numbers_set)

# Membership testing
print("Is 5 in the set?", 5 in numbers_set)
print("Is 10 in the set?", 10 in numbers_set)

# Iterating through set
print("Set elements:")
for item in numbers_set:
    print(f" - {item}")
