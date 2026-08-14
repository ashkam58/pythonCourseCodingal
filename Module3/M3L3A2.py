# M3L3A2: Loop Control & Placeholders
# Activity 2: Demonstrating break, continue, and pass keywords in Python

print("--- 1. Continue Example (Skipping Even Numbers) ---")
for i in range(1, 10):
    if i % 2 == 0:
        continue  # Skip even numbers
    print(f"Odd number: {i}")

print("\n--- 2. Break Example (Stopping at 5) ---")
for i in range(1, 10):
    if i == 5:
        print("Reached 5! Breaking out of loop.")
        break  # Exit loop completely
    print(f"Current count: {i}")

print("\n--- 3. Pass Example (Placeholder) ---")
for i in range(1, 4):
    if i == 2:
        pass  # Placeholder - do nothing
    else:
        print(f"Processing item {i}")
