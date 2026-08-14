# M4L2A2: Cube of the Cube
# Activity 2: Function Chaining - Calling one function from inside another

# Define function to calculate cube
def cube(number):
    return number * number * number

# Define function to execute cube only if number is divisible by 3
def by_three(number):
    if number % 3 == 0:
        return cube(number)
    else:
        return False

# Display results
print("by_three(9):", by_three(9))
print("by_three(4):", by_three(4))
