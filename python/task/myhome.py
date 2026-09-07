file_name = input("Enter TXT file name: ").strip()

if not file_name.endswith(".txt"):
    file_name += ".txt"

student_id = input("Enter Student ID: ")
name = input("Enter Student Name: ")
student_class = input("Enter Class: ")

subjects = []

for i in range(5):
    subject_name = input(f"Enter Subject {i + 1} Name: ")
    marks = int(input(f"Enter Marks for {subject_name}: "))

    subjects.append({
        "subject": subject_name,
        "marks": marks
    })

address = input("Enter Address: ")
city = input("Enter City: ")
school_name = input("Enter School Name: ")

with open(file_name, "w") as file:

    file.write("STUDENT DETAILS\n")
    file.write("====================\n")
    file.write(f"Student ID : {student_id}\n")
    file.write(f"Name       : {name}\n")
    file.write(f"Class      : {student_class}\n\n")

    file.write("SUBJECTS AND MARKS\n")
    file.write("====================\n")

    for subject in subjects:
        file.write(
            f"Subject : {subject['subject']}, "
            f"Marks : {subject['marks']}\n"
        )

    file.write("\n")
    file.write(f"Address     : {address}\n")
    file.write(f"City        : {city}\n")
    file.write(f"School Name : {school_name}\n")

print(f"\nStudent data successfully saved in {file_name}")