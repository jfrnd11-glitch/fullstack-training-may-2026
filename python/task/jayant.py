import uuid
import json
data = []
def registration():

    print("====================")
    print("    REGISTRATION")
    print("====================")

    student_id = uuid.uuid4().int % 900000 + 100000
    name = input("Enter student name: ")
    age = int(input("Enter student age: "))
    mobile = input("Enter mobile number: ")
    email = input("Enter email: ")
    address = input("Enter address: ")
    pincode = input("Enter pincode: ")

    student = {
        "id": student_id,
        "name": name,
        "age": age,
        "mobile": mobile,
        "email": email,
        "address": address,
        "pincode": pincode
    }

    data.append(student)
    with open("student.json", "w") as file:
        json.dump(data, file, indent=4)
    print("Registration successful!")
    print("Student ID:", student_id)

def update():

    print("====================")
    print("       UPDATE")
    print("====================")

    student_id = int(input("Enter Student ID: "))
    for student in data:
        if student["id"] == student_id:
            print("\n1. Name")
            print("2. Age")
            print("3. Mobile")
            print("4. Email")
            print("5. Address")
            print("6. Pincode")

            choice = input("What do you want to update: ")
            if choice == "1":
                student["name"] = input("Enter new name: ")
            elif choice == "2":
                student["age"] = int(input("Enter new age: "))
            elif choice == "3":
                student["mobile"] = input("Enter new mobile: ")
            elif choice == "4":
                student["email"] = input("Enter new email: ")
            elif choice == "5":
                student["address"] = input("Enter new address: ")
            elif choice == "6":
                student["pincode"] = input("Enter new pincode: ")
            else:
                print("Invalid choice")
                return
            with open("student.json", "w") as file:
                json.dump(data, file, indent=4)
            print("Update successful!")
            return
    print("Student ID not found.")

while True:
    print("\n====================")
    print(" STUDENT MANAGEMENT")
    print("====================")
    print("1. Registration")
    print("2. Update")
    print("3. Exit")

    choice = input("Enter choice: ")
    if choice == "1":
        registration()
    elif choice == "2":
        update()
    elif choice == "3":
        print("thank you")
        print("Exit")
        break
    else:
        print("Invalid choice")