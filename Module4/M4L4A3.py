# M4L4A3: Bye Bye
# Activity 3: Exception Handling - Retry Loop and Nested While Loop

valid = False
while not valid:  # Using nested while loop and retry logic
    try:
        n = int(input("Enter a number: "))
        # If an even number is entered, run loop printing bye
        while n % 2 == 0:
            print("bye")
            n = int(input("Enter an odd number to stop: "))
        valid = True
        print(f"Thank you! You entered odd number: {n}")
    except ValueError:
        print("Invalid")
