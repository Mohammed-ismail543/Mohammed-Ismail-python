# Python writing files (.txt, .json, .csv)

import json

employee = {
    "name": "Sam",
    "age": 30,
    "job": "cook"
}

file_path = "C:/Users/hp/Desktop/output.jason"

try:
    with open(file_path, "w") as file:
        json.dump(employee, file, indent=4)
        print(f"json file '{file_path}' was created")
except FileExistsError:
    print("That file already exists!")