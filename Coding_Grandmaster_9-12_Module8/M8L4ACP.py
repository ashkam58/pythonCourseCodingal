# M8L4ACP: Expression Class
# Coding Grandmaster (Grades 9-12) - Module 8 Lesson 4 After Class Project

class Expression:
    """Class to evaluate and represent mathematical expressions."""
    def __init__(self, num1, num2, num3):
        self.num1 = num1
        self.num2 = num2
        self.num3 = num3

    def addition(self):
        return self.num1 + self.num2 + self.num3

    def complex_expression(self):
        # Expression: (num1 * num2) + (num3 ** 2)
        return (self.num1 * self.num2) + (self.num3 ** 2)

    def display_results(self):
        print("=" * 40)
        print(f"Numbers: a = {self.num1}, b = {self.num2}, c = {self.num3}")
        print("=" * 40)
        print(f"Sum (a + b + c): {self.addition()}")
        print(f"Expression (a * b + c^2): {self.complex_expression()}")
        print("=" * 40)

if __name__ == "__main__":
    expr = Expression(4, 5, 3)
    expr.display_results()
