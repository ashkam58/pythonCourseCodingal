# M2L2A2: Reverse a String
# Activity 2: Reversing a user-entered string using for loop

string = input("Please enter your string: ")
string2 = ""

for i in string:
    string2 = i + string2

print("\nThe Original String =", string)
print("The Reversed String =", string2)
