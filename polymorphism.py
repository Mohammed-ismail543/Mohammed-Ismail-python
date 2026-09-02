# Polymorphism using Inheritance

# Parent class
class Animal:
    def sound(self):
        print("Animal makes a sound")

# Child class 1
class Dog(Animal):
    def sound(self):
        print("Dog barks")

# Child class 2
class Cow(Animal):
    def sound(self):
        print("Cow moos")

# Function for polymorphism
def make_sound(animal):
    animal.sound()

# Objects
dog = Dog()
cow = Cow()

# Polymorphism through Inheritance
print("Polymorphism using Inheritance:")
make_sound(dog)
make_sound(cow)