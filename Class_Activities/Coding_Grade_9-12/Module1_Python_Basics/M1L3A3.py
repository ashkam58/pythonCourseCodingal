# M1L3A3: Percentage and Grade Calculator / BMI Calculator
# Activity 3: Calculating percentages and values using expressions

math_marks = 85
science_marks = 90
english_marks = 88
total_marks = math_marks + science_marks + english_marks

percentage = (total_marks / 300) * 100

print("Total Marks obtained:", total_marks, "/ 300")
print("Percentage:", round(percentage, 2), "%")

# BMI Calculator
weight_kg = 50
height_m = 1.6
bmi = weight_kg / (height_m ** 2)
print("BMI Value:", round(bmi, 2))
