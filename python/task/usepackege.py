from zoom.auth import registration, login
from zoom.dashboard import dashboard


def main():

    while True:

        print("\n==============================")
        print("            ZOOM")
        print("==============================")

        print("1. Registration")
        print("2. Login")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            registration()

        elif choice == "2":
            success, user_id = login()

            if success:
                dashboard(user_id)

        elif choice == "3":
            print("\nThank you for using Zoom!")
            print("Program closed.")
            break

        else:
            print("\nInvalid choice!")


if __name__ == "__main__":
    main()