"""
Prompt Engineering - Lesson 4: Storytelling with Prompts
After Class Project (ACP): Sea Rescue Adventure

Interactive Python simulator for the Sea Rescue Adventure story.
"""

import time
import random

def banner(title):
    print("\n" + "=" * 70)
    print(f"   🌊 {title.upper()} 🐢")
    print("=" * 70)

def simulate_rescue():
    banner("Act 1: The Stranded Fish")
    print("🌊 Scene: Deep blue ocean. A pink fish is stranded high up near the surface (y=50).")
    print("🐢 The brave sea turtle at the bottom (y=350) spots the fish in danger!")
    time.sleep(1)
    
    print("\n🐢 Turtle begins swimming upward...")
    for y in range(350, 50, -60):
        time.sleep(0.3)
        print(f"   Turtle at y={y}px...")
    print("✨ TOUCHDOWN! Turtle touches the fish: [rescued = True]!")
    time.sleep(1)

    banner("Act 2: Escort to Safety")
    print("🐠 The fish climbs safely onto the turtle's back [fish.y = turtle.y - 40].")
    print("🐢 The turtle turns and swims downward toward the coral reef...")
    for y in range(90, 310, 50):
        time.sleep(0.3)
        print(f"   Descending with fish at y={y}px...")
    print("🪸 Reached the coral reef sanctuary [released = True]!")
    time.sleep(1)

    banner("Act 3: Free Ocean Swimming")
    vx = random.choice([-2, 2])
    vy = random.choice([-2, -1, 1, 2])
    print(f"🎉 The fish is released! Initial velocity: vx={vx}, vy={vy}")
    print("🐠 The fish happily darts across the coral reef, bouncing safely off walls!")
    
    fx, fy = 200, 300
    for frame in range(6):
        time.sleep(0.3)
        fx += vx * 10
        fy += vy * 10
        print(f"   Fish swimming at ({fx}, {fy})...")
    print("\n✨ Mission Complete! The ocean ecosystem is thriving!")

def view_code():
    banner("Game Lab Code Snippet")
    print("""// State transition inside draw()
if (!rescued) {
  turtle.y -= 2;
  if (turtle.isTouching(fish)) rescued = true;
} else if (!released) {
  fish.x = turtle.x; fish.y = turtle.y - 40;
  turtle.y += 2;
  if (turtle.y >= 300) { released = true; vx = 2; vy = -2; }
} else {
  fish.x += vx; fish.y += vy;
  if (fish.x < 30 || fish.x > 370) vx = -vx;
  if (fish.y < 50 || fish.y > 350) vy = -vy;
}""")

def main():
    while True:
        banner("Sea Rescue Adventure Simulator")
        print("1. Run Story Simulation (Act 1 -> Act 2 -> Act 3)")
        print("2. View Game Lab JavaScript Code")
        print("3. Exit")
        
        c = input("\nEnter choice (1-3): ").strip()
        if c == "1":
            simulate_rescue()
        elif c == "2":
            view_code()
        elif c == "3":
            print("\nKeep coding great stories! 🌊\n")
            break
        else:
            print("Invalid selection.")
        input("\nPress Enter to return to menu...")

if __name__ == "__main__":
    main()
