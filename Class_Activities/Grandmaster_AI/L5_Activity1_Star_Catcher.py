"""
Prompt Engineering - Lesson 5: Game Building with Prompts
Activity 1: Star Catcher (From Words to Game)

Interactive Python Arcade Simulator for Star Catcher.
Allows students to play the game in the terminal, experience the mechanics,
and inspect the progressive prompt-to-code decomposition.
"""

import time
import random

def banner(title):
    print("\n" + "=" * 70)
    print(f"   🌟 {title.upper()} 🧺")
    print("=" * 70)

def play_arcade_game():
    banner("Star Catcher Terminal Arcade")
    print("Instructions:")
    print(" - Press 'a' + Enter to move basket LEFT")
    print(" - Press 'd' + Enter to move basket RIGHT")
    print(" - Press Enter to stay in place")
    print(" - Catch 5 stars to WIN before 15 rounds run out!\n")
    
    basket_x = 3
    score = 0
    rounds = 15
    grid_width = 7

    while rounds > 0 and score < 5:
        star_x = random.randint(0, grid_width - 1)
        
        # Display HUD
        print("\n" + "—" * 35)
        print(f"📊 [HUD] SCORE: {score}/5  |  TIME LEFT: {rounds}s")
        print("—" * 35)
        
        # Display Star Falling
        star_line = ["·"] * grid_width
        star_line[star_x] = "⭐"
        print(f"Sky:    {' '.join(star_line)}")
        
        # Display Basket
        basket_line = ["·"] * grid_width
        basket_line[basket_x] = "🧺"
        print(f"Ground: {' '.join(basket_line)}")
        
        # User input for movement
        move = input("\nMove ('a' = left, 'd' = right, Enter = stay): ").strip().lower()
        if move == 'a' and basket_x > 0:
            basket_x -= 1
        elif move == 'd' and basket_x < grid_width - 1:
            basket_x += 1
            
        # Catch check
        if basket_x == star_x:
            score += 1
            print("✨ CATCH! Star caught in the basket! (+1 Point)")
        else:
            print("💨 Missed! The star fell to the ground.")
            
        rounds -= 1
        time.sleep(0.3)
        
    print("\n" + "=" * 40)
    if score >= 5:
        print("🏆 YOU WIN! 🌟")
        print(f"Fantastic catching! Final Score: {score}")
    else:
        print("💀 GAME OVER!")
        print(f"Time ran out! Final Score: {score} (Needed 5)")
    print("=" * 40)

def view_prompt_chain():
    banner("The 6-Step Prompt Chain")
    steps = [
        ("Part 1: Sprites", "Write Game Lab code that creates a background sprite, basket at bottom, and falling star."),
        ("Part 2: Controls", "Make the basket move left with left arrow and right with right arrow."),
        ("Part 3: Physics", "Make the star fall (star.y += 5) and reset to the top at random x when y > 400."),
        ("Part 4: Scoring", "Add score variable. Increase score by 1 when star touches basket and reset star."),
        ("Part 5: Timer", "Add timer = 30. Decrement each second (World.frameCount % 30 === 0). End at 0."),
        ("Part 6: HUD", "Draw HUD rectangle and score/time text after drawSprites() so it overlays on top.")
    ]
    for name, prompt in steps:
        print(f"\n👉 {name}:")
        print(f"   \"{prompt}\"")

def main():
    while True:
        banner("Star Catcher Project Studio")
        print("1. Play Interactive Terminal Arcade Game")
        print("2. View The 6-Step Prompt Chain")
        print("3. Exit")
        
        c = input("\nEnter selection (1-3): ").strip()
        if c == "1":
            play_arcade_game()
        elif c == "2":
            view_prompt_chain()
        elif c == "3":
            print("\nKeep building games with prompts! 🚀\n")
            break
        else:
            print("Invalid selection.")
        input("\nPress Enter to return to menu...")

if __name__ == "__main__":
    main()
