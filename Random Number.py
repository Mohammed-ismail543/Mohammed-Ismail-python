import random

print("RANDOM NUMBER PROGRAM")

# Random Integer
number = random.randint(1, 100)
print("Random Integer\n:", number)

# Random Float
decimal = random.random()
print("Random Float\n:", decimal)

# Random Choice
colors = ["Green", "Blue", "Red", "Yellow", "Black"]

print("Available Colors:")

for color in colors:
    print(color)

selected_color = random.choice(colors)

print("Randomly Selected Color\n:", selected_color)

# Random Shuffle
numbers = [1, 12, 3, 14, 5, 16, 7, 18, 9, 20]

print("Before Shuffle:")
print(numbers)

random.shuffle(numbers)

print("After Shuffle:")
print(numbers)

print("PROGRAM END")