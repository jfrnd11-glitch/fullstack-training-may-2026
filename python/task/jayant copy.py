print("=" * 50)
print("      STUDENT SMART ID CARD GENERATOR")
print("=" * 50)

student = {}
while True:
    institute = input("Enter Institute Name : ").strip().title()
    if institute.replace(" ", "").isalpha():
        student["Institute"] = institute
        break
    else:
        print("Invalid Institute Name!")
while True:
    name = input("Enter Student Full Name : ").strip().title()
    if name.replace(" ", "").isalpha():
        student["Student Name"] = name
        break
    else:
        print("Invalid Name!")

while True:
    father = input("Enter Father Name : ").strip().title()
    if father.replace(" ", "").isalpha():
        student["Father Name"] = father
        break
    else:
        print("Invalid Father Name!")

while True:
    roll = input("Enter Roll Number : ").strip()
    if roll.isdigit():
        student["Roll Number"] = roll
        break
    else:
        print("Roll Number should contain only digits.")

student["Class"] = input("Enter Class : ").strip().upper()

while True:
    section = input("Enter Section : ").strip().upper()
    if len(section) == 1 and section.isalpha():
        student["Section"] = section
        break
    else:
        print("plese enter a single letter.")

student["Department"] = input("Enter Department : ").strip().upper()

while True:
    city = input("Enter City : ").strip().title()
    if city.replace(" ", "").isalpha():
        student["City"] = city
        break
    else:
        print("Invalid City Name!")

blood_groups = ["A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-"]

while True:
    blood = input("Enter Blood Group : ").strip().upper()
    if blood in blood_groups:
        student["Blood Group"] = blood
        break
    else:
        print("Invalid Blood Group!")

while True:
    phone = input("Enter Phone Number : ").strip()
    if phone.isdigit() and len(phone) == 10:
        student["Phone Number"] = phone
        break
    else:
        print("Please enter a valid 10-digit phone number.")

student["Student ID"] = student["Roll Number"].zfill(8)

name_valid = student["Student Name"].replace(" ", "").isalpha()
roll_valid = student["Roll Number"].isdigit()
phone_valid = student["Phone Number"].isdigit() and len(student["Phone Number"]) == 10

print("\n")
print("=" * 50)
print("           STUDENT SMART ID CARD")
print("=" * 50)

for key, value in student.items():
    print(f"{key:<15}: {value}")

print("=" * 50)
print("Validation Report")
print("=" * 50)
print("Name Valid  :", name_valid)
print("Roll Valid  :", roll_valid)
print("Phone Valid :", phone_valid)