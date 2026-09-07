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

def booking():
    tables = []

    for i in range(1, 11):
        tables.append({"table_id": "T" + str(i), "table_size": "2 Seater"})

    for i in range(11, 21):
        tables.append({"table_id": "T" + str(i), "table_size": "4 Seater"})

    for i in range(21, 26):
        tables.append({"table_id": "T" + str(i), "table_size": "6 Seater"})
    try:
        with open("bookings.json", "r") as file:
            bookings = json.load(file)
    except:
        bookings = []

    print("\n--------- Available Tables ---------")
    for t in tables:
        found = False
        for b in bookings:
            if b["table_id"] == t["table_id"]:
                found = True
        if found == False:
            print(t["table_id"], "-", t["table_size"])

    name = input("\nCustomer Name: ")
    table_id = input("Enter Table ID: ").upper()
    start = input("Start Time (HH:MM): ")
    end = input("End Time (HH:MM): ")

    table = None
    for t in tables:
        if t["table_id"] == table_id:
            table = t
    if table == None:
        print("Invalid Table ID!")
        return
    new_start = datetime.strptime(start, "%H:%M")
    new_end = datetime.strptime(end, "%H:%M")
    for b in bookings:
        if b["table_id"] == table_id:
            old_start = datetime.strptime(b["start"], "%H:%M")
            old_end = datetime.strptime(b["end"], "%H:%M")
            if new_start < old_end and new_end > old_start:
                print("Table already booked at this time!")
                return

    data = {
        "customer_name": name,
        "table_id": table_id,
        "table_size": table["table_size"],
        "start": start,
        "end": end
    }
    bookings.append(data)
    with open("bookings.json", "w") as file:
        json.dump(bookings, file, indent=4)
    obj = Table(name, table_id, table["table_size"], start, end)
    print("\nBooking Successful!")
    obj.display()

booking()