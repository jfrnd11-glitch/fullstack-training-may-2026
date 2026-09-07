# zoom/dashboard.py

from .metting import start_meeting
from .metting import end_meeting
from .schedule import schedule_meeting


def dashboard(user_id):

    while True:

        print("\n================================")
        print("          ZOOM DASHBOARD")
        print("================================")

        print("Logged in User ID:", user_id)

        print("\n1. Start Meeting")
        print("2. End Meeting")
        print("3. Schedule Meeting")
        print("4. Exit")

        choice = input("\nEnter your choice: ").strip()

        if choice == "1":

            start_meeting()

        elif choice == "2":

            end_meeting()

        elif choice == "3":

            schedule_meeting()

        elif choice == "4":

            print("\nThank you for using Zoom!")
            print("Exiting Dashboard...")
            break

        else:

            print("\nInvalid choice!")
            print("Please select 1, 2, 3 or 4.")