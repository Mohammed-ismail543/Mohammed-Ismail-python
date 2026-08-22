student = {
    "name": "Ismail",
    "age": "21",
    "marks": ["85", "78", "90"]
}

# keys()
data = student.keys()

for k in data:
    print(k)

# values()
data = student.values()
for k in data:
    print(k)

# get()
print(student.get("name"))

# items()
data = student.items()

for k, v in data:
    print(f"{k}: {v}")