#To check whether a person is senior citizen or not
age = int(input("Enter your age: "))
if age >= 60:
    print("You are senior citizen")

elif age < 60:
    print("You are not senior citizen")

else:
    print("You must be 60+ to be a senior citizen")


print()

#Program to check students marks and Grade
print()

# Program to check students marks and Grade

Name = input("Enter your name: ")
Marks = int(input("Enter the students marks: "))

if Marks < 0 or Marks > 100:
    print("Invalid Marks")
else:
    if Marks >= 90:
        print("Grade: A")
        print("Excellent Performance")
    elif Marks >= 80:
        print("Grade: B")
        print("Very Good")
    elif Marks >= 60:
        print("Grade: C")
        print("Good")
    else:
        if Marks >= 35:
            print("Result: Pass")
        else:
            print("Result: Fail")

age = int(input("Enter your age: "))
license = input("Do you have a driving license? (yes/no): ")

if age >= 18 and license == "yes":
    print("You can drive.")

if age >= 18 or license == "yes":
    print("You satisfy at least one requirement.")

if not license == "yes":
                                                           
    print("You don't have a driving license.")

a = 10
b = 20

print(a > 5 and b > 15)
print(a > 15 or b > 15)
print(not(a > 15))