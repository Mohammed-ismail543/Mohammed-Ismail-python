# Collection of Tuple Operations

students = ("Rahul", "Arun", "Kiran", "Rahul", "Mohan", "Kiran")


print(students)

# len() - finds the number of elements
print("\nLength of tuple:")
print(len(students))

# index() - finds the position of an element
print("\nIndex of Kiran:")
print(students.index("Kiran"))

# count() - counts how many times an element occurs
print("\nNumber of times Rahul occurs:")
print(students.count("Rahul"))

print("\nNumber of times Kiran occurs:")
print(students.count("Kiran"))

# dir() - displays available methods and attributes
print("\nMethods and attributes of Tuple:")
print(dir(students))

# help() - displays documentation about tuple
print("\nHelp for Tuple:")
help(tuple)