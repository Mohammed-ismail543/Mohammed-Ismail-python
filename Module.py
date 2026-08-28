# module
import math
pi = 3.14159

def square(x):
    return x ** 2
def cube(x):
    return x ** 3
def circumference(x):
    return 2 * pi * x
radius = float(input("Enter radius: "))
result = circumference(radius)
print("square=",square(radius))
print("cube=",cube(radius))
print("circumference of the circle=",(radius))