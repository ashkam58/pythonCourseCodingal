# M1L4A3: Exam Eligibility Check / Nested If Statements
# Activity 3: Checking eligibility based on attendance and medical cause

attendance_percentage = 80
has_medical_cause = False

if attendance_percentage >= 75:
    print("Allowed to sit in exam based on attendance.")
else:
    if has_medical_cause:
        print("Attendance is low, but allowed due to medical cause.")
    else:
        print("Not allowed to sit in exam due to low attendance.")
