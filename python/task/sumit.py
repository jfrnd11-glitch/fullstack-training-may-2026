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
txt_file_name = file_name.replace(".json", ".txt")

with open(txt_file_name, "w") as file:

    file.write("================================\n")
    file.write("        STUDENT DETAILS\n")
    file.write("================================\n\n")

    file.write(f"Student ID : {student['student_id']}\n")
    file.write(f"Name       : {student['name']}\n")
    file.write(f"Class      : {student['class']}\n\n")

    file.write("Subjects and Marks:\n")
    file.write("-------------------\n")

    for subject in student["subjects"]:
        file.write(
            f"Subject : {subject['subject']} | "
            f"Marks : {subject['marks']}\n"
        )

    file.write("\n")
    file.write(f"Address    : {student['address']}\n")
    file.write(f"City       : {student['city']}\n")
    file.write(f"School Name: {student['school_name']}\n")

print(f"Student data successfully saved in {txt_file_name}")

txt_file_name = file_name.replace("json.",".txt")
with open(txt_file_name,"w") as file:
    print(f" data successfully saved in {txt_file_name}")