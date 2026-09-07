users = {}


def signup():
    print("\n========== SIGNUP ==========")

    username = input("Enter Username: ").strip()
    password = input("Enter Password: ").strip()

    if username == "":
        print("Username cannot be empty!")
        return

    if password == "":
        print("Password cannot be empty!")
        return

    if username in users:
        print("Username already exists!")
        return

    users[username] = password

    print("Signup successful!")


def login():
    print("\n========== LOGIN ==========")

    username = input("Enter Username: ").strip()
    password = input("Enter Password: ").strip()

    if username in users and users[username] == password:
        print("Login successful!")
        return True

    print("Invalid username or password!")
    return False


def auth():
    while True:

        print("\n==============================")
        print("       AUTHENTICATION")
        print("==============================")
        print("1. Signup")
        print("2. Login")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            signup()

        elif choice == "2":
            if login():
                return True

        elif choice == "3":
            print("Program Exit.")
            return False

        else:
            print("Invalid choice!")