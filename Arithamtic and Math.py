a = 20
b = 6

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Floor Division:", a // b)
print("Modulus:", a % b)
print("Exponent:", a ** b)

print()

import math
radius=float(input("Enter radius of circle: "))
circumference=2*math.pi*radius
print(f" The Circumference is : { round(circumference ,2)}cm")

print()

import math
radius=float(input("Enter radius of circle: "))
area=math.pi*pow(radius,2)
print(f" The Area of the circle is : {round(area, 2)}cm^2")

print()

import math
X=float(input("Enter side X: "))
Y=float(input("Enter side Y: "))
c=math.sqrt(pow(X,2)+pow(Y,2))
print(f" side C={c}")