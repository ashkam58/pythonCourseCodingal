"""
Prompt Engineering - Lesson 6: Prompt-to-Project Showcase
Activity 1: Choose Your Own Game (Capstone Launcher)

Interactive Python Launcher for the Capstone Game Showcase.
Allows students to play simulated games, review prompt breakdowns, and choose themes.
"""

import random
import time

def banner(title):
    print("\n" + "=" * 70)
    print(f"   🚀 {title.upper()} 🎮")
    print("=" * 70)

def play_meteor_dodger():
    banner("Meteor Dodger Terminal Game")
    print("Mission: Dodge Meteors (☄️) and catch Stars (⭐)!")
    print("Controls: 'a' (left), 'd' (right), Enter (stay)\n")

    ship_x = 3
    stars = 0
    lives = 3
    rounds = 12
    width = 7

    while rounds > 0 and lives > 0 and stars < 5:
        meteor_x = random.randint(0, width - 1)
        star_x = random.randint(0, width - 1)
        while star_x == meteor_x:
            star_x = random.randint(0, width - 1)

        print("\n" + "—" * 35)
        print(f"🛰️ STARS: {stars}/5 | LIVES: {'❤️' * lives} | TIME: {rounds}s")
        print("—" * 35)

        sky = ["·"] * width
        sky[meteor_x] = "☄️"
        sky[star_x] = "⭐"
        print(f"Space:  {' '.join(sky)}")

        ground = ["·"] * width
        ground[ship_x] = "🚀"
        print(f"Ship:   {' '.join(ground)}")

        move = input("\nControl (a/d): ").strip().lower()
        if move == 'a' and ship_x > 0:
            ship_x -= 1
        elif move == 'd' and ship_x < width - 1:
            ship_x += 1

        if ship_x == meteor_x:
            lives -= 1
            print("💥 HIT! Meteor struck your shields! (-1 Life)")
        elif ship_x == star_x:
            stars += 1
            print("✨ COLLECTED! Star absorbed! (+1 Star)")
        else:
            print("🌌 Maneuver successful, drifting safely.")

        rounds -= 1
        time.sleep(0.3)

    print("\n" + "=" * 40)
    if stars >= 5 and lives > 0:
        print("🏆 MISSION SUCCESS! 🚀")
        print(f"Congratulations! Stars: {stars}, Remaining Lives: {lives}")
    else:
        print("💀 MISSION FAILED!")
        if lives <= 0:
            print("Your ship was destroyed by meteors!")
        else:
            print(f"Time ran out! Final Stars: {stars}/5")
    print("=" * 40)

def view_all_options():
    banner("The 7 Capstone Menu Themes")
    themes = [
        ("1. Meteor Dodger 🚀", "Spaceship avoids falling meteors and collects energy stars."),
        ("2. Jungle Escape 🐒", "Monkey jumps over rocks and logs to collect bananas."),
        ("3. Animal Rescue 🧺", "Basket catches falling pets with scoring and time limits."),
        ("4. Mystery Door Challenge 🚪", "Click the correct key to unlock the magical castle portal."),
        ("5. Race to the Finish 🏎️", "Racecar steers through city traffic to beat the timer."),
        ("6. Underwater Explorer 🤿", "Diver collects shiny pearls while avoiding sharks."),
        ("7. Sky Jumper ☁️", "Hero leaps across floating cloud platforms without falling.")
    ]
    for name, desc in themes:
        print(f"\n👉 {name}")
        print(f"   {desc}")

def main():
    while True:
        banner("Prompt-to-Project Showcase Studio")
        print("1. Play Meteor Dodger Terminal Arcade")
        print("2. Explore All 7 Capstone Project Themes")
        print("3. Exit")

        c = input("\nEnter choice (1-3): ").strip()
        if c == "1":
            play_meteor_dodger()
        elif c == "2":
            view_all_options()
        elif c == "3":
            print("\nCongratulations on completing the Prompt Engineering Course! 🎓\n")
            break
        else:
            print("Invalid selection.")
        input("\nPress Enter to return to menu...")

if __name__ == "__main__":
    main()
