# M2L8A2: Number Guessing Game with Limited Attempts
# Activity 2: Module 2 Capstone - Guessing Game with Max Attempts

import random

target = random.randint(1, 50)
max_attempts = 5

print("=== NUMBER GUESSING GAME (1 - 50) ===")
print(f"You have {max_attempts} attempts to guess the secret number.\n")

won = False
for attempt in range(1, max_attempts + 1):
    guess = int(input(f"Attempt #{attempt}: Enter your guess: "))
    if guess == target:
        print(f"🎉 Winner! You guessed the number in {attempt} attempts.")
        won = True
        break
    elif guess < target:
        print("Hint: Go higher!\n")
    else:
        print("Hint: Go lower!\n")

if not won:
    print(f"Game Over! The secret number was {target}.")
