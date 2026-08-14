# M4L7A1: Tuple Operations
# Activity 1: Tuple Creation, Immutability, Concatenation (+ operator), Count & Slicing

# Create a tuple with different data types
tuplex = ("tuple", False, 3.2, 1)
print("Mixed Tuple:", tuplex)

# Create a tuple of integers
tuplex = (4, 6, 2, 8, 3, 1)
print("Integer Tuple:", tuplex)

# Tuples are immutable, so you cannot add new elements directly.
# Using merge of tuples with the + operator, you can add an element and it creates a new tuple.
tuplex = tuplex + (9,)
print("After adding 9 using +:", tuplex)

# Counts the number of occurrences of item 50 from a tuple
tuple1 = (50, 10, 60, 70, 50)
print("Count of 50 in tuple1:", tuple1.count(50))

# Create a tuple for slicing
tuplex = (2, 4, 3, 5, 4, 6, 7, 8, 6, 1)
# tuple[start:stop]
_slice = tuplex[3:5]
print("Slice [3:5]:", _slice)

# Slicing from the beginning
_slice = tuplex[:6]
print("Slice [:6]:", _slice)
