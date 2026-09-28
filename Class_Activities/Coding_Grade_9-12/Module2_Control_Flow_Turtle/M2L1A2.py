# M2L1A2: Exam Eligibility & Medical Check
# Activity 2: Nested Conditional Statements - Attendance & Medical Permission

attendance = int(input("Enter student attendance percentage: "))

if attendance >= 75:
    print("Attendance criteria met (>= 75%). Student is eligible to sit for the exam.")
else:
    medical = input("Is there a valid medical certificate? (yes/no): ").strip().lower()
    if medical == "yes":
        print("Special permission granted due to medical certificate. Eligible for exam.")
    else:
        print("Attendance too low and no medical certificate. Student is NOT eligible.")
