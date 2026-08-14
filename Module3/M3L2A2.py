# M3L2A2: Cube of the Cube
# Activity 2: Function Chaining - Calling one function from inside another

def cube(number):
    return number * number * number

def by_three(number):
    if number % 3 == 0:
        return cube(number)
    else:
        return False

print("by_three(9):", by_three(9))
print("by_three(4):", by_three(4))
