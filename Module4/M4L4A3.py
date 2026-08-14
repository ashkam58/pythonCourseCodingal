# M4L4A3: Array Operations
# Activity 3: Arrays - Using array module to create, append, reverse, and count elements

import array as arr

# Create integer array
numbers = arr.array('i', [10, 20, 30, 40, 20, 50])
print("Original Array:", numbers)

# Append and count
numbers.append(60)
print("After appending 60:", numbers)
print("Count of 20 in array:", numbers.count(20))

# Reverse array
numbers.reverse()
print("Reversed Array:", numbers)
