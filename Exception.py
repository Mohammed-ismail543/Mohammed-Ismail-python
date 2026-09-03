# Exception
try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    result = a / b

    print("Result:", result)

except ZeroDivisionError:
    print("Error: Cannot divide by zero")

except TypeError:
    print("Error: Invalid data type")

except ValueError:
    print("Error: Please enter numbers only")

finally:
    print("Program execution completed")