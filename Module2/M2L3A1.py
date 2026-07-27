# M2L3A1: My Chore Checklist Countdown
# Activity 1: While Loop - Countdown Checklist

total_chores = 4
original_count = total_chores
print(f"You have {original_count} chores to finish today!\n")

completed_count = 0
chore_num = 1

while chore_num <= total_chores:
    if chore_num == 1: next_chore = "Make your bed"
    elif chore_num == 2: next_chore = "Feed the pet"
    elif chore_num == 3: next_chore = "Take out the trash"
    else: next_chore = "Wash the dishes"

    print(f"Chore #{chore_num}: {next_chore}")
    ans = input("Did you complete this chore? (y/n): ").strip().lower()
    if ans == 'y':
        completed_count += 1
        print("Great job! Marked as completed.\n")
    else:
        print("Don't forget to complete it later!\n")
    chore_num += 1

print(f"Summary: Completed {completed_count} out of {original_count} chores.")
