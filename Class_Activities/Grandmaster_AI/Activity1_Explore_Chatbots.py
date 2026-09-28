"""
Prompt Engineering - Lesson 1: Meet the World of Prompts
Activity 1: Explore Chatbots

This interactive Python script helps students explore how different AI chatbots
(ChatGPT, Gemini, Claude, Copilot) interpret and answer the same prompts.
"""

def print_header(title):
    print("\n" + "=" * 70)
    print(f"   🚀 {title.upper()} 🚀")
    print("=" * 70)

# Built-in sample responses collected from testing major chatbots
CHATBOT_DATABASE = {
    "space_fact": {
        "prompt": "Tell me a fun fact about space in 2 sentences.",
        "responses": {
            "ChatGPT": "Did you know there are more stars in the universe than grains of sand on Earth's beaches? 🌟 Some stars are so big they could fit millions of Earths inside them!",
            "Gemini": "Space is completely silent because sound cannot travel in a vacuum. 🌌 The hottest planet in our solar system isn't Mercury — it's Venus!",
            "Claude": "There's a giant cloud in space that smells like rum and contains enough alcohol to make 400 trillion trillion pints of beer. 🛸 Space can be fun and weird!",
            "Copilot": "The footprints left on the Moon by astronauts will stay there for millions of years. 🌕 That's because there's no wind or water to wash them away."
        }
    },
    "story": {
        "prompt": "Write a short story about a penguin who wants to be an astronaut.",
        "responses": {
            "ChatGPT": "Pip the penguin looked past the glaciers to the midnight stars. With a helmet made from a glass jar and a bottle rocket sled, he launched over the ice shelf, reaching into the aurora!",
            "Gemini": "Barnaby was an emperor penguin who studied astronomy instead of fishing. When a high-altitude weather balloon touched down, he strapped on his goggles and drifted into the stratosphere, waving at Earth below.",
            "Claude": "Flipper didn't want to swim with seals; he wanted to float in zero gravity. He trained by holding his breath underwater, proving flippers and spacesuits are practically made for each other.",
            "Copilot": "Pippin built a cardboard lunar module at the South Pole. With a countdown from his penguin colony, he slid down the steepest snowbank and dreamed among the constellations."
        }
    },
    "riddle": {
        "prompt": "Give me a riddle for kids with 3 answer choices.",
        "responses": {
            "ChatGPT": "Riddle: I have keys but no locks. I have space but no room. You can enter, but you can't go outside. What am I?\nA) A piano\nB) A keyboard\nC) A treasure chest\nAnswer: B) A keyboard",
            "Gemini": "Riddle: I have a tail and a head, but no body. What am I?\nA) A dog\nB) A coin\nC) A comet\nAnswer: B) A coin",
            "Claude": "Riddle: What gets wetter the more it dries?\nA) A cloud\nB) A towel\nC) A sponge\nAnswer: B) A towel",
            "Copilot": "Riddle: I am tall when I am young, and short when I am old. What am I?\nA) A tree\nB) A pencil\nC) A candle\nAnswer: C) A candle"
        }
    },
    "coding": {
        "prompt": "Write Game Lab code to make a rocket move upward.",
        "responses": {
            "ChatGPT": "var rocket = createSprite(200, 350);\nfunction draw() {\n  background('black');\n  if (keyDown('up')) {\n    rocket.y -= 3;\n  }\n  drawSprites();\n}",
            "Gemini": "var rocket = createSprite(200, 300);\nrocket.setAnimation('rocket');\nfunction draw() {\n  background('space');\n  rocket.velocityY = -2;\n  drawSprites();\n}",
            "Claude": "var rocket = createSprite(200, 380);\nfunction draw() {\n  background('navy');\n  if (keyDown('up')) {\n    rocket.y = rocket.y - 4;\n  }\n  drawSprites();\n}",
            "Copilot": "var rocket = createSprite(200, 350);\nfunction draw() {\n  background('midnightblue');\n  rocket.y = rocket.y - 2;\n  drawSprites();\n}"
        }
    }
}

def display_prompt_comparison(category_key):
    data = CHATBOT_DATABASE[category_key]
    print_header(f"Prompt Test: {category_key.replace('_', ' ').title()}")
    print(f"\n📝 PROMPT GIVEN:\n\"{data['prompt']}\"\n")
    print("-" * 70)
    
    for bot, response in data["responses"].items():
        print(f"\n🤖 [{bot.upper()}] Response:")
        print(f"{response}")
        print(f"   [Word count: {len(response.split())} words]")
    print("-" * 70)

def custom_prompt_tester():
    print_header("Test Your Own Prompt Experiment")
    user_prompt = input("\n👉 Enter your prompt: ").strip()
    if not user_prompt:
        print("Prompt cannot be empty! Returning to menu.")
        return

    print("\n🔍 PROMPT ANALYSIS:")
    words = user_prompt.split()
    print(f"- Total words: {len(words)}")
    
    # Simple rule-based prompt analysis for students
    has_constraint = any(word.isdigit() for word in words) or any(k in user_prompt.lower() for k in ["sentence", "words", "lines", "short", "bullet", "step"])
    has_polite = any(k in user_prompt.lower() for k in ["please", "can you", "tell me", "explain", "write"])
    
    print(f"- Specific constraints detected: {'✅ Yes' if has_constraint else '⚠️ None detected (Try adding limits like \"in 2 sentences\")'}")
    print(f"- Clear instruction verb detected: {'✅ Yes' if has_polite else '⚠️ Consider starting with \"Write\", \"Explain\", or \"Give me\"'}")
    
    print("\n💡 Now open your browser and test this exact prompt in:")
    print("   1. ChatGPT (https://chatgpt.com)")
    print("   2. Google Gemini (https://gemini.google.com)")
    print("   3. Anthropic Claude (https://claude.ai)")
    print("   4. Microsoft Copilot (https://copilot.microsoft.com)")

def compare_two_saved_responses():
    print_header("Side-by-Side Detective Comparison")
    bot1 = input("Enter first chatbot name (e.g., ChatGPT): ").strip() or "ChatGPT"
    ans1 = input(f"Paste answer from {bot1}: ").strip()
    
    bot2 = input("Enter second chatbot name (e.g., Gemini): ").strip() or "Gemini"
    ans2 = input(f"Paste answer from {bot2}: ").strip()
    
    print("\n" + "=" * 70)
    print(f"📊 COMPARISON REPORT: {bot1} vs {bot2}")
    print("=" * 70)
    print(f"\n[1] {bot1}: ({len(ans1.split())} words)")
    print(f"    \"{ans1}\"")
    print(f"\n[2] {bot2}: ({len(ans2.split())} words)")
    print(f"    \"{ans2}\"")
    
    print("\n🕵️ Detective Questions for Discussion:")
    print(" - Which answer was more concise?")
    print(" - Did both chatbots follow all rules of your prompt?")
    print(" - Which one had a more engaging or creative style?")

def main():
    while True:
        print_header("Meet the World of Prompts - Activity 1")
        print("1. View Space Fun Fact Comparison (ChatGPT, Gemini, Claude, Copilot)")
        print("2. View Penguin Astronaut Story Comparison")
        print("3. View Kids Riddle Comparison")
        print("4. View Game Lab Code Comparison")
        print("5. Analyze My Own Prompt")
        print("6. Compare Two Responses Side-by-Side")
        print("7. Exit")
        
        choice = input("\nSelect an option (1-7): ").strip()
        
        if choice == "1":
            display_prompt_comparison("space_fact")
        elif choice == "2":
            display_prompt_comparison("story")
        elif choice == "3":
            display_prompt_comparison("riddle")
        elif choice == "4":
            display_prompt_comparison("coding")
        elif choice == "5":
            custom_prompt_tester()
        elif choice == "6":
            compare_two_saved_responses()
        elif choice == "7":
            print("\n👋 Keep exploring prompts and happy learning!\n")
            break
        else:
            print("\n❌ Invalid selection. Please enter a number between 1 and 7.")
        
        input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()
