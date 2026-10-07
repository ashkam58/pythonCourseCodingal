# M8L1A2: Operations on Dictionary
# Coding Grandmaster (Grades 9-12) - Module 8 Lesson 1 Activity 2

# Creating a student record dictionary
student_info = {
    "name": "Ashkam",
    "grade": 10,
    "course": "AI & Coding Grandmaster",
    "marks": 95
}
print("Original Dictionary:", student_info)

# Accessing values using keys and get()
print("Student Name:", student_info["name"])
print("Course:", student_info.get("course"))

# Adding a new key-value pair
student_info["school"] = "Delhi Public School"
print("After adding school:", student_info)

# Updating an existing value
student_info["marks"] = 98
print("After updating marks:", student_info)

# Getting keys and values
print("All Keys:", list(student_info.keys()))
print("All Values:", list(student_info.values()))
print("Key-Value Pairs (Items):", list(student_info.items()))

# Removing a key using pop()
removed_grade = student_info.pop("grade")
print("Removed grade:", removed_grade)
print("Dictionary after pop:", student_info)
