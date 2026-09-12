"""
Prompt Engineering - Lesson 2: Clear Prompts, Clear Code
After Class Project (ACP): Click-to-Color Circle

This interactive Python script provides:
1. Complete step-by-step prompts for ChatGPT -> Code.org Game Lab.
2. An interactive simulation of the magic Click-to-Color Circle.
3. A checklist & exporter for students to complete and submit their project.
"""

import random

ACP_STEPS = {
    1: {
        "step_name": "Step 1 — Make a Background",
        "prompt": "You are a Code.org Game Lab assistant. Write only the JavaScript for Game Lab. Create a draw() loop and set the background to skyblue. No shapes yet.",
        "code": """function draw() {
  background("skyblue");
}"""
    },
    2: {
        "step_name": "Step 2 — Add an Object (Circle)",
        "prompt": "Extend the previous Code.org Game Lab code. Keep the skyblue background. Add a red circle at the center using ellipse(200, 200, 100, 100). Return the full code.",
        "code": """function draw() {
  background("skyblue");
  // red circle at the center
  fill("red");
  ellipse(200, 200, 100, 100);
}"""
    },
    3: {
        "step_name": "Step 3 — Make the Object Change Color on Click",
        "prompt": "Extend the previous Code.org Game Lab code to make the circle change color when clicked. Create a global variable circleColor defaulting to 'red'. In draw(), call background(\"skyblue\"), then fill(circleColor) and draw ellipse(200, 200, 100, 100). Detect clicks using mouseWentDown() and check if the click is inside the circle with dist(mouseX, mouseY, 200, 200) < 50. When clicked, set circleColor = rgb(randomNumber(0, 255), randomNumber(0, 255), randomNumber(0, 255)). Return the full code.",
        "code": """var circleColor = "red";

function draw() {
  background("skyblue");
  fill(circleColor);
  noStroke();
  ellipse(200, 200, 100, 100);

  if (mouseWentDown("leftButton")) {
    if (dist(mouseX, mouseY, 200, 200) < 50) {
      circleColor = rgb(randomNumber(0, 255), randomNumber(0, 255), randomNumber(0, 255));
    }
  }
}"""
    }
}

def print_header(title):
    print("\n" + "=" * 70)
    print(f"   🔮 {title.upper()} 🔮")
    print("=" * 70)

def show_step(step_idx):
    item = ACP_STEPS[step_idx]
    print_header(item["step_name"])
    print("\n📝 PROMPT TO COPY INTO CHATGPT:")
    print("-" * 70)
    print(f'"{item["prompt"]}"')
    print("-" * 70)
    print("\n💻 EXPECTED JAVASCRIPT CODE OUTPUT:")
    print(item["code"])

def interactive_circle_simulator():
    print_header("Interactive Magic Circle Simulator")
    circle_color = "red"
    clicks = 0
    print("\n[Canvas 400x400 Ready]")
    print("Background: skyblue")
    print(f"Circle at center (200, 200) | Current Color: {circle_color}")
    
    while True:
        cmd = input("\nType 'click' to click the magic circle (or 'q' to return to menu): ").strip().lower()
        if cmd == "q":
            break
        elif cmd == "click":
            clicks += 1
            r = random.randint(0, 255)
            g = random.randint(0, 255)
            b = random.randint(0, 255)
            circle_color = f"rgb({r}, {g}, {b})"
            print(f"✨ Click #{clicks}: Magic circle absorbed energy!")
            print(f"🎨 Circle Color is now: {circle_color}")
        else:
            print("Unknown input. Type 'click' to simulate a mouse click or 'q' to quit.")

def submission_guide():
    print_header("ACP Project Submission Guide")
    print("1. Open Code.org Game Lab: https://studio.code.org/projects/gamelab/new")
    print("2. Paste your completed Step 3 JavaScript code.")
    print("3. Click 'Run' to test clicking the circle.")
    print("4. Click the 'Share' button in the top left.")
    print("5. Copy your project link.")
    print("6. Submit the link in your Codingal dashboard!")

def main():
    while True:
        print_header("ACP: Click-to-Color Circle Menu")
        print("1. View Step 1: Background Prompt & Code")
        print("2. View Step 2: Circle Shape Prompt & Code")
        print("3. View Step 3: Interactive Color-Change Prompt & Full Code")
        print("4. Run Console Interactive Circle Simulator")
        print("5. View Submission Guide & Checklist")
        print("6. Exit")
        
        choice = input("\nSelect option (1-6): ").strip()
        if choice in ["1", "2", "3"]:
            show_step(int(choice))
        elif choice == "4":
            interactive_circle_simulator()
        elif choice == "5":
            submission_guide()
        elif choice == "6":
            print("\nGreat job building interactive apps with prompts! 🚀\n")
            break
        else:
            print("Invalid option. Please enter 1 to 6.")
        
        input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()
