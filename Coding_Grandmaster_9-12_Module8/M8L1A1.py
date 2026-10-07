# M8L1A1: Operations on List
# Coding Grandmaster (Grades 9-12) - Module 8 Lesson 1 Activity 1

# Creating a list of numbers and strings
fruits = ["apple", "banana", "cherry", "mango", "orange"]
print("Original List:", fruits)

# Appending a new fruit to the list
fruits.append("strawberry")
print("After append('strawberry'):", fruits)

# Inserting at a specific index
fruits.insert(1, "blueberry")
print("After insert at index 1:", fruits)

# Removing an item from list
fruits.remove("banana")
print("After remove('banana'):", fruits)

# Popping the last element
popped_item = fruits.pop()
print("Popped item:", popped_item)
print("List after pop():", fruits)

# Slicing and reversing
print("First 3 fruits:", fruits[:3])
fruits.reverse()
print("Reversed list:", fruits)

# Sorting the list
fruits.sort()
print("Sorted list alphabetically:", fruits)
