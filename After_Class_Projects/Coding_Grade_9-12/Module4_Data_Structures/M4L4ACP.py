# M4L4ACP: Basket Fruit Selector & Array Master
# After Class Project: Sets and Arrays

import array as arr

print("===== SETS AND ARRAYS MASTER =====")

# PART 1: Set Operations
set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}

print("\n--- Set Operations ---")
print("Set A:", set_a)
print("Set B:", set_b)

print("Intersection (Common elements):", set_a & set_b)
print("Union (All unique elements):", set_a | set_b)
print("Difference (Set A - Set B):", set_a - set_b)
print("Symmetric Difference:", set_a ^ set_b)

# PART 2: Array Operations
print("\n--- Array Operations ---")
arr_num = arr.array('i', [5, 12, 8, 12, 25, 30])
print("Original Array:", list(arr_num))

arr_num.append(40)
print("After appending 40:", list(arr_num))

arr_num.reverse()
print("Reversed Array:", list(arr_num))

print("Count of 12:", arr_num.count(12))

print("\n===== SUMMARY COMPLETE =====")
