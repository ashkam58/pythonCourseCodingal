"""
Prompt Engineering - Lesson 6: Prompt-to-Project Showcase
After Class Project (ACP): Choice Board Showcase

Interactive Python terminal player supporting all 5 Choice Board game themes.
"""

import time
import random

def banner(title):
    print("\n" + "=" * 70)
    print(f"   🏆 {title.upper()} 🎮")
    print("=" * 70)

def play_traffic_dodge():
    banner("Theme B: Traffic Dodge Arcade")
    print("Goal: Dodge cones on the highway! Survive for 10 rounds with lives > 0.")
    print("Controls: 'a' (steer left), 'd' (steer right), Enter (stay in lane)\n")

    car_lane = 2
    lives = 3
    rounds = 10
    lanes = 5

    while rounds > 0 and lives > 0:
        cone_lane = random.randint(0, lanes - 1)

        print("\n" + "—" * 35)
        print(f"🚗 DODGES LEFT: {rounds} | LIVES: {'❤️' * lives}")
        print("—" * 35)

        road_hazard = ["·"] * lanes
        road_hazard[cone_lane] = "⚠️"
        print(f"Highway: {' '.join(road_hazard)}")

        road_car = ["·"] * lanes
        road_car[car_lane] = "🏎️"
        print(f"Car:     {' '.join(road_car)}")

        steer = input("\nSteer (a/d): ").strip().lower()
        if steer == 'a' and car_lane > 0:
            car_lane -= 1
        elif steer == 'd' and car_lane < lanes - 1:
            car_lane += 1

        if car_lane == cone_lane:
            lives -= 1
            print("💥 CRASH! You clipped a traffic cone! (-1 Life)")
        else:
            print("💨 Clean dodge! Speeding forward!")

        rounds -= 1
        time.sleep(0.3)

    print("\n" + "=" * 40)
    if lives > 0:
        print("🏆 YOU WIN! 🏁")
        print(f"You conquered the Traffic Dodge challenge with {lives} lives remaining!")
    else:
        print("💥 GAME OVER! Vehicle totaled!")
    print("=" * 40)

def play_treasure_door():
    banner("Theme E: Treasure Door Challenge")
    print("A locked stone portal stands before you in the castle.")
    print("Three antique keys lie on the pedestal:\n")
    print(" [A] 🔑 Golden Key")
    print(" [B] 🗝️ Silver Key")
    print(" [C] 🗝️ Copper Key\n")

    choice = input("Which key will you insert into the lock? (A, B, or C): ").strip().upper()

    time.sleep(0.5)
    if choice == "B":
        print("\n✨ *CLICK!* The silver key turns smoothly!")
        print("🚪 The massive stone door slowly grinds open...")
        print("💎 An ancient vault overflowing with glowing gold and gems is revealed!")
        print("🏆 YOU WIN! Treasure Unlocked! 🗝️✨")
    else:
        print("\n❌ *SKRRRCH!* The key jams and fails to turn.")
        print("🔒 The magical trap locks the chest forever!")
        print("💀 GAME OVER! Wrong key chosen.")

def main():
    while True:
        banner("Choice Board Showcase Menu")
        print("1. Play Theme B: Traffic Dodge")
        print("2. Play Theme E: Treasure Door")
        print("3. View Prompts for All 5 Themes")
        print("4. Exit")

        c = input("\nEnter choice (1-4): ").strip()
        if c == "1":
            play_traffic_dodge()
        elif c == "2":
            play_treasure_door()
        elif c == "3":
            banner("The 5 Choice Board Themes")
            print("Theme A: Fruit Catcher 🍎 (Move basket left/right to catch apples)")
            print("Theme B: Traffic Dodge 🏎️ (Steer car to dodge cones on highway)")
            print("Theme C: Coral Explorer 🤿 (Diver swims 4-way to collect pearls)")
            print("Theme D: Jungle Runner 🐒 (Monkey auto-runs and jumps over logs)")
            print("Theme E: Treasure Door 🚪 (Click the correct key to unlock castle door)")
        elif c == "4":
            print("\nCongratulations on becoming a certified Prompt Engineer! 🎓🚀\n")
            break
        else:
            print("Invalid selection.")
        input("\nPress Enter to return to menu...")

if __name__ == "__main__":
    main()
