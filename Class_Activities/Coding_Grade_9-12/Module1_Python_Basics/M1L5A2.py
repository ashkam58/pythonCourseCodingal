# M1L5A2: Reverse String / Digits using While Loop
# Activity 2: Reversing numbers using while loop

number = 12345
original_number = number
reversed_num = 0

while number > 0:
    digit = number % 10
    reversed_num = (reversed_num * 10) + digit
    number //= 10

print("Original Number:", original_number)
print("Reversed Number:", reversed_num)
