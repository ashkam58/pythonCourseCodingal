# M4L5A3: map() and zip() Functions
# Activity 3: Demonstrating map() with lambda and zip() pairing

names = ["Alice", "Bob", "Charlie"]
scores = [85, 92, 78]

# Using zip() to pair two lists together
paired_student_scores = list(zip(names, scores))
print("Paired Student Scores (zip):", paired_student_scores)

# Using map() to convert scores to percentage strings
percentage_scores = list(map(lambda score: f"{score}%", scores))
print("Formatted Scores (map):", percentage_scores)
