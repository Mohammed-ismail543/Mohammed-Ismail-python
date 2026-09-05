#Python Reading file(txt,json,csv)

file_path = "C:/Users/hp/Desktop/output.txt"
with open(file_path,"r") as file:
    content = file.read()
    print(content)