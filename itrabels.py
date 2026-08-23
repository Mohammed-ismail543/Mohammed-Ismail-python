# String iterable
name = "PYTHON"

print("String:")
for character in name:
    print(character)

# List iterable
fruits = ["Apple", "Banana", "Mango"]

print("\nList:")
for fruit in fruits:
    print(fruit)

# Tuple iterable
numbers = (10, 20, 30, 40)

print("\nTuple:")
for number in numbers:
    print(number)

# Dictionary iterable
student = {
    "Name": " Mohammed Ismail",
    "Age": 20,
    "Course": "CSE"
}

print("\nDictionary:")
for key, value in student.items():
    print(key, ":", value)