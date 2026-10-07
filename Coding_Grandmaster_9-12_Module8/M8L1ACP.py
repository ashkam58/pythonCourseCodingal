# M8L1ACP: Number Guessing Game
# Coding Grandmaster (Grades 9-12) - Module 8 Lesson 1 After Class Project
import random

def play_number_guessing_game():
    secret_number = random.randint(1, 50)
    attempts = 0
    max_attempts = 7
    guess_history = []

    print("=" * 45)
    print(" Welcome to the Number Guessing Challenge! ")
    print("=" * 45)
    print("I have picked a secret number between 1 and 50.")
    print(f"You have {max_attempts} attempts to guess it.\n")

    # Simulation demonstration
    simulated_guesses = [25, 37, 42, secret_number]
    for guess in simulated_guesses:
        attempts += 1
        guess_history.append(guess)
        print(f"Attempt #{attempts}: Guessed {guess}")
        
        if guess < secret_number:
            print(" -> Too Low! Try a higher number.")
        elif guess > secret_number:
            print(" -> Too High! Try a lower number.")
        else:
            print(f"\n [SUCCESS] Congratulations! You found {secret_number} in {attempts} attempts!")
            break

    print("\nYour Guess History (List Data Structure):", guess_history)
    print("Total Guesses Made:", len(guess_history))

if __name__ == "__main__":
    play_number_guessing_game()
