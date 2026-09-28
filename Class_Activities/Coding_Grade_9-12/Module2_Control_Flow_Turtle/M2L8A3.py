# M2L8A3: Password Strength Validator
# Activity 3: Module 2 Capstone - Validating password complexity using loops & logic

password = input("Enter a password to test strength: ")

has_upper = any(c.isupper() for c in password)
has_lower = any(c.islower() for c in password)
has_digit = any(c.isdigit() for c in password)
has_length = len(password) >= 8

print("\n--- Password Strength Results ---")
print("Min 8 characters :", "PASS" if has_length else "FAIL")
print("Uppercase letter :", "PASS" if has_upper else "FAIL")
print("Lowercase letter :", "PASS" if has_lower else "FAIL")
print("Digit number     :", "PASS" if has_digit else "FAIL")

if has_length and has_upper and has_lower and has_digit:
    print("\nOverall Status: STRONG PASSWORD!")
else:
    print("\nOverall Status: WEAK PASSWORD. Please fulfill all criteria.")
