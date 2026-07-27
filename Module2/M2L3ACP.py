# M2L3ACP: Homework Completion Tracker
# After Class Project: While Loop Homework Tracker

total_homework = 4
original_count = total_homework
print(f"You have {original_count} homework tasks to finish today!\n")

completed_count = 0
task_num = 1

while task_num <= total_homework:
    if task_num == 1: subject = "Maths exercises"
    elif task_num == 2: subject = "Science lab report"
    elif task_num == 3: subject = "English essay"
    else: subject = "History reading"

    print(f"Task #{task_num}: {subject}")
    ans = input("Is this homework complete? (y/n): ").strip().lower()
    if ans == 'y':
        completed_count += 1
        print("Great effort! Homework finished.\n")
    else:
        print("Keep working on it!\n")
    task_num += 1

print(f"Homework Tracker Summary: Completed {completed_count} out of {original_count} tasks.")
