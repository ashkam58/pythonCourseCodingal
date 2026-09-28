"""
Prompt Engineering - Lesson 4: Storytelling with Prompts
Activity 1: Space Rescue Story

Interactive Python Story Engine simulating the branching Space Rescue Story.
Students can play through the story, answer the riddle, and trigger different endings.
"""

import time
import sys

def banner(title):
    print("\n" + "=" * 75)
    print(f"   🚀 {title.upper()} 🌌")
    print("=" * 75)

def play_story():
    banner("Act 1: Launch Preparation on Earth")
    print("🌍 Scene: Earth at the bottom, Maya standing beside the launchpad.")
    print("🚀 Action: Rocket rolls from x=50 toward Maya at x=150...")
    for progress in range(1, 6):
        time.sleep(0.3)
        print(f"   ...rocket rolling [{progress * 20}%]")
    print("\nMaya: 'The rocket is fueled and ready! Let's go rescue the lost astronaut!'")
    time.sleep(1)

    banner("Act 2: Blast Off!")
    print("🔥 Engines ignite! Maya boards the rocket.")
    print("⬆️ Both the rocket and Maya soar upward through the atmosphere...")
    for altitude in [1000, 5000, 15000, 50000]:
        time.sleep(0.3)
        print(f"   Altitude: {altitude}m...")
    print("\n✨ Breakthrough! The blue sky fades to pitch black deep space.")
    time.sleep(1)

    banner("Act 3: Encounter in Deep Space")
    print("🌌 Background: Pitch black with twinkling distant stars.")
    print("👨‍🚀 A lone astronaut drifts into sensor range from x=400 toward x=250...")
    time.sleep(1)
    print("\nAstronaut (over radio): 'My emergency thruster is locked! You must input the override code!'")
    time.sleep(1)

    banner("Act 4: The Riddle Challenge")
    print("❓ SECURITY OVERRIDE RIDDLE:")
    print("   'I'm full of holes, but I can still hold water. What am I?'\n")
    print("   [A] Sponge")
    print("   [B] Bucket")
    print("   [C] Balloon")
    
    choice = input("\n👉 Enter your choice (A, B, or C): ").strip().upper()

    if choice == "A":
        banner("Act 5: SUCCESSFUL RESCUE! 🎉")
        print("✅ Maya transmits: 'Sponge!'")
        print("🔓 Overriding code accepted! The astronaut's safety clamp unlocks!")
        print("🤝 Maya grabs the astronaut's hand and pulls him safely into the cockpit.")
        print("🚀 Turning the ship around... Flying back toward Earth!")
        time.sleep(1)
        print("\n🌍 Background turns lightblue as they land on Earth.")
        print("🏆 MISSION COMPLETE! Everyone cheered their safe return! 🎊")
    elif choice in ["B", "C"]:
        banner("Act 5: RESCUE FAILED! ❌")
        selected = "Bucket" if choice == "B" else "Balloon"
        print(f"❌ Maya transmits: '{selected}'")
        print("⚠️ INCORRECT OVERRIDE CODE! Systems locked!")
        print("🚨 Background flashes WARNING RED!")
        print("🌌 The astronaut drifts farther into deep space: 'Nooooo...!'")
        print("😢 Mission Failed. Better luck next time, Space Cadet!")
    else:
        print("\nInvalid choice! The signal timed out.")

def view_game_lab_code():
    banner("Complete Code.org Game Lab JavaScript")
    print("""// Key Sprites
var rocket = createSprite(50, 350);
var astronaut = createSprite(400, 200); astronaut.visible = false;
var friends = createSprite(200, 300);
var earth = createSprite(200, 400);
var storyStep = 0;

function draw() {
  if (storyStep < 2) background('lightblue');
  else if (storyStep === 'fail') background('red');
  else { background('black'); drawStars(); }

  // State Machine logic (0 -> 1 -> 2 -> 'question' -> 3 -> 4 -> 5 or 'fail')
  drawSprites();
}""")

def main():
    while True:
        banner("Space Rescue Story - Menu")
        print("1. Play the Branching Interactive Story")
        print("2. View Game Lab JavaScript Code")
        print("3. Exit")
        
        c = input("\nEnter choice (1-3): ").strip()
        if c == "1":
            play_story()
        elif c == "2":
            view_game_lab_code()
        elif c == "3":
            print("\nSafe travels through the cosmos! 🚀\n")
            break
        else:
            print("Invalid selection.")
        input("\nPress Enter to return to menu...")

if __name__ == "__main__":
    main()
