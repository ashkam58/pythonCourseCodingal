# M8L3ACP: Robot Introduction
# Coding Grandmaster (Grades 9-12) - Module 8 Lesson 3 After Class Project

class Robot:
    # Class attribute
    category = "Autonomous Intelligent Assistant"

    def __init__(self, name, model, battery_percentage):
        self.name = name
        self.model = model
        self.battery = battery_percentage

    def introduce(self):
        print("=" * 45)
        print(f" Greetings! I am {self.name} ")
        print(f" Model: {self.model}")
        print(f" Type: {Robot.category}")
        print(f" Battery Level: {self.battery}%")
        print("=" * 45)

    def perform_task(self, task_name, energy_cost):
        if self.battery >= energy_cost:
            self.battery -= energy_cost
            print(f" {self.name} completed: '{task_name}'. Battery remaining: {self.battery}%")
        else:
            print(f" [!] Insufficient battery to perform '{task_name}'. Please recharge!")

    def recharge(self):
        self.battery = 100
        print(f" {self.name} has been fully recharged to 100%!")

if __name__ == "__main__":
    bot1 = Robot("Nova-1", "NV-2026-AI", 85)
    bot1.introduce()
    bot1.perform_task("Scanning Codebase", 30)
    bot1.perform_task("Running Unit Tests", 40)
    bot1.perform_task("Deep Learning Training", 30)
    bot1.recharge()
