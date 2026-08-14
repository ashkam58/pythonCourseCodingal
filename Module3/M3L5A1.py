# M3L5A1: Number Game
# Activity 1: Random Module - Generating random integer with randint()

import random  # Importing random module

playing = True  # Initialize loop control
number = str(random.randint(0, 9))  # Random in-built function

print("I will generate a number from 0 to 9, and you have to guess the number one digit at a time.")
print("The game ends when you get it right!")

# Iterate loop till the condition is true
while playing:
    guess = input("Give me your best guess! \n")
    if number == guess:
        print("You win the game!")
        print("The number was", number)
        break
    else:
        print("Your guess isn't quite right, try again. \n")
