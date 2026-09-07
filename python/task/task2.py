import json
import os
import uuid

FILE_NAME = "students.json"
def load_data():
    if os.path.exists(FILE_NAME):
        try:
            with open(FILE_NAME, "r") as file:
                return json.load(file)

        except json.JSONDecodeError:
            return {}

    return {}

def save_data(students):
    with open(FILE_NAME, "w") as file:
        json.dump(students, file, indent=4)

def generate_user_id(students):

    while True:

        user_id = uuid.uuid4().int % 100000000000
        if user_id >= 10000000000:

            if str(user_id) not in students:
                return user_id

def valid_name(name):

    name_without_space = name.replace(" ", "")

    return (
        len(name_without_space) >= 3
        and name_without_space.isalpha()
    )

def valid_email(email):

    return "@" in email and "." in email

def registration(students):

    if len(students) >= 10:
        print("\nOnly 10 students can be registered.")
        return

    print("\n========== REGISTRATION ==========")

    user_id = generate_user_id(students)

    print("Generated User ID:", user_id)

    while True:

        name = input("Enter Name: ").strip()

        if valid_name(name):
            break

        print("Name must contain at least 3 letters.")

    while True:

        email = input("Enter Email: ").strip()

        if valid_email(email):
            break

        print("Invalid Email!")

    while True:

        address = input("Enter Address: ").strip()

        if address:
            break

        print("Address cannot be empty.")

    students[str(user_id)] = {

        "user_id": user_id,
        "name": name,
        "email": email,
        "address": address
    }

    save_data(students)

    print("\nRegistration Successful!")
    print("Your User ID:", user_id)

def search_user(students):

    print("\n========== SEARCH ==========")

    try:
        user_id = int(input("Enter User ID to search: "))

    except ValueError:
        print("User ID must be an integer.")
        return

    user = students.get(str(user_id))

    if user:

        print("\nUser Found!")
        print("User ID :", user["user_id"])
        print("Name    :", user["name"])
        print("Email   :", user["email"])
        print("Address :", user["address"])

    else:
        print("User not found.")

def update_user(students):

    print("\n========== UPDATE ==========")

    try:
        user_id = int(input("Enter User ID to update: "))

    except ValueError:
        print("User ID must be an integer.")
        return

    user = students.get(str(user_id))

    if not user:

        print("User not found.")
        return

    print("\nCurrent Details:")
    print("User ID :", user["user_id"])
    print("Name    :", user["name"])
    print("Email   :", user["email"])
    print("Address :", user["address"])

    print("\n1. Update Name")
    print("2. Update Email")
    print("3. Update Address")
    print("4. Cancel")

    choice = input("Enter your choice: ").strip()

    if choice == "1":

        while True:

            name = input("Enter New Name: ").strip()

            if valid_name(name):

                user["name"] = name
                break

            print("Invalid Name!")

    elif choice == "2":

        while True:

            email = input("Enter New Email: ").strip()

            if valid_email(email):

                user["email"] = email
                break

            print("Invalid Email!")

    elif choice == "3":

        address = input("Enter New Address: ").strip()

        if address:

            user["address"] = address

        else:

            print("Address cannot be empty.")
            return

    elif choice == "4":

        print("Update cancelled.")
        return

    else:

        print("Invalid choice.")
        return

    save_data(students)

    print("\nUser details updated successfully!")

def delete_user(students):

    print("\n========== DELETE ==========")

    try:
        user_id = int(input("Enter User ID to delete: "))

    except ValueError:
        print("User ID must be an integer.")
        return

    if str(user_id) not in students:

        print("User not found.")
        return

    print("\nUser Found:")
    print("User ID:", students[str(user_id)]["user_id"])
    print("Name:", students[str(user_id)]["name"])

    confirm = input(
        "Are you sure you want to delete? (yes/no): "
    ).strip().lower()

    if confirm == "yes":

        del students[str(user_id)]

        save_data(students)

        print("User deleted successfully.")

    elif confirm == "no":

        print("Delete cancelled.")

    else:

        print("Please enter yes or no.")

def display_users(students):

    print("\n========== ALL USERS ==========")

    if not students:

        print("No users registered.")
        return

    for user in students.values():

        print("------------------------------")
        print("User ID :", user["user_id"])
        print("Name    :", user["name"])
        print("Email   :", user["email"])
        print("Address :", user["address"])
def main():

    students = load_data()

    while True:

        print("\n================================")
        print("     STUDENT MANAGEMENT SYSTEM")
        print("================================")

        print("1. Registration")
        print("2. Search")
        print("3. Update")
        print("4. Delete")
        print("5. Display All Students")
        print("6. Exit")

        choice = input("\nEnter your choice: ").strip()

        if choice == "1":

            registration(students)

        elif choice == "2":

            search_user(students)

        elif choice == "3":

            update_user(students)

        elif choice == "4":

            delete_user(students)

        elif choice == "5":

            display_users(students)

        elif choice == "6":

            print("\nThank you!")
            print("Program exited.")
            break

        else:

            print("Invalid choice! Please select 1 to 6.")

if __name__ == "__main__":
    main()