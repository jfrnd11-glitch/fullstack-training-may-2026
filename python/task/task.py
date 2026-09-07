import json
import uuid
import os

FILE_NAME = "students.json"

def validate_name(name):
    name = name.strip()

    if len(name.replace(" ", "")) < 3:
        return False

    if not name.replace(" ", "").isalpha():
        return False

    return True

def validate_age(age):
    if not age.isdigit():
        return False

    age = int(age)

    if age < 1 or age > 100:
        return False

    return True

def validate_mobile(mobile):
    return mobile.isdigit() and len(mobile) == 10

def registration():

    students = {}

    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            students = json.load(file)

    print("\n==============================")
    print("       STUDENT REGISTRATION")
    print("==============================")

    while True:
        name = input("Enter Student Name: ").strip()

        if validate_name(name):
            break

        print("Invalid Name! Minimum 3 letters required.")

    while True:
        age = input("Enter Student Age: ").strip()

        if validate_age(age):
            break

        print("Invalid Age! Enter age between 1 and 100.")

    while True:
        course = input("Enter Course: ").strip()

        if course != "":
            break

        print("Course cannot be empty!")

    while True:
        mobile = input("Enter Mobile Number: ").strip()

        if validate_mobile(mobile):
            break

        print("Invalid Mobile! Enter exactly 10 digits.")

    while True:
        address = input("Enter Address: ").strip()

        if address != "":
            break

        print("Address cannot be empty!")

    student_id = int(uuid.uuid4())

    students[student_id] = {
        "student_id": student_id,
        "name": name,
        "age": int(age),
        "course": course,
        "mobile": mobile,
        "address": address
    }

    with open(FILE_NAME, "w") as file:
        json.dump(students, file, indent=4)

    print("\nRegistration Successful!")
    print("Student UUID:", student_id)

def update_student():

    if not os.path.exists(FILE_NAME):
        print("\nPlease register first!")
        return

    with open(FILE_NAME, "r") as file:
        students = json.load(file)

    print("\n==============================")
    print("        UPDATE STUDENT")
    print("==============================")

    student_id = input("Enter Student UUID: ").strip()

    if student_id not in students:
        print("\nInvalid UUID! Student not found.")
        return

    print("\nCurrent Student Details")
    print("------------------------------")
    print("Name    :", students[student_id]["name"])
    print("Age     :", students[student_id]["age"])
    print("Course  :", students[student_id]["course"])
    print("Mobile  :", students[student_id]["mobile"])
    print("Address :", students[student_id]["address"])

    print("\nEnter New Details")

    while True:
        name = input("Enter New Name: ").strip()

        if validate_name(name):
            break

        print("Invalid Name! Minimum 3 letters required.")

    while True:
        age = input("Enter New Age: ").strip()

        if validate_age(age):
            break

        print("Invalid Age! Enter age between 1 and 100.")

    while True:
        course = input("Enter New Course: ").strip()

        if course != "":
            break

        print("Course cannot be empty!")

    while True:
        mobile = input("Enter New Mobile Number: ").strip()

        if validate_mobile(mobile):
            break

        print("Invalid Mobile! Enter exactly 10 digits.")

    while True:
        address = input("Enter New Address: ").strip()

        if address != "":
            break

        print("Address cannot be empty!")

    students[student_id]["name"] = name
    students[student_id]["age"] = int(age)
    students[student_id]["course"] = course
    students[student_id]["mobile"] = mobile
    students[student_id]["address"] = address

    with open(FILE_NAME, "w") as file:
        json.dump(students, file, indent=4)

    print("\nStudent Details Updated Successfully!")

def main():

    while True:

        print("\n==============================")
        print("     STUDENT MANAGEMENT")
        print("==============================")
        print("1. Registration")
        print("2. Update Student")
        print("3. Exit")
        print("==============================")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            registration()

        elif choice == "2":
            update_student()

        elif choice == "3":
            print("\nThank You!")
            print("Program Closed.")
            break

        else:
            print("\nInvalid Choice! Please select 1, 2 or 3.")
            
if __name__ == "__main__":
    main()