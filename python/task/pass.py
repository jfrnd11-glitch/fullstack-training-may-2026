students = ["jayant", "sumit", "rahul","golu","vishal",]

def registration():
    print("\n===== STUDENT REGISTRATION =====")

    name = input("Enter Student Name: ")

    if not name.replace(" ", "").isalpha():
        print("Invalid Name! Sirf letters enter karein.")
        return

    if name in students:
        print("Student already registered!")

def login():
    print("\n===== STUDENT LOGIN =====")

    name = input("Enter Student Name: ")

    if name in students:
        print("\nLogin Successful!")
        print("Welcome", name)

        dashboard(name)
    else:
        print("Student not registered!")

def dashboard(name):
    print("\n================================")
    print("       STUDENT DASHBOARD")
    print("================================")

    print("Welcome:", name)

    print("\nRegistered Students:")

    for i in range(len(students)):
        print(i + 1, ".", students[i])

    print("================================")


def menu():
    while True:
        print("\n================================")
        print("       STUDENT MANAGEMENT")
        print("================================")
        print("1. Registration")
        print("2. Login")
        print("3. Exit")
        print("================================")

        choice = input("Enter your choice: ")

        if choice == "1":
            registration()

        elif choice == "2":
            login()

        elif choice == "3":
            print("\nThank You!")
            print("Program Exit.")
            break

        else:
            print("Invalid Choice!")


menu()