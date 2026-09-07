import json

def get_file_name(extension):
    while True:
        file_name = input(f"Enter {extension.upper()} file name: ").strip()

        if file_name == "":
            print("File name cannot be empty!")
        elif not file_name.endswith(extension):
            print(f"File name must end with {extension}")
        else:
            return file_name


def get_student_id():
    while True:
        value = input("Enter Student ID: ").strip()

        if value.isdigit() and int(value) > 0:
            return int(value)

        print("Invalid Student ID! Enter a positive number.")


def get_name():
    while True:
        name = input("Enter Student Name: ").strip()

        if name == "":
            print("Name cannot be empty!")
        elif len(name.replace(" ", "")) < 3:
            print("Name must contain at least 3 letters!")
        elif not name.replace(" ", "").isalpha():
            print("Name can contain only alphabets and spaces!")
        else:
            return name


def get_class():
    while True:
        class_name = input("Enter Class: ").strip()

        if class_name == "":
            print("Class cannot be empty!")

        else:
            return class_name


def get_subject_name(number):
    while True:
        subject = input(f"Enter Subject {number} Name: ").strip()

        if subject == "":
            print("Subject name cannot be empty!")

        elif not subject.replace(" ", "").isalpha():
            print("Subject name can contain only alphabets and spaces!")

        else:
            return subject


def get_marks(subject_name):
    while True:
        marks = input(f"Enter Marks for {subject_name}: ").strip()

        if marks.isdigit():

            marks = int(marks)

            if 0 <= marks <= 100:
                return marks

            print("Marks must be between 0 and 100!")

        else:
            print("Marks must be a number!")


def get_address():
    while True:
        address = input("Enter Address: ").strip()

        if address == "":
            print("Address cannot be empty!")

        else:
            return address


def get_city():
    while True:
        city = input("Enter City: ").strip()

        if city == "":
            print("City cannot be empty!")

        elif not city.replace(" ", "").isalpha():
            print("City can contain only alphabets and spaces!")

        else:
            return city


def get_school_name():
    while True:
        school_name = input("Enter School Name: ").strip()

        if school_name == "":
            print("School Name cannot be empty!")

        else:
            return school_name

def get_student_data():

    student = {}

    student["student_id"] = get_student_id()
    student["name"] = get_name()
    student["class"] = get_class()

    subjects = []

    for i in range(5):

        subject_name = get_subject_name(i + 1)
        marks = get_marks(subject_name)

        subjects.append({
            "subject": subject_name,
            "marks": marks
        })

    student["subjects"] = subjects

    student["address"] = get_address()
    student["city"] = get_city()
    student["school_name"] = get_school_name()

    return student

def create_json(student):

    file_name = get_file_name(".json")

    with open(file_name, "w") as file:
        json.dump(student, file, indent=4)

    print(f"JSON file created successfully: {file_name}")

def create_txt(student):

    file_name = get_file_name(".txt")

    with open(file_name, "w") as file:

        file.write(f"Student ID: {student['student_id']}\n")
        file.write(f"Name: {student['name']}\n")
        file.write(f"Class: {student['class']}\n")

        file.write("\nSubjects:\n")

        for subject in student["subjects"]:
            file.write(
                f"{subject['subject']}: {subject['marks']}\n"
            )

        file.write(f"\nAddress: {student['address']}\n")
        file.write(f"City: {student['city']}\n")
        file.write(f"School Name: {student['school_name']}\n")

    print(f"TXT file created successfully: {file_name}")

while True:

    print("\n==============================")
    print("        STUDENT FILE")
    print("==============================")

    print("1. Create JSON File")
    print("2. Create TXT File")
    print("3. Create JSON and TXT File")
    print("4. Exit")

    choice = input("Enter your choice: ").strip()

    if choice == "1":

        student = get_student_data()

        create_json(student)

    elif choice == "2":

        student = get_student_data()

        create_txt(student)

    elif choice == "3":

        print("\nEnter Student Details")

        student = get_student_data()

        print("\nEnter JSON File Details")
        create_json(student)

        print("\nEnter TXT File Details")
        create_txt(student)

        print("\nBoth JSON and TXT files created successfully!")


    elif choice == "4":

        print("\nProgram exited successfully.")
        break

    else:

        print("\nInvalid choice! Please select 1, 2, 3 or 4.")