"""
Prompt Engineering - Lesson 3: Animations with Prompts
Interactive Animation Studio & Prompt Simulator

Features:
1. View prompts and Game Lab JavaScript code for all 3 activities + ACP.
2. Run live console animations (Rocket Launch, Penguin Gravity Jump, Bouncing Ball).
3. Evaluate and test animation prompts.
"""

import time
import os
import random

def clear():
    # Simple line break separator for cross-platform stability
    print("\n" * 2)

def banner(title):
    print("=" * 70)
    print(f"   🎬 {title.upper()} 🎬")
    print("=" * 70)

def animate_rocket():
    banner("Simulating Activity 1: Rocket Launch")
    print("Prompt: 'Write Game Lab code to make a rocket sprite move upward as if it's flying into space.'")
    print("Code: rocket.y = rocket.y - 2;\n")
    time.sleep(1)
    
    height = 8
    for y in range(height, -1, -1):
        lines = ["." * 20 for _ in range(height + 1)]
        if y >= 0:
            lines[y] = " " * 9 + "🚀" + " " * 9
        print("\n" * 3)
        print("\n".join(lines))
        print(f"Rocket Y: {350 - (height - y) * 40}px (Flying upward)")
        time.sleep(0.3)
    print("\n✨ Rocket reached outer space!")

def animate_penguin():
    banner("Simulating Activity 2: Penguin Gravity Jump")
    print("Refined Prompt: 'Extend the penguin code to add gravity so the penguin lands back down after jumping.'")
    print("Physics: velocityY += 0.5; penguin.y += velocityY;\n")
    time.sleep(1)
    
    y = 0.0
    vy = -6.0
    gravity = 0.8
    ground = 0.0
    
    trajectory = []
    while True:
        vy += gravity
        y += vy
        if y >= ground:
            y = ground
            trajectory.append(y)
            break
        trajectory.append(y)
        
    for current_y in trajectory:
        pos = int(abs(current_y))
        bar = [" "] * 10
        idx = min(pos, 9)
        bar[9 - idx] = "🐧"
        print("\n" + "\n".join(bar))
        print("—" * 20 + " ❄️ Ice Floor")
        print(f"Position: {pos} units above ground")
        time.sleep(0.2)
    print("✨ Penguin landed safely on the ice!")

def animate_bouncing_ball():
    banner("Simulating ACP: Bouncing Ball")
    print("Prompt: 'Extend the ball code so it bounces back when it hits the left or right edge of the screen.'")
    print("Physics: if (ball.x > 400 || ball.x < 0) velocityX = -velocityX;\n")
    time.sleep(1)
    
    width = 25
    pos = 0
    vx = 2
    
    for frame in range(26):
        pos += vx
        if pos >= width - 1 or pos <= 0:
            vx = -vx
        screen = ["-"] * width
        screen[max(0, min(pos, width - 1))] = "🏀"
        print(f"Frame {frame:02d}: |{''.join(screen)}| (vx={vx})")
        time.sleep(0.15)
    print("\n✨ Ball smoothly bounced off the walls!")

def main():
    while True:
        banner("Lesson 3: Animations with Prompts")
        print("1. [Activity 1] Rocket Builder (Upward Motion)")
        print("2. [Activity 2] Penguin Jumper (Jump & Gravity Simulation)")
        print("3. [Activity 3] Cat Chaser (Multi-Sprite Chase Behavior)")
        print("4. [ACP Project] Bouncing Ball (Velocity Reversal)")
        print("5. Run Rocket Launch Console Animation")
        print("6. Run Penguin Gravity Jump Console Animation")
        print("7. Run Bouncing Ball Console Animation")
        print("8. Exit")
        
        choice = input("\nEnter choice (1-8): ").strip()
        
        if choice == "1":
            banner("Activity 1: Rocket Builder")
            print("Prompt: 'Write Game Lab code to make a rocket sprite move upward as if it's flying into space.'")
            print("\nCode:")
            print("var rocket = createSprite(200, 350);\nrocket.setAnimation('rocket');\nfunction draw() {\n  background('black');\n  rocket.y = rocket.y - 2;\n  drawSprites();\n}")
        elif choice == "2":
            banner("Activity 2: Penguin Jumper")
            print("Part 1: 'Write Game Lab code where a penguin jumps when the spacebar is pressed.'")
            print("Part 2: 'Extend the penguin code to add gravity so the penguin lands back down after jumping.'")
            print("\nKey Logic:")
            print("if (keyDown('space') && penguin.y >= ground) velocityY = -10;")
            print("velocityY = velocityY + 0.5; // gravity")
            print("penguin.y = penguin.y + velocityY;")
        elif choice == "3":
            banner("Activity 3: Cat Chaser")
            print("Prompt: 'Write Game Lab code to make a cat follow the mouse pointer, and add an escaping mouse sprite.'")
            print("\nKey Logic:")
            print("cat.x = mouseX; cat.y = mouseY; // cat tracks mouse")
            print("mouse.x += randomNumber(-3, 3); mouse.y += randomNumber(-3, 3); // mouse escapes")
        elif choice == "4":
            banner("ACP: Bouncing Ball")
            print("Prompt: 'Extend the ball code so it bounces back when it hits the left or right edge of the screen.'")
            print("\nKey Logic:")
            print("ball.x = ball.x + velocityX;")
            print("if (ball.x > 400 || ball.x < 0) {\n  velocityX = -velocityX; // reverse direction\n}")
        elif choice == "5":
            animate_rocket()
        elif choice == "6":
            animate_penguin()
        elif choice == "7":
            animate_bouncing_ball()
        elif choice == "8":
            print("\nKeep animating with clear prompts! 🎬\n")
            break
        else:
            print("Invalid selection. Choose 1-8.")
            
        input("\nPress Enter to return to menu...")

if __name__ == "__main__":
    main()
