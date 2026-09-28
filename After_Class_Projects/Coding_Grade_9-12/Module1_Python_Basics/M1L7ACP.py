# M1L7ACP: Factorial Calculator ACP
# After Class Project: Calculating Factorial of a number using function

def find_factorial(n):
    if n < 0:
        return "Factorial does not exist for negative numbers"
    elif n == 0 or n == 1:
        return 1
    else:
        fact = 1
        for i in range(1, n + 1):
            fact *= i
        return fact

num = 5
print(f"The factorial of {num} is: {find_factorial(num)}")
