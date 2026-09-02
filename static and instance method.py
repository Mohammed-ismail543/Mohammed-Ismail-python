class Mobile:

    def __init__(self, brand, price):
        self.brand = brand
        self.price = price

    # Instance method
    def display(self):
        print("Mobile Brand:", self.brand)
        print("Price:", self.price)

    # Static method
    @staticmethod
    def operating_system():
        print("Operating System: Android")


m1 = Mobile("Oneplus", 25000)

m1.display()
Mobile.operating_system()