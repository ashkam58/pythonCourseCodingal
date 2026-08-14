# M3L3A2: Loop Control & Placeholders
# Activity 2: Demonstrating break, continue, and pass keywords

for i in range(1, 10):
    if i % 2 == 0:
        continue
    print(f"Odd number: {i}")

for i in range(1, 10):
    if i == 5:
        print("Reached 5! Breaking out of loop.")
        break
    print(f"Current count: {i}")

for i in range(1, 4):
    if i == 2:
        pass
    else:
        print(f"Processing item {i}")
