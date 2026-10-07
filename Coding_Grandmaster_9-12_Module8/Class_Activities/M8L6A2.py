# M8L6A2: Encapsulation Implementation (Private Members & Getters/Setters)
# Coding Grandmaster (Grades 9-12) - Module 8 Lesson 6 Activity 2

class BankAccount:
    def __init__(self, account_holder, initial_balance):
        self.account_holder = account_holder
        self.__balance = initial_balance # Private attribute (encapsulated)

    # Getter method
    def get_balance(self):
        return self.__balance

    # Deposit method
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"[+] Successfully deposited ${amount}. New Balance: ${self.__balance}")
        else:
            print("[!] Deposit amount must be positive.")

    # Withdraw method with protection
    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"[-] Successfully withdrew ${amount}. Remaining Balance: ${self.__balance}")
        else:
            print("[!] Insufficient balance or invalid withdrawal amount.")

account = BankAccount("Ashkam Anwar", 1000)
print("Account Holder:", account.account_holder)
print("Initial Balance via Getter:", account.get_balance())

account.deposit(500)
account.withdraw(200)

# Trying to access private variable directly
try:
    print(account.__balance)
except AttributeError as e:
    print("[Protected] Cannot access __balance directly due to encapsulation:", e)
