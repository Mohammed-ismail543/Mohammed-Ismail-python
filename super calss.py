# SuperClass

class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def display(self):
        print("Brand:", self.brand)


class Car(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model

    def display(self):
        super().display()
        print("Model:", self.model)


c = Car("Toyota", "Fortuner")
c1 = Car("Maruti Suzuki", "Swift")
c2 = Car("Ford", "Mustang")
c3 = Car("Mahindra", "Thar")

c.display()
c1.display()
c2.display()
c3.display()