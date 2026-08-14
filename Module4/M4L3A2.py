# M4L3A2: Check the Frequency
# Activity 2: Dictionaries - Counting frequency of a specific value in a dictionary

test_dict = {'Codingal': 2, 'is': 2, 'best': 2, 'for': 2, 'Coding': 1}
print("The original dictionary : " + str(test_dict))

K = 2
res = 0

for key in test_dict:
    if test_dict[key] == K:
        res = res + 1

print("Frequency of K is : " + str(res))
