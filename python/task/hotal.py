import json
import os
class table:
    def __init__(self, customer_name, table_id, table_size, table_seat, table_duration):
        self.customer_name = customer_name
        self.table_id = table_id
        self.table_size = table_size
        self.table_seat = table_seat
        self.table_duration = table_duration
class Dispay(table):
    def display(self):
        print("\n---------- Booking Details ----------")
        print("Customer Name  :", self.customer_name)
        print("Table ID       :", self.table_id)
        print("Table Size     :", self.table_size)
        print("Table Seat     :", self.table_seat)
        print("Table Duration :", self.table_duration)
        print("-------------------------------------")

tables = {
    "2 Seater": {
        "seat": 2,
        "ids": [
            "T01", "T02", "T03", "T04", "T05",
            "T06", "T07", "T08", "T09", "T10"
        ]
    },
    "4 Seater": {
        "seat": 4,
        "ids": [
            "T11", "T12", "T13", "T14", "T15",
            "T16", "T17", "T18", "T19", "T20"
        ]
    },
    "6 Seater": {
        "seat": 6,
        "ids": [
            "T21", "T22", "T23", "T24", "T25"
        ]
    }
}

FILE_NAME = "tabledata.json"
def load_data():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, "w") as file:
            json.dump([], file, indent=4)
        return []
    try:

        with open(FILE_NAME, "r") as file:
            return json.load(file)

    except json.JSONDecodeError:

        return []


def save_data(data):

    with open(FILE_NAME, "w") as file:
        json.dump(data, file, indent=4)


def show_availability(data):

    booked_ids = []

    for booking_data in data:
        booked_ids.append(booking_data["table_id"])

    print("\n--------- Table Availability ---------")

    for size in tables:

        total = len(tables[size]["ids"])

        booked = 0

        for table_id in tables[size]["ids"]:

            if table_id in booked_ids:
                booked += 1

        available = total - booked

        print(size, ":", available)

    print("--------------------------------------")


def booking():

    data = load_data()

    print("\n--------- New Customer Booking ---------")

    # Customer Name
    customer_name = input("Please enter customer name: ")

    if customer_name.strip() == "":
        print("Customer name cannot be empty!")
        return

    # Show availability
    show_availability(data)

    # Table Size
    print("\n1 = 2 Seater")
    print("2 = 4 Seater")
    print("3 = 6 Seater")

    choice = input("Please select table size: ")

    if choice == "1":

        table_size = "2 Seater"

    elif choice == "2":

        table_size = "4 Seater"

    elif choice == "3":

        table_size = "6 Seater"

    else:

        print("Invalid choice!")
        return

    # Already booked IDs
    booked_ids = []

    for booking_data in data:
        booked_ids.append(booking_data["table_id"])

    # Find available tables
    available_tables = []

    for table_id in tables[table_size]["ids"]:

        if table_id not in booked_ids:
            available_tables.append(table_id)

    # Check availability
    if len(available_tables) == 0:

        print("\nSorry!")
        print("No", table_size, "table available.")

        return

    # Automatically assign first available table
    table_id = available_tables[0]

    table_seat = tables[table_size]["seat"]

    print("\nYour Table ID :", table_id)
    print("Table Size    :", table_size)
    print("Table Seat    :", table_seat)

    # Duration
    table_duration = input("Please enter table duration: ")

    # Create Object
    obj = Dispay(
        customer_name,
        table_id,
        table_size,
        table_seat,
        table_duration
    )

    # JSON Data
    booking_data = {
        "customer_name": customer_name,
        "table_id": table_id,
        "table_size": table_size,
        "table_seat": table_seat,
        "table_duration": table_duration
    }

    # Save booking
    data.append(booking_data)

    save_data(data)

    print("\n---------- Booking Successful ----------")
    print("Customer Name  :", customer_name)
    print("Table ID       :", table_id)
    print("Table Size     :", table_size)
    print("Table Seat     :", table_seat)
    print("Table Duration :", table_duration)

    # Remaining table
    remaining = len(available_tables) - 1

    print("\nRemaining", table_size, ":", remaining)


def display_all_bookings():

    data = load_data()

    print("\n========== ALL BOOKINGS ==========")

    if len(data) == 0:

        print("No booking available.")

        return

    for i, booking_data in enumerate(data, start=1):

        print("\nBooking", i)
        print("--------------------------------")
        print("Customer Name  :", booking_data["customer_name"])
        print("Table ID       :", booking_data["table_id"])
        print("Table Size     :", booking_data["table_size"])
        print("Table Seat     :", booking_data["table_seat"])
        print("Table Duration :", booking_data["table_duration"])

    print("=================================")


def main():

    while True:

        print("\n\n========== RESTAURANT ==========")
        print("1 = New Customer Booking")
        print("2 = Display All Bookings")
        print("3 = Table Availability")
        print("4 = Exit")
        print("================================")

        choice = input("Please enter your choice: ")

        if choice == "1":

            booking()

        elif choice == "2":

            display_all_bookings()

        elif choice == "3":

            data = load_data()
            show_availability(data)

        elif choice == "4":

            print("\nThank you! Restaurant closed.")
            break

        else:

            print("\nInvalid choice!")


main()