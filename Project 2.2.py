# Python writing files (.txt, .json, .csv)

import json
import csv

employees = [["Name", "Age", "Job"],
             ["Sam", 30, "Cook"],
             ["sahil", 37, "Unemployed"],
             ["karma", 27, "Scientist"]]

file_path = "C:/Users/hp/Desktop/output.csv"

try:
    with open(file_path, "w", newline="") as file:
        writer = csv.writer(file)
        for row in employees:
            writer.writerow(row)
        print(f"csv file '{file_path}' was created")
except FileExistsError:
    print("That file already exists!")