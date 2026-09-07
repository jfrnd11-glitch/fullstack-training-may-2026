import json
from datetime import datetime
class Table:
    def __init__(self, name, table_id, size, start, end):
        self.name = name
        self.table_id = table_id
        self.size = size
        self.start = start
        self.end = end

    def display(self):
        print("\n---------- Booking Details ----------")
        print("Customer Name:", self.name)
        print("Table ID:", self.table_id)
        print("Table Size:", self.size)
        print("Start Time:", self.start)
        print("End Time:", self.end)
        print("-------------------------------------")

def create_tables():
    tables = []

    for i in range(1, 11):
        tables.append({
            "table_id": "T" + str(i),
            "table_size": "2 Seater"
        })

    for i in range(11, 21):
        tables.append({
            "table_id": "T" + str(i),
            "table_size": "4 Seater"
        })

    for i in range(21, 26):
        tables.append({
            "table_id": "T" + str(i),
            "table_size": "6 Seater"
        })
    return tables

def load_data():
    try:
        with open("bookings.json", "r") as file:
            data = json.load(file)
        if isinstance(data, list):
            data = {
                "tables": create_tables(),
                "bookings": data
            }
            with open("bookings.json", "w") as file:
                json.dump(data, file, indent=4)

        return data
    except:
        data = {
            "tables": create_tables(),
            "bookings": []
        }
        with open("bookings.json", "w") as file:
            json.dump(data, file, indent=4)

        return data

def booking():

    data = load_data()

    tables = data["tables"]
    bookings = data["bookings"]

    print("\n--------- Available Tables ---------")
    for t in tables:
        booked = False
        for b in bookings:
            if b["table_id"] == t["table_id"]:
                booked = True
                break
        if booked == False:
            print(t["table_id"], "-", t["table_size"])

    name = input("\nCustomer Name: ")

    table_id = input("Enter Table ID: ").upper()
    start = input("Start Time (HH:MM): ")
    end = input("End Time (HH:MM): ")

    table = None
    for t in tables:
        if t["table_id"] == table_id:
            table = t
            break

    if table is None:
        print("Invalid Table ID!")
        return
    try:
        new_start = datetime.strptime(start, "%H:%M")
        new_end = datetime.strptime(end, "%H:%M")
    except:
        print("Invalid Time Format!")
        return
    if new_start >= new_end:
        print("End Time must be greater than Start Time!")
        return
    for b in bookings:

        if b["table_id"] == table_id:
            old_start = datetime.strptime(b["start"], "%H:%M")
            old_end = datetime.strptime(b["end"], "%H:%M")

            if new_start < old_end and new_end > old_start:
                print("Table already booked at this time!")
                return

    new_booking = {
        "customer_name": name,
        "table_id": table_id,
        "table_size": table["table_size"],
        "start": start,
        "end": end
    }

    bookings.append(new_booking)

    with open("bookings.json", "w") as file:
        json.dump(data, file, indent=4)
    obj = Table(
        name,
        table_id,
        table["table_size"],
        start,
        end
    )
    print("\nBooking Successful!")
    obj.display()

booking()