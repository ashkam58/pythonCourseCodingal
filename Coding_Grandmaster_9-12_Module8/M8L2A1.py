# M8L2A1: Operations on Tuple
# Coding Grandmaster (Grades 9-12) - Module 8 Lesson 2 Activity 1

# Creating tuples
rainbow_colors = ("red", "orange", "yellow", "green", "blue", "indigo", "violet")
print("Original Tuple:", rainbow_colors)
print("Type:", type(rainbow_colors))

# Indexing and slicing
print("First color:", rainbow_colors[0])
print("Last color:", rainbow_colors[-1])
print("Middle 3 colors:", rainbow_colors[2:5])

# Immutability demonstration
print("\nTuples are immutable: elements cannot be modified in-place.")

# Counting and index
numbers_tuple = (10, 20, 30, 20, 40, 20, 50)
print("Count of 20 in tuple:", numbers_tuple.count(20))
print("First index of 30 in tuple:", numbers_tuple.index(30))

# Tuple packing and unpacking
coordinates = (12.9716, 77.5946)
latitude, longitude = coordinates
print(f"Unpacked Coordinates -> Lat: {latitude}, Long: {longitude}")
