students = ["Jayant", "Sumit", "Rahul","golu","vishal",]


def registration():
    print("\n===== REGISTRATION =====")
    
    print("Registered Students:")
    for name in students:
        print(name)

    print("Registration Successful!")


def login():
    print("\n===== LOGIN =====")

    print("Students login:")
    for name in students:
        print(name)

    print("Login Successful!")


while True:
    print("\n===== MAIN MENU =====")
    print("1. Registration")
    print("2. Login")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        registration()

    elif choice == "2":
        login()

    elif choice == "3":
        print("Thank You!")
        break

    else:
        print("Invalid Choice!")