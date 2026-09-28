# M2L3A2: Sum of Digits & Armstrong Checker
# Activity 2: While Loop - Extracting digits and checking Armstrong number

number = int(input("Enter a number to check Armstrong property: "))
temp = number
digits_sum = 0
num_digits = len(str(number))

while temp > 0:
    digit = temp % 10
    digits_sum += digit ** num_digits
    temp //= 10

if number == digits_sum:
    print(f"{number} is an Armstrong Number!")
else:
    print(f"{number} is NOT an Armstrong Number.")
