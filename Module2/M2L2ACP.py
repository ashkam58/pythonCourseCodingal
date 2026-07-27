# M2L2ACP: Power Calculator
# After Class Project: Calculating power of a number using loops

base = int(input("Enter base number: "))
exponent = int(input("Enter exponent power: "))

result = 1
for i in range(exponent):
    result *= base

print(f"{base} raised to the power of {exponent} is: {result}")
