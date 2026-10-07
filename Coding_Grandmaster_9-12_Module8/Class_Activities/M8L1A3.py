# M8L1A3: List to Dictionary
# Coding Grandmaster (Grades 9-12) - Module 8 Lesson 1 Activity 3

# Two separate lists: keys and values
roll_numbers = [101, 102, 103, 104, 105]
student_names = ["Alice", "Bob", "Charlie", "David", "Emma"]

print("Keys list:", roll_numbers)
print("Values list:", student_names)

# Converting two lists into a dictionary using zip()
students_dict = dict(zip(roll_numbers, student_names))
print("\nCreated Dictionary from two lists:")
print(students_dict)

# List of tuples to dictionary
tuple_pairs = [("Python", 1991), ("Java", 1995), ("JavaScript", 1995), ("C++", 1985)]
lang_dict = dict(tuple_pairs)
print("\nDictionary from list of tuples:")
print(lang_dict)

# Dictionary comprehension from single list
numbers = [1, 2, 3, 4, 5, 6]
squares_dict = {num: num ** 2 for num in numbers}
print("\nDictionary with numbers and their squares:")
print(squares_dict)
