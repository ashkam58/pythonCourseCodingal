# M3L7A3: Weather Prediction
# Activity 3: Counting Sunny vs Rainy Days in a Weather Tuple

weather = (1, 0, 0, 0, 1, 1, 0)
sunny = 0
rainy = 0

for i in range(0, 7):
    if weather[i] == 0:
        rainy += 1
    else:
        sunny += 1

print(f"Sunny days: {sunny}, Rainy days: {rainy}")

if sunny > rainy:
    print("Good weather")
else:
    print("Bad weather")
