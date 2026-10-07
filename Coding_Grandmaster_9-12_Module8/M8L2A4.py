# M8L2A4: Set Intersection
# Coding Grandmaster (Grades 9-12) - Module 8 Lesson 2 Activity 4

# Sets representing subjects taken by students
python_students = {"Ashkam", "Diya", "Karan", "Simran", "Rahul", "Aarav"}
ai_students = {"Karan", "Ashkam", "Zoya", "Rahul", "Farhan"}

print("Python Course Students:", python_students)
print("AI Course Students:", ai_students)

# Set Intersection using ampersand (&)
both_courses_op = python_students & ai_students
print("\nStudents enrolled in BOTH courses (& operator):", both_courses_op)

# Set Intersection using intersection() method
both_courses_method = python_students.intersection(ai_students)
print("Students enrolled in BOTH courses (.intersection()):", both_courses_method)

# Set Difference (Only Python, not AI)
only_python = python_students - ai_students
print("Students enrolled ONLY in Python:", only_python)

# Symmetric Difference (In either Python or AI, but NOT both)
either_not_both = python_students ^ ai_students
print("Students in only one course (Symmetric Difference):", either_not_both)
