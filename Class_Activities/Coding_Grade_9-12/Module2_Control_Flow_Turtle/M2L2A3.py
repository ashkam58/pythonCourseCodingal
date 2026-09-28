# M2L2A3: Reverse Order Countdown
# Activity 3: Printing numbers in reverse order beginning from N down to 1

n = int(input("Enter the starting number (n > 1): "))

print(f"Numbers from {n} down to 1 are:")
for i in range(n, 0, -1):
    print(i)
