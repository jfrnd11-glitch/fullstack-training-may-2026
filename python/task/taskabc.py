students = []

# SABSE PAHLE HAM VALIDATION FUNCTION LAGAYENGE

def validate_name(name):
    if name == "":
        return False

    if not name.replace(" ", "").isalpha():
        return False

    return True


def validate_id(student_id):
    if student_id.isdigit():
        return True
    

    return False


def validate_address(address):
    if address == "":
        return False

    if not address.replace(" ", "").isalpha():
        return False

    return True


def validate_mobile(mobile):
    if mobile.isdigit() and len(mobile) == 10:
        return True

    return False


def validate_password(password):
    upper = False
    lower = False
    digit = False

    for character in password:
        if character.isupper():
            upper = True
        elif character.islower():
            lower = True
        elif character.isdigit():
            digit = True

    if upper and lower and digit:
        return True

    return False

# REGISTRATION NAME SE FUNCTION BANAYA HAI

def registration():

    print("\n================================")
    print("       STUDENT REGISTRATION")
    print("================================")

    # -------- NAME --------
    while True:
        name = input("Enter Student Name: ")

        if validate_name(name):
            break
        else:
            print("\nInvalid Name!")
            print("Please enter only letters.")

    # -------- STUDENT ID --------
    while True:
        student_id = input("Enter Student ID: ")

        if validate_id(student_id):
            break
        else:
            print("\nInvalid ID!")
            print("Please enter only numbers.")

    # -------- ADDRESS --------
    while True:
        address = input("Enter Your Address: ")

        if validate_address(address):
            break
        else:
            print("\nInvalid Address!")
            print("please enter only letter .")

    # -------- MOBILE --------
    while True:
        mobile = input("Enter Your Mobile Number: ")

        if validate_mobile(mobile):
            break
        else:
            print("\nInvalid Mobile Number!")
            print("Please enter 10 digits number.")

    # -------- PASSWORD --------
    while True:
        password = input("Enter Password: ")

        if validate_password(password):
            break
        else:
            print("\nInvalid Password!")
            print("Password must contain:")
            print("example = Jayant123")

    # -------- STORE STUDENT --------
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
    print("new student added:", name)

# LOGIN NAME SE FUNCTION BANAYA HAI 

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

# STUDENT DASHBOARD NAME SE FUNCTION BANAYA HAI JISME STUDENT KA DETLSE STORE HOGI

def student_dashboard():

    print("\n================================")
    print("       STUDENT DASHBOARD")
    print("================================")

    if len(students) == 0:
        print("No Students Registered!")
        return

    print("Total Students:", len(students))

    for i in range(len(students)):

        print("\nStudent", i + 1)
        print("--------------------------------")
        print("ID      :", students[i]["id"])
        print("Name    :", students[i]["name"])
        print("Address :", students[i]["address"])
        print("Mobile  :", students[i]["mobile"])
        print("--------------------------------")

# DELETE STUDENT NAME SE EK FUNCTION BANAYA HAI JISME STUDENT KO HATA V SAKTE HAI

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

# MAIN MENU HAI

while True:

    print("\n================================")
    print("       STUDENT MANAGEMENT")
    print("================================")
    print("1. Registration")
    print("2. Login")
    print("3. Student Dashboard")
    print("4. Delete")
    print("5. Exit")
    print("================================")

    choice = input("Enter your choice: ")

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