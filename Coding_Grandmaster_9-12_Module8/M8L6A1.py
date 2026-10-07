# M8L6A1: Polymorphism Implementation (Method Overriding)
# Coding Grandmaster (Grades 9-12) - Module 8 Lesson 6 Activity 1

class India:
    def capital(self):
        print("New Delhi is the capital of India.")

    def language(self):
        print("Hindi is the official language of India.")

    def currency(self):
        print("Indian Rupee (INR) is the currency of India.")

class USA:
    def capital(self):
        print("Washington, D.C. is the capital of USA.")

    def language(self):
        print("English is the primary language of USA.")

    def currency(self):
        print("United States Dollar (USD) is the currency of USA.")

# Demonstrating polymorphism using a common function
def describe_country(country_obj):
    country_obj.capital()
    country_obj.language()
    country_obj.currency()
    print("-" * 40)

obj_ind = India()
obj_usa = USA()

print("--- Country 1 Details ---")
describe_country(obj_ind)

print("--- Country 2 Details ---")
describe_country(obj_usa)
