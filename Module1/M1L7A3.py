# M1L7A3: Variable Scope & Return Values
# Activity 3: Demonstrating local vs global scope and function returns

global_var = "I am Global"

def scope_demo():
    local_var = "I am Local"
    print("Inside function - Global:", global_var)
    print("Inside function - Local:", local_var)

scope_demo()
print("Outside function - Global:", global_var)
