# M8L2A3: Set Union
# Coding Grandmaster (Grades 9-12) - Module 8 Lesson 2 Activity 3

# Two sets representing student clubs
coding_club = {"Ashkam", "Rohan", "Priya", "Ananya", "Arjun"}
robotics_club = {"Priya", "Arjun", "Kabir", "Meera", "Siddharth"}

print("Coding Club Members:", coding_club)
print("Robotics Club Members:", robotics_club)

# Set Union using the pipe operator (|)
all_members_pipe = coding_club | robotics_club
print("\nCombined Members using (|):", all_members_pipe)

# Set Union using union() method
all_members_method = coding_club.union(robotics_club)
print("Combined Members using .union():", all_members_method)

# Total unique students across both clubs
print(f"Total unique students enrolled: {len(all_members_method)}")
