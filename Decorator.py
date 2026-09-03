# Decorator
def decorator(func):

    def wrapper():
        print("Hey, Amit!")
        print("Before function")
        func()
        print("After function")

    return wrapper

@decorator
def greet():
    print("Hello, Rahul!")

greet()