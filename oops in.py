class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display(self):
        print("Name:", self.name)
        print("Salary:", self.salary)


e1 = Employee("Ismail", 25000)
e2 = Employee("Rahil", 30000)
e3 = Employee("Reyan", 28000)
e4 = Employee("Rehan", 35000)

e1.display()
e2.display()
e3.display()
e4.display()