class Father:
    def house(self):
        print("Father has a house")

class Mother:
    def car(self):
        print("Mother has a car")

class Child(Father, Mother):
    def study(self):
        print("Child is studying")

c = Child()

c.house()
c.car()
c.study()