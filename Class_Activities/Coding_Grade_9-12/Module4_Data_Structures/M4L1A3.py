# M4L1A3: Play with Lists
# Activity 3: Calculating Sum, Average, Smallest, and Largest Elements in a List

L = [4, 5, 1, 2, 9, 7, 10, 8]
print("Original List :", L)

count = 0
for i in L:
    count += i

avg = count / len(L)

print("sum = ", count)
print("average = ", avg)

L.sort()

print("Smallest element is:", L[0])
print("Largest element is:", L[-1])
