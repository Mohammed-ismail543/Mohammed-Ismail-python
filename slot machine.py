# Python Slot Machine
import random

symbols = ["🍒", "🍋", "⭐", "🔔"]

a = random.choice(symbols)
b = random.choice(symbols)
c = random.choice(symbols)

print(a, b, c)

if a == b == c:
    print("You Win!")
else:
    print("Try Again!")