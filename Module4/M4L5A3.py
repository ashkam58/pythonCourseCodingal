# M4L5A3: Mathematical Operations
# Activity 3: Math Module - ceil, floor, copysign, fabs, and gcd

import math  # Importing math module

# Using ceil and floor functions of math module
print('The Floor and Ceiling value of 23.56 are: ' + str(math.ceil(23.56)) + ', ' + str(math.floor(23.56)))

x = 10
y = -15
# Using copysign function
print('The value of x after copying the sign from y is: ' + str(math.copysign(x, y)))

# Using fabs and gcd functions
print('Absolute value of -96 and 56 are: ' + str(math.fabs(-96)) + ', ' + str(math.fabs(56)))

print('The GCD of 24 and 56 : ' + str(math.gcd(24, 56)))
