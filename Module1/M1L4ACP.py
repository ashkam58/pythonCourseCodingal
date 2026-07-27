# M1L4ACP: Custom Ride Selector / Age Check ACP
# After Class Project: Custom Ride Eligibility Checker

age = 14
height_cm = 150

print("Age:", age, "| Height:", height_cm, "cm")

if age >= 10:
    if height_cm >= 140:
        print("Eligible for the Rollercoaster Ride!")
    else:
        print("Eligible for the Junior Bumper Cars only.")
else:
    print("Eligible for Kiddie Train Ride only.")
