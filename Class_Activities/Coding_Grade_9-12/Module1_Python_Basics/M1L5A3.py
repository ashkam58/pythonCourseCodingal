# M1L5A3: Prime Number Checker / Power Calculation
# Activity 3: Checking if a given number is prime using loops

num = 29
is_prime = True

if num <= 1:
    is_prime = False
else:
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            is_prime = False
            break

if is_prime:
    print(num, "is a Prime Number.")
else:
    print(num, "is NOT a Prime Number.")
