# M8L2ACP: Tuple to List & List to Tuple Converter
# Coding Grandmaster (Grades 9-12) - Module 8 Lesson 2 After Class Project

# Initial immutable tuple
original_tuple = ("Python", "Machine Learning", "Data Science", "Deep Learning")
print("Original Tuple (Immutable):", original_tuple)
print("Type:", type(original_tuple))

# Convert Tuple to List to enable modifications
converted_list = list(original_tuple)
print("\nConverted to List (Mutable):", converted_list)
print("Type:", type(converted_list))

# Modify the list: add new topics
converted_list.append("Natural Language Processing")
converted_list.append("Computer Vision")
converted_list.sort()
print("\nList after additions and sorting:", converted_list)

# Convert modified list back to an immutable tuple
final_tuple = tuple(converted_list)
print("\nFinal Converted Tuple:", final_tuple)
print("Type:", type(final_tuple))
print(f"Total topics finalized in course curriculum: {len(final_tuple)}")
