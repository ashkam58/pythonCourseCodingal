# M2L8A1: Interactive Quiz Game
# Activity 1: Module 2 Capstone - Interactive Python Quiz with Score Counter

questions = [
    {"q": "What loop is used when the number of iterations is known?", "a": "for"},
    {"q": "Which keyword breaks out of a loop immediately?", "a": "break"},
    {"q": "What function is used to create sequence numbers in a for loop?", "a": "range"}
]

score = 0
print("=== PYTHON BASICS QUIZ ===\n")

for i, q in enumerate(questions, 1):
    ans = input(f"Q{i}: {q['q']} ").strip().lower()
    if ans == q['a']:
        print("Correct!\n")
        score += 1
    else:
        print(f"Incorrect. Correct answer was '{q['a']}'.\n")

print(f"Quiz Finished! Your Final Score: {score}/{len(questions)}")
