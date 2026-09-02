# Ducking Typing Polymorphism

# Parent class
class Animal:
    def sound(self):
        print("Animal makes a sound")

# Duck Typing class
class Lion:
    def sound(self):
        print("Lion roars")

# Function for polymorphism
def make_sound(animal):
    animal.sound()

# Objects
lion = Lion()

# Polymorphism through Duck Typing
print("\nPolymorphism using Duck Typing:")
make_sound(lion)