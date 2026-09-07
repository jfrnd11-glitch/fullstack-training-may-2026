students=[]


def validate_name(name):
    if name == "":
        return False

    if not name.replace(" ", "").isalpha():
        return False

    return True
# AB HAMNE STUDENT ID KA VALIDATION LAGAYA AGAR STUDENT ID NUMBER ME HOGA TO SAHI HOGA 
def validation_id(student_id):
    if student_id.isdigit():
        return True
    return False
# AB HAMNE STUDENT KA ADDRESS KA VALIDATION LAGAYA HAI JAISME ADDRESS HAMNESA STRING ME RAHEGA
def validation_address(address):
    if address == "":
        return False
    return True
# AB HAM MOBILE NUMBER KA VALIDATION LAGAYENGE JISME NUMBER 10 DIGIT KA RAHEGA AUR STYRING NAHI RAHEGA
def vaslidation_mobile(mobile):
    if mobile.isdigit()and len(mobile) == 10:
        return True

    return False
# AB HAM PASSWORD KA VALIDATION BANAYENGE JISME UPPER LOWER AND DIGIT TINO CASE KA USE HUWA HAI
def validation_password(password):
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
# AB HAM REGISTRION FUNCTION BANAYE HAI 
def registrion():
    print("\n==========")
    print("STUDENT REGISTRION")
    print("==========")
# hamne heding print kiya hai
    while True:
        name = input("enter student name :")
        if validate_name(name):
            break
        else:
            print("invalid name!")
            print("please enter only alphabets letter.")
# AB HAMNE USER SE STUDENT KA NAME PUCHA HAI AGAR NAME ALPHABET ME NAHI HUWA TO HAMARA CODE INVALID HO JAYEGA
    while True:
        student_id = input("enter student id :")
        if  validation_id(student_id):
            id_exists = False

            for student in student_id:
                if student["id"] == student_id:
                    id_exists = True
                    break
            if id_exists:
                    print("student id already exists!")
            else:
                    break
        else: 
            
            print("invalid ID")
            print("please enter only number")
    while True:
        address = input("enter your address:")
        if validation_address(address):
            break
        else:
            print("address is invalid.")
# AB HAMNE USER SE ADDRESS LIYA HAI 
    while True:
        mobile = input("enter your mobile number :")
        if vaslidation_mobile(mobile):
            break
        else:
            print("inva;lid mobile number ")
            print("please enter 10 digit mobile number")
# AB HAMNE MOBILE NUMBER USER SE LIYA HAI JO 10 DIGIT KA HOGA ALPHABET ME NAHI HOGA 
    while True:

        password = input("Enter Password: ")

        if validation_password(password):
            break

        else:
            print("\nInvalid Password!")
            print("Password must contain:")
            print("- One uppercase letter")
            print("- One lowercase letter")
            print("- One number")
# AB HAMNE PASSWORD USER SE LIYA HAI ISME UPPER LOWER AND DIGIT CASE USE KIYA HAI 
    student = {
        "id": student_id,
        "name": name,
        "address": address,
        "mobile": mobile,
        "password": password

    }
    students. append(student)
    print("\n==========")
    print("Registrion successful")
    print("add new student:", name)
    print("=========")
# AB HAM LOGIN FUNCTION BANAYENGE 
def login():
    print("\n==========")
    print("STUDENT LOGIN")
    print("==========")
    if len(students) == 0:

        print("No student registered yet.")
        return

    student_id = input("Enter Student ID: ")

    password = input("Enter Password: ")

    login_success = False
# HAM AB SEARCH KARENGE KOUN STUDENT LOGIN HUWA HAI

    for student in students:

        if (
            str(student["id"]) == student_id
            and student["password"] == password
        ):

            print("\n================================")
            print("       LOGIN SUCCESSFUL!")
            print("================================")

            print("Welcome", student["name"])
            print("\n===== STUDENT DASHBOARD=====")
            print("id:   ", student["id"])
            print("name:   ", student["name"])
            print("address:   ", student["address"])
            print("mobile:   ", student["mobile"])

            login_success = True
            break
        # agar user galat id password dal kiya to login nahi hoga 
    if not login_success:
            print("\n invalid id and password")
def delete_student():
            print("\n================================")
            print("          DELETE STUDENT")
            print("================================")


            if len(students) == 0:
               print("No student available.")
               return
            
            student_id = input("Enter student id to Delete: ")
            for student in students:

             if str(student["id"]) == student_id:
               
               print("\nStudent Found!")
               print("Name:", student["name"])

            confirm = input("Are you sure? (yes/no): ")

            if confirm.lower() == "yes":

                students.remove(student)

                print("\nStudent Deleted Successfully!")
            else:

                print("\nDelete Cancelled.")

                return

                print("\nStudent ID not found")
def show_students():

    print("\n================================")
    print("       REGISTERED STUDENTS")
    print("================================")

    if len(students) == 0:

        print("No student registered yet.")
        return

    for student in students:

        print("\n----------------------------")

        print("ID      :", student["id"])
        print("Name    :", student["name"])
        print("Address :", student["address"])
        print("Mobile  :", student["mobile"])

    print("----------------------------")

while True:

    print("\n================================")
    print("       STUDENT MANAGEMENT")
    print("================================")

    print("1. Registration")
    print("2. Login")
    print("3. Exit")
    print("4. Delete")
    print("5. Show Students")

    print("================================")

    choice = input("Enter your choice: ")

    # -----------------------------
    # REGISTRATION
    # -----------------------------

    if choice == "1":

        registrion()

    elif choice == "2":

        login()
    elif choice == "3":

        print("\nThank You!")
        print(" Exit.")

        break

    elif choice == "4":
        delete_student()
    elif choice == "5":
        show_students()

    else:

        print("\nInvalid Choice!")
        print("Please enter 1, 2, 3, 4 or 5.")