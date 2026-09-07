
students = []


# ---------- VALIDATION ----------

def validate_name(name):
    return len(name) >= 3 and name.replace(" ", "").isalpha()


def validate_id(student_id):
    return student_id.isdigit()


def validate_address(address):
    return address != "" and address.replace(" ", "").isalpha()


def validate_mobile(mobile):
    return mobile.isdigit() and len(mobile) == 10


def validate_password(password):
    upper = lower = digit = False

    for ch in password:
        if ch.isupper():
            upper = True
        elif ch.islower():
            lower = True
        elif ch.isdigit():
            digit = True

    return upper and lower and digit


# ---------- REGISTRATION ----------

def registration():

    print("\n================================")
    print("       STUDENT REGISTRATION")
    print("================================")

    # NAME
    while True:
        name = input("Enter Student Name: ")

        if validate_name(name):
            break

        print("Invalid Name!")
        print("Name must contain at least 3 letters.")

    # STUDENT ID
    while True:
        student_id = input("Enter Student ID: ")

        if validate_id(student_id):
            break

        print("Invalid ID!")
        print("Please enter numbers only.")

    # ADDRESS
    while True:
        address = input("Enter Your Address: ")

        if validate_address(address):
            break

        print("Invalid Address!")
        print("Please enter letters only.")

    # MOBILE
    while True:
        mobile = input("Enter Your Mobile Number: ")

        if validate_mobile(mobile):
            break

        print("Invalid Mobile Number!")
        print("Please enter exactly 10 digits.")

    # PASSWORD
    while True:
        password = input("Enter Password: ")

        if validate_password(password):
            break

        print("Invalid Password!")
        print("Password must contain uppercase, lowercase and number.")
        print("Example: Jayant123")

    # STORE STUDENT
    student = {
        "id": student_id,
        "name": name,
        "address": address,
        "mobile": mobile,
        "password": password
    }

    students.append(student)

    print("\n================================")
    print("     REGISTRATION SUCCESSFUL!")
    print("================================")
    print("New Student Added:", name)


# ---------- LOGIN ----------

def login():

    print("\n================================")
    print("          STUDENT LOGIN")
    print("================================")

    student_id = input("Enter Student ID: ")
    password = input("Enter Password: ")

    for student in students:

        if student["id"] == student_id and student["password"] == password:

            print("\n================================")
            print("       LOGIN SUCCESSFUL!")
            print("================================")
            print("Welcome", student["name"])

            return

    print("\nInvalid Student ID or Password!")


# ---------- DASHBOARD ----------

def student_dashboard():

    print("\n================================")
    print("       STUDENT DASHBOARD")
    print("================================")

    if not students:
        print("No Students Registered!")
        return

    print("Total Students:", len(students))

    for i, student in enumerate(students, 1):

        print("\nStudent", i)
        print("--------------------------------")
        print("ID      :", student["id"])
        print("Name    :", student["name"])
        print("Address :", student["address"])
        print("Mobile  :", student["mobile"])
        print("--------------------------------")


# ---------- DELETE STUDENT ----------

def delete_student():

    print("\n================================")
    print("        DELETE STUDENT")
    print("================================")

    student_id = input("Enter Student ID: ")

    for student in students:

        if student["id"] == student_id:

            students.remove(student)

            print("\n================================")
            print("    STUDENT DELETED SUCCESSFULLY!")
            print("================================")
            print("Deleted Student:", student["name"])

            return

    print("\nStudent ID Not Found!")


# ---------- MAIN MENU ----------

while True:

    print("\n================================")
    print("       STUDENT MANAGEMENT")
    print("================================")
    print("1. Registration")
    print("2. Login")
    print("3. Student Dashboard")
    print("4. Delete Student")
    print("5. Exit")
    print("================================")

    choice = input("Enter Your Choice: ")

    if choice == "1":
        registration()

    elif choice == "2":
        login()

    elif choice == "3":
        student_dashboard()

    elif choice == "4":
        delete_student()

    elif choice == "5":
        print("\n================================")
        print("          THANK YOU!")
        print("    EXITED SUCCESSFULLY")
        print("================================")
        break

    else:
        print("\nInvalid Choice!")
        print("Please select between 1 and 5.")