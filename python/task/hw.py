import json

file_name = input("Enter JSON file name: ").strip()

if not file_name.endswith(".json"):
    file_name += ".json" 

student = {}

student["student_id"] = int(input("Enter Student ID: "))
student["name"] = input("Enter Student Name: ")
student["class"] = input("Enter Class: ")

subjects = []

for i in range(5): 
    subject_name = input(f"Enter Subject {i + 1} Name: ")
    marks = int(input(f"Enter Marks for {subject_name}: "))
    
    subjects.append({
        "subject": subject_name,
        "marks": marks
    })

student["subjects"] = subjects

student["address"] = input("Enter Address: ")
student["city"] = input("Enter City: ")
student["school_name"] = input("Enter School Name: ")

with open(file_name, "w") as file:
    json.dump(student, file, indent=4)

print(f"\nStudent data successfully saved in {file_name}")
