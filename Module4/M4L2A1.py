# M4L2A1: Tuple Operations
# Activity 1: Tuple Creation, Immutability, Concatenation (+ operator), Count & Slicing

tuplex = ("tuple", False, 3.2, 1)
print("Mixed Tuple:", tuplex)

tuplex = (4, 6, 2, 8, 3, 1)
print("Integer Tuple:", tuplex)

tuplex = tuplex + (9,)
print("After adding 9 using +:", tuplex)

tuple1 = (50, 10, 60, 70, 50)
print("Count of 50 in tuple1:", tuple1.count(50))

tuplex = (2, 4, 3, 5, 4, 6, 7, 8, 6, 1)
_slice = tuplex[3:5]
print("Slice [3:5]:", _slice)

_slice = tuplex[:6]
print("Slice [:6]:", _slice)
