# M2L8ACP: Student Grade & Attendance System
# After Class Project: Complete Module 2 Capstone System

print("=== STUDENT ACADEMIC SYSTEM ===\n")

num_students = int(input("Enter total number of students: "))
student_records = []

for i in range(1, num_students + 1):
    name = input(f"\nStudent #{i} Name: ")
    attendance = float(input(f"Enter attendance % for {name}: "))
    marks = float(input(f"Enter average exam marks % for {name}: "))

    if attendance >= 75:
        status = "Eligible"
    else:
        status = "Not Eligible (Low Attendance)"

    if marks >= 90: grade = "A+"
    elif marks >= 80: grade = "A"
    elif marks >= 70: grade = "B"
    elif marks >= 60: grade = "C"
    else: grade = "F"

    student_records.append((name, attendance, marks, grade, status))

print("\n" + "="*50)
print("              CLASS PERFORMANCE REPORT             ")
print("="*50)
for record in student_records:
    print(f"Name: {record[0]:12s} | Attendance: {record[1]}% | Marks: {record[2]}% | Grade: {record[3]} | Status: {record[4]}")
print("="*50)
