def calculate(a, b):
    addition = a + b
    subtraction = a - b
    multiplication = a * b

    return addition, subtraction, multiplication

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

add, sub, mul = calculate(num1, num2)

print("Addition:", add)
print("Subtraction:", sub)
print("Multiplication:", mul)