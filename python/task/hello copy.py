students = []

def registration():
    print("\n===== REGISTRATION =====")
    name = input("Enter Student Name: ")
    students.append(name)
    print("Registration Successful!")

def login():
    print("\n===== LOGIN =====")
    name = input("Enter Student Name: ")

    for i in range(len(students)):
        if name == students[i]:
            print("Login Successful!")
            print("Welcome", name)

            print("\nRegistered Students:")
            for j in range(len(students)):
                print(j + 1, ".", students[j])
            return

    print("Invalid Student Name!")

while True:
    print("\n===== STUDENT DASHBOARD =====")
    print("1. Registration")
    print("2. Login")
    print("3. Exit")

    choice = input("Enter Your Choice: ")

    if choice == "1":
        registration()

    elif choice == "2":
        if len(students) == 0:
            print("Please Register First!")
        else:
            login()

    elif choice == "3":
        print("Thank You!")
        break

    else:
        print("Invalid Choice!")