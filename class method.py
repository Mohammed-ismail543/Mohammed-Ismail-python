# Class Method

class Student:

    count = 0

    def __init__(self, name):
        self.name = name
        Student.count = Student.count + 1

    @classmethod
    def total_students(cls):
        print("Total Students:", cls.count)


s1 = Student("Rahul")
s2 = Student("Ali")
s3 = Student("Ahmed")

Student.total_students()