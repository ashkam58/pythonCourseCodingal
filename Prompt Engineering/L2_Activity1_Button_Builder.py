"""
Prompt Engineering - Lesson 2: Clear Prompts, Clear Code
Activity 1: Button Builder (From Words to Code)

This Python script models the step-by-step prompt decomposition process:
Part 1: Background Prompt -> Code
Part 2: Shapes & Visuals Prompt -> Code
Part 3: Interactivity & Event Handling Prompt -> Full Working Code
"""

import time
import random

PROMPT_STAGES = {
    1: {
        "title": "Part 1: Set a Background",
        "prompt": (
            "You are a Code.org Game Lab assistant. Write only the JavaScript for Game Lab. "
            "Create a draw() loop and set the background to skyblue. No shapes yet."
        ),
        "explanation": "Establishes the base canvas loop and background color.",
        "js_code": """function draw() {
  background("skyblue");
}"""
    },
    2: {
        "title": "Part 2: Add Shapes & Button Visuals",
        "prompt": (
            "Extend the previous Code.org Game Lab code. Keep the skyblue background. "
            "Add a red circle at the top and a yellow rectangle at the bottom with the text 'Click Me'."
        ),
        "explanation": "Adds geometric elements (ellipse, rect) and typography with clear coordinates and colors.",
        "js_code": """function draw() {
  background("skyblue");
  
  // Red circle at top
  fill("red");
  ellipse(200, 80, 100, 100);
  
  // Button rectangle
  fill("yellow");
  rect(150, 350, 100, 40);
  
  // Button text
  fill("black");
  textSize(20);
  text("Click Me", 160, 375);
}"""
    },
    3: {
        "title": "Part 3: Add Interactivity (Click Changes Background Color)",
        "prompt": (
            "Extend the previous Code.org Game Lab code to add click interactivity. "
            "Create a hidden sprite centered at (200, 370) sized 100x40 to detect clicks (createSprite + mousePressedOver). "
            "Declare a global bgColor defaulting to 'skyblue'. In draw(), call background(bgColor) so the color persists. "
            "When the sprite is clicked, update bgColor to a new random color using rgb(randomNumber(0, 255), randomNumber(0, 255), randomNumber(0, 255)). "
            "Keep the red circle at the top and the button visuals and include drawSprites(). Return the full code."
        ),
        "explanation": "Introduces persistent state (variables), event handling (mousePressedOver), and random color generation.",
        "js_code": """// Hidden button sprite for click detection
var button = createSprite(200, 370, 100, 40);
button.visible = false;

// Persistent background color
var bgColor = "skyblue";

function draw() {
  background(bgColor);

  // Red circle at the top
  fill("red");
  ellipse(200, 80, 100, 100);

  // Yellow button visuals near the bottom
  fill("yellow");
  rect(150, 350, 100, 40);

  // Button label
  fill("black");
  textSize(20);
  text("Click Me", 160, 375);

  // Change background color once on click
  if (mousePressedOver(button)) {
    bgColor = rgb(randomNumber(0, 255), randomNumber(0, 255), randomNumber(0, 255));
  }

  // Draw (hidden) sprites to keep mousePressedOver working
  drawSprites();
}"""
    }
}

def print_banner(msg):
    print("\n" + "=" * 75)
    print(f"   ✨ {msg.upper()} ✨")
    print("=" * 75)

def display_stage(stage_num):
    data = PROMPT_STAGES[stage_num]
    print_banner(data["title"])
    print(f"\n💡 PURPOSE: {data['explanation']}\n")
    print("📝 PROMPT GIVEN TO CHATGPT:")
    print(f'"{data["prompt"]}"\n')
    print("💻 GENERATED CODE.ORG JAVASCRIPT:")
    print("-" * 50)
    print(data["js_code"])
    print("-" * 50)

def simulate_button_app():
    print_banner("Simulating Button Builder App in Console")
    bg_color = "skyblue"
    colors = ["salmon", "lightgreen", "coral", "mediumpurple", "gold", "cyan", "pink"]
    clicks = 0
    
    print("\n[Game Lab Canvas Ready (400x400)]")
    print("Top Element: Red Circle at (200, 80)")
    print("Bottom Element: Yellow Button ['Click Me'] at (150, 350)")
    print(f"Current Background: {bg_color}")
    
    while True:
        cmd = input("\nType 'click' to simulate clicking the button (or 'q' to quit): ").strip().lower()
        if cmd == "q":
            break
        elif cmd == "click":
            clicks += 1
            r = random.randint(0, 255)
            g = random.randint(0, 255)
            b = random.randint(0, 255)
            bg_color = f"rgb({r}, {g}, {b})"
            print(f"\n👆 Click #{clicks} Detected on [button]!")
            print(f"🎨 Background updated to: {bg_color}")
        else:
            print("Unknown command. Type 'click' or 'q'.")

def evaluate_custom_prompt():
    print_banner("Prompt Quality Evaluator")
    prompt = input("\nEnter your custom prompt for Game Lab: ").strip()
    if not prompt:
        return
        
    p_lower = prompt.lower()
    score = 0
    feedback = []
    
    # Check key technical criteria
    if "game lab" in p_lower or "code.org" in p_lower:
        score += 25
        feedback.append("✅ Specifies platform (Code.org Game Lab)")
    else:
        feedback.append("⚠️ Missing platform mention: Add 'For Code.org Game Lab'")
        
    if any(k in p_lower for k in ["draw()", "draw loop", "background", "loop"]):
        score += 25
        feedback.append("✅ Includes structure/loop requirements")
    else:
        feedback.append("⚠️ Specify the draw loop or background")
        
    if any(k in p_lower for k in ["circle", "ellipse", "rect", "button", "sprite"]):
        score += 25
        feedback.append("✅ Specifies shapes or visual elements")
    else:
        feedback.append("⚠️ Add specific shapes and coordinates (e.g., at (200, 80))")
        
    if any(k in p_lower for k in ["click", "when clicked", "mouse", "variable", "random"]):
        score += 25
        feedback.append("✅ Includes interactivity or state logic")
    else:
        feedback.append("ℹ️ Static design: Consider adding click interaction")
        
    print(f"\n📊 Prompt Rating: {score}/100")
    for f in feedback:
        print(f"   {f}")

def main():
    while True:
        print_banner("Clear Prompts, Clear Code - Activity 1")
        print("1. View Part 1: Background Prompt & Code")
        print("2. View Part 2: Shapes & Visuals Prompt & Code")
        print("3. View Part 3: Interactivity (Button Click) & Full Code")
        print("4. Walk Through All 3 Steps Sequentially")
        print("5. Run Console Simulation of the Interactive Button App")
        print("6. Evaluate Your Own Prompt Quality")
        print("7. Exit")
        
        choice = input("\nSelect option (1-7): ").strip()
        if choice in ["1", "2", "3"]:
            display_stage(int(choice))
        elif choice == "4":
            for s in [1, 2, 3]:
                display_stage(s)
                time.sleep(1)
        elif choice == "5":
            simulate_button_app()
        elif choice == "6":
            evaluate_custom_prompt()
        elif choice == "7":
            print("\nKeep writing clear, progressive prompts! 🚀\n")
            break
        else:
            print("\n❌ Invalid choice. Please choose 1-7.")
        
        input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()
