# Class Variable

class Student:
    College = "Ghousia College of Engineering"

    def __init__(self, name):
        self.name = name

        # Instance variable
s1 = Student("Reyan")
s2 = Student("Ismail")
s3 = Student("Isyan")

print(s1.name)
print(s1.College)

print(s2.name)
print(s2.College)

print(s3.name)
print(s3.College)