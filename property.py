# @Property
class Rectangle:

    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    @property
    def area(self):
        return self.length * self.breadth

r1 = Rectangle(10, 5)
r2 = Rectangle(25,10)

print("Area:", r1.area)
print("Area:", r2.area)