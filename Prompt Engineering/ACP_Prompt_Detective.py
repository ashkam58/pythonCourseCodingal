"""
Prompt Engineering - Lesson 1: Meet the World of Prompts
After Class Project (ACP): Be a Prompt Detective

In this project, students act as AI detectives comparing how two chatbots
(e.g., ChatGPT and Gemini) answer the same prompts, experiment with prompt
refinement, and record their findings.
"""

import sys

def print_banner(text):
    print("\n" + "=" * 75)
    print(f"   🔍 CASE FILE: {text.upper()} 🕵️‍♂️")
    print("=" * 75)

class PromptDetectiveSession:
    def __init__(self):
        self.bot1_name = "ChatGPT"
        self.bot2_name = "Gemini"
        
        # Default sample dataset from detective experiments
        self.case_records = {
            "prompt_1": {
                "title": "Fun Fact Prompt",
                "prompt": "Tell me 3 fun facts about the Moon.",
                "bot1_response": "1. Drifting away: Moon moves 3.8 cm farther every year.\n2. Extreme temps: 250°F down to -208°F.\n3. Moonquakes: Caused by Earth's gravitational pull.",
                "bot2_response": "1. 1/6th gravity: A 60-lb kid weighs only 10 lbs on the moon!\n2. Preserved footprints: No wind or rain to erase Apollo tracks.\n3. Egg shape: The Moon is not a perfect sphere."
            },
            "prompt_2": {
                "title": "Story Prompt",
                "prompt": "Write a short, funny story about an alien visiting Earth for the first time.",
                "bot1_response": "Zog landed in a backyard and observed cats being fed tuna on velvet couches. He reported back that cats ruled the human race as supreme masters.",
                "bot2_response": "Gleep hid behind a fast-food drive-through and concluded humans worship a magic speaker box that converts paper rectangles into golden fries."
            },
            "prompt_3": {
                "title": "Riddle Prompt",
                "prompt": "Give me a riddle about space with 3 answer choices.",
                "bot1_response": "I control ocean tides and shine in the night without making my own light. What am I? (A) Sun (B) Moon (C) Comet. Answer: (B) Moon",
                "bot2_response": "I am a giant gas planet with rings that could float in water. What am I? (A) Jupiter (B) Saturn (C) Neptune. Answer: (B) Saturn"
            },
            "refinement": {
                "original_prompt": "Tell me 3 fun facts about the Moon.",
                "refined_prompt": "Tell me 3 fun facts about how astronauts lived and did daily activities on the Moon during the Apollo missions.",
                "original_summary": "Returned general astronomical data (gravity, temperature, distance).",
                "refined_summary": "Returned vivid human survival facts (bunny hopping in suits, moon dust smelling like gunpowder, rehydrating food packets)."
            }
        }
        
        self.reflection = (
            "Through this detective mission, I learned that AI chatbots are shaped by the exact wording of our prompts. "
            "When I used general prompts, both bots gave textbook answers, but when I refined the prompt to specify Apollo astronaut daily life, "
            "the answers became much more descriptive, engaging, and detailed. Different chatbots also have distinct personalities: "
            "ChatGPT was great at storytelling humor, while Gemini provided relatable practical comparisons."
        )

    def view_case_files(self):
        print_banner(f"Detective Interrogation Records: {self.bot1_name} vs {self.bot2_name}")
        for key in ["prompt_1", "prompt_2", "prompt_3"]:
            item = self.case_records[key]
            print(f"\n📂 [{item['title']}]")
            print(f"   Prompt: \"{item['prompt']}\"")
            print(f"\n   🤖 {self.bot1_name}:")
            print(f"      {item['bot1_response']}")
            print(f"\n   🤖 {self.bot2_name}:")
            print(f"      {item['bot2_response']}")
            print("-" * 75)

    def view_prompt_refinement(self):
        ref = self.case_records["refinement"]
        print_banner("Prompt Refinement Experiment")
        print("\n[Step 1: Original Vague Prompt]")
        print(f"   👉 \"{ref['original_prompt']}\"")
        print(f"   Outcome: {ref['original_summary']}")
        
        print("\n[Step 2: Refined Specific Prompt]")
        print(f"   👉 \"{ref['refined_prompt']}\"")
        print(f"   Outcome: {ref['refined_summary']}")
        
        print("\n💡 Detective Insight:")
        print("   Adding context (astronauts + daily activities + Apollo missions) drastically improved response relevance!")

    def record_own_case(self):
        print_banner("Interrogate Your Own Chatbots")
        b1 = input(f"Enter Name for Chatbot #1 [{self.bot1_name}]: ").strip()
        if b1: self.bot1_name = b1
        
        b2 = input(f"Enter Name for Chatbot #2 [{self.bot2_name}]: ").strip()
        if b2: self.bot2_name = b2
        
        print(f"\nInterrogating {self.bot1_name} and {self.bot2_name}...")
        prompt = input("\nEnter your investigation prompt: ").strip()
        if not prompt:
            print("Prompt cannot be empty.")
            return
            
        r1 = input(f"Paste {self.bot1_name}'s answer: ").strip()
        r2 = input(f"Paste {self.bot2_name}'s answer: ").strip()
        
        print("\n📊 Detective Comparison Analysis:")
        print(f"   - {self.bot1_name} Word Count: {len(r1.split())}")
        print(f"   - {self.bot2_name} Word Count: {len(r2.split())}")
        print("   - Difference in length: abs({}) words".format(len(r1.split()) - len(r2.split())))

    def view_reflection(self):
        print_banner("Prompt Detective Final Report & Reflection")
        print(f"\n📝 4-5 Sentence Reflection:\n\n\"{self.reflection}\"\n")

    def export_report(self):
        filename = "Detective_Report_Meet_The_World_Of_Prompts.txt"
        with open(filename, "w", encoding="utf-8") as f:
            f.write("PROMPT DETECTIVE FINAL REPORT\n")
            f.write("=" * 50 + "\n\n")
            f.write(f"Investigated Chatbots: {self.bot1_name} and {self.bot2_name}\n\n")
            for key in ["prompt_1", "prompt_2", "prompt_3"]:
                item = self.case_records[key]
                f.write(f"[{item['title']}]\nPrompt: {item['prompt']}\n")
                f.write(f"- {self.bot1_name}: {item['bot1_response']}\n")
                f.write(f"- {self.bot2_name}: {item['bot2_response']}\n\n")
            ref = self.case_records["refinement"]
            f.write("[Prompt Refinement]\n")
            f.write(f"Original: {ref['original_prompt']}\nRefined: {ref['refined_prompt']}\n\n")
            f.write(f"Student Reflection:\n{self.reflection}\n")
        print(f"\n✅ Report exported successfully to {filename}!")

def main():
    session = PromptDetectiveSession()
    while True:
        print_banner("Prompt Detective Menu")
        print("1. View The Three Prompt Test Comparisons")
        print("2. View Prompt Refinement Experiment (Original vs Refined)")
        print("3. Record Your Own Chatbot Investigation")
        print("4. Read 4-5 Sentence Learning Reflection")
        print("5. Export Detective Report (.txt)")
        print("6. Exit")
        
        choice = input("\nEnter choice (1-6): ").strip()
        if choice == "1":
            session.view_case_files()
        elif choice == "2":
            session.view_prompt_refinement()
        elif choice == "3":
            session.record_own_case()
        elif choice == "4":
            session.view_reflection()
        elif choice == "5":
            session.export_report()
        elif choice == "6":
            print("\nCase closed, Detective! Keep asking great questions. 🕵️\n")
            break
        else:
            print("\n❌ Invalid choice. Please choose 1-6.")
        
        input("\nPress Enter to return to menu...")

if __name__ == "__main__":
    main()
