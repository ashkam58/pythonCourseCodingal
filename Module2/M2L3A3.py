# M2L3A3: Infinite Loop with Break & Guessing Game
# Activity 3: While Loop - Infinite Loop until correct input is entered

import random

target = random.randint(1, 10)
print("Guess the secret number between 1 and 10!")

attempts = 0
while True:
    guess = int(input("Enter your guess: "))
    attempts += 1
    if guess == target:
        print(f"Congratulations! You guessed it in {attempts} attempts.")
        break
    elif guess < target:
        print("Too low! Try again.")
    else:
        print("Too high! Try again.")
