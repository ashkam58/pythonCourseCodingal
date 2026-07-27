# M1L2A2: Typecasting
# Activity 2: Converting data from one type to another (Implicit & Explicit)

# Explicit Typecasting
age_str = "15"
age_int = int(age_str)
print("Converted String to Int:", age_int, "| Type:", type(age_int))

weight_float = 45.75
weight_int = int(weight_float)
print("Float to Int:", weight_int, "| Type:", type(weight_int))

# Implicit Typecasting
num_int = 10
num_float = 2.5
sum_val = num_int + num_float
print("Implicit Sum:", sum_val, "| Type:", type(sum_val))
