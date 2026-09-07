import json
import os
print("\n==============================")
print("        STUDENT FILE")
print("==============================")
print("1. Create JSON File")
print("2. Create TXT File")
print("3. Exit")
choice = input("Enter your choice: ").strip()

if choice == "1":

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
        json.dump(student,file,indent=4)
        
    print(f"\nStudent data successfully saved in {file_name}")
elif choice == "2":

    file_name = input("Enter TXT file name: ").strip()

    if not file_name.endswith(".txt"):
        file_name += ".txt"
    student = {}

    student["student_id"] = int(input("Enter Student ID: "))
    student["name"] = input("Enter Student Name: ")
    student["class"] = input("Enter Class: ")

    subjects = []

    for i in range(5):
        subject_name = input(  f"Enter Subject {i + 1} Name: ")        
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
        file.write(f"Student ID: {student['student_id']}\n")
        file.write(f"Name: {student['name']}\n")
        file.write(f"Class: {student['class']}\n")
        
        file.write("\nSubjects:\n")
        for subject in student["subjects"]:

            file.write(f"{subject['subject']}: " f"{subject['marks']}\n")
        file.write(f"\nAddress: {student['address']}\n")
        file.write(f"City: {student['city']}\n")
        
        file.write(f"School Name: {student['school_name']}\n")
        
    print(f"\nStudent data successfully saved in {file_name}")

elif choice == "3":
    print("\nProgram exited successfully.")
else:
    print("\nInvalid choice! Please select 1, 2 or 3.")