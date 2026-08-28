# Variable scope

name = " Mohammed Ismail"

# Global variable
def outer():
    age = 20

    # Enclosed variable
    def inner():
        marks = 90
        # Local variable

        print("Local:", marks)
        print("Enclosed:", age)
        print("Global:", name)
        print("Built-in:", len("Hello"))

    inner()

outer()