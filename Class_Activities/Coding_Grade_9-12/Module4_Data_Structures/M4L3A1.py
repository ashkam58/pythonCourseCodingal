# M4L3A1: Get Rid of the Duplicates
# Activity 1: Dictionaries - Eliminating duplicate student records

student_data = {
    "id1": {"name": "Sara", "class": "V", "subject_integration": "english, math, science"},
    "id2": {"name": "David", "class": "V", "subject_integration": "english, math, science"},
    "id3": {"name": "Sara", "class": "V", "subject_integration": "english, math, science"},
    "id4": {"name": "Surya", "class": "V", "subject_integration": "english, math, science"},
}

result = {}
seen_keys = []

for student_id, details in student_data.items():
    unique_key = (details["name"], details["class"], details["subject_integration"])

    if unique_key not in seen_keys:
        seen_keys.append(unique_key)
        result[student_id] = details

print("Unique Student Records:")
for k, v in result.items():
    print(k, ":", v)
