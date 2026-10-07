# M8L3A2: Class Student - II
# Coding Grandmaster (Grades 9-12) - Module 8 Lesson 3 Activity 2

class Student:
    def __init__(self, name, roll_number, marks_list):
        self.name = name
        self.roll_number = roll_number
        self.marks = marks_list

    def calculate_total(self):
        return sum(self.marks)

    def calculate_average(self):
        return sum(self.marks) / len(self.marks)

    def get_grade(self):
        avg = self.calculate_average()
        if avg >= 90:
            return "A+"
        elif avg >= 80:
            return "A"
        elif avg >= 70:
            return "B"
        else:
            return "C"

    def report_card(self):
        print("=" * 35)
        print(f" REPORT CARD FOR {self.name.upper()} ")
        print("=" * 35)
        print(f"Roll Number: {self.roll_number}")
        print(f"Marks: {self.marks}")
        print(f"Total Marks: {self.calculate_total()}")
        print(f"Average Percentage: {self.calculate_average():.2f}%")
        print(f"Final Grade: {self.get_grade()}")
        print("=" * 35)

s1 = Student("Ashkam Anwar", 21, [95, 92, 98, 89, 94])
s1.report_card()
