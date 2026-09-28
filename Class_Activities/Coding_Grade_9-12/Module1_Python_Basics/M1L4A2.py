# M1L4A2: Greater Among Numbers / Elif Ladder
# Activity 2: Finding the greatest of three numbers

num1 = 45
num2 = 78
num3 = 32

if num1 >= num2 and num1 >= num3:
    greatest = num1
elif num2 >= num1 and num2 >= num3:
    greatest = num2
else:
    greatest = num3

print("The greatest number among", num1, ",", num2, ", and", num3, "is:", greatest)
