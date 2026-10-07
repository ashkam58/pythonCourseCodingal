# M8L4A1: Constructor and Destructor
# Coding Grandmaster (Grades 9-12) - Module 8 Lesson 4 Activity 1

class Employee:
    # Initializing constructor
    def __init__(self, emp_name, emp_id):
        self.emp_name = emp_name
        self.emp_id = emp_id
        print(f"[+] Constructor called: Employee record for {self.emp_name} (ID: {self.emp_id}) created.")

    # Destructor
    def __del__(self):
        print(f"[-] Destructor called: Employee record for {self.emp_name} deleted from memory.")

    def show_profile(self):
        print(f"Profile: Name = {self.emp_name}, ID = {self.emp_id}")

# Creating and deleting employee objects
emp1 = Employee("Ashkam", 901)
emp1.show_profile()

print("Deleting emp1 manually using del...")
del emp1
