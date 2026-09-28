# M1L6A1: Character Frequency / Occurrences Counter
# Activity 1: Counting character occurrences in a string using nested iteration

text = "programming"
char_to_count = "g"
count = 0

for char in text:
    if char == char_to_count:
        count += 1

print(f"The character '{char_to_count}' appears {count} times in '{text}'.")
