# M1L6A3: Diamond Pattern / Mid Number Search
# Activity 3: Printing diamond patterns using nested loops

n = 5

# Upper half
for i in range(1, n + 1):
    print(" " * (n - i) + "* " * i)

# Lower half
for i in range(n - 1, 0, -1):
    print(" " * (n - i) + "* " * i)
