# M4L5A2: List & Dict Comprehensions
# Activity 2: List Comprehension and Dictionary Comprehension Examples

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# List Comprehension: Filter even numbers
even_numbers = [num for num in numbers if num % 2 == 0]
print("Even numbers (List Comprehension):", even_numbers)

# List Comprehension: Square numbers
squared_numbers = [num**2 for num in numbers]
print("Squared numbers:", squared_numbers)

# Dictionary Comprehension: Number -> Square mapping
square_dict = {num: num**2 for num in numbers if num <= 5}
print("Number-Square Dictionary:", square_dict)
