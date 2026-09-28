# M2L4A2: Character Frequency Counter
# Activity 2: Nested Loops - Outer loop iterates through text, inner counts occurrences

text = input("Enter a string: ")
checked = ""

print("\nCharacter Frequencies:")
for char in text:
    if char not in checked and char != " ":
        checked += char
        count = 0
        for c in text:
            if c == char:
                count += 1
        print(f"'{char}' : {count}")
