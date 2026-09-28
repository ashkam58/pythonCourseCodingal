"""
Prompt Engineering - Lesson 5: Game Building with Prompts
After Class Project (ACP): Fruit Basket Dash

Interactive Python terminal simulation for Fruit Basket Dash.
"""

import time
import random

def banner(title):
    print("\n" + "=" * 70)
    print(f"   🍎 {title.upper()} 🧺")
    print("=" * 70)

def play_fruit_game():
    banner("Fruit Basket Dash Terminal Arcade")
    print("Goal: Catch 5 apples before 15 seconds run out!")
    print("Controls:")
    print(" - 'a' + Enter: Move Left")
    print(" - 'd' + Enter: Move Right")
    print(" - Enter: Stay in place\n")

    basket_pos = 3
    score = 0
    time_left = 15
    width = 7

    while time_left > 0 and score < 5:
        fruit_pos = random.randint(0, width - 1)
        
        # HUD overlay
        print("\n" + "—" * 35)
        print(f"🍏 [HUD] APPLES: {score}/5  |  TIME: {time_left}s")
        print("—" * 35)

        # Falling Apple
        sky = ["·"] * width
        sky[fruit_pos] = "🍎"
        print(f"Sky:    {' '.join(sky)}")

        # Basket Position
        ground = ["·"] * width
        ground[basket_pos] = "🧺"
        print(f"Ground: {' '.join(ground)}")

        move = input("\nMove (a/d): ").strip().lower()
        if move == 'a' and basket_pos > 0:
            basket_pos -= 1
        elif move == 'd' and basket_pos < width - 1:
            basket_pos += 1

        if basket_pos == fruit_pos:
            score += 1
            print("✨ CAUGHT! Sweet apple in the basket! (+1 Score)")
        else:
            print("🍎 Splat! Apple missed.")

        time_left -= 1
        time.sleep(0.3)

    print("\n" + "=" * 40)
    if score >= 5:
        print("🎉 YOU WIN! 🍎")
        print(f"Champion Catcher! Final Score: {score}")
    else:
        print("💀 GAME OVER!")
        print(f"Time ran out! Final Score: {score} (Needed 5)")
    print("=" * 40)

def view_steps():
    banner("The 6 Prompt Steps for Fruit Basket Dash")
    steps = [
        ("Step 1: Sprites", "Write Game Lab code that creates background (sunshine_showers_1), basket (bowl_1), and fruit (apple_1_1, scaled 0.1)."),
        ("Step 2: Movement", "Make basket move left/right with arrow keys and constrain inside screen."),
        ("Step 3: Falling", "Make fruit fall (fruit.y += 5) and reset to top at random x when passing bottom."),
        ("Step 4: Catching", "Add score variable. Increment score when fruit touches basket and reset fruit."),
        ("Step 5: Timer", "Add 30s timer with World.frameCount % 30 === 0. Win if score >= 10, else Game Over."),
        ("Step 6: HUD", "Overlay top white rectangle bar with black score and time text.")
    ]
    for s, p in steps:
        print(f"\n👉 {s}:")
        print(f"   \"{p}\"")

def main():
    while True:
        banner("Fruit Basket Dash Studio")
        print("1. Play Interactive Terminal Game")
        print("2. View The 6 Prompt Steps")
        print("3. Exit")

        c = input("\nEnter choice (1-3): ").strip()
        if c == "1":
            play_fruit_game()
        elif c == "2":
            view_steps()
        elif c == "3":
            print("\nEnjoy game building with prompts! 🍎\n")
            break
        else:
            print("Invalid selection.")
        input("\nPress Enter to return to menu...")

if __name__ == "__main__":
    main()
