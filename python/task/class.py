print("=" * 50)
print("      STUDENT SMART ID CARD GENERATOR")
print("=" * 50)

while True:
    institute = input("Enter Institute Name : ").strip().title()

    if institute.replace(" ", "").isalpha():
        break
    else:
        print("Invalid Institute Name!")

while True:
    name = input("Enter Student Full Name : ").strip().title()

    if name.replace(" ", "").isalpha():
        break
    else:
        print("Invalid Name!")
while True:
    father = input("Enter Father Name : ").strip().title()

    if father.replace(" ", "").isalpha():
        break
    else:
        print("Invalid Father Name!")

while True:
    roll = input("Enter Roll Number : ").strip()

    if roll.isdigit():
        break
    else:
        print("Roll Number should contain only digits.")

student_class = input("Enter Class : ").strip().upper()

while True:
    section = input("Enter Section : ").strip().upper()

    if len(section) == 1 and section.isalpha():
        break
    else:
        print("Section should be a single letter.")

department = input("Enter Department : ").strip().upper()

while True:
    city = input("Enter City : ").strip().title()

    if city.replace(" ", "").isalpha():
        break
    else:
        print("Invalid City Name!")

blood_groups = ["A+","A-","B+","B-","AB+","AB-","O+","O-"]

while True:
    blood = input("Enter Blood Group : ").strip().upper()

    if blood in blood_groups:
        break
    else:
        print("Invalid Blood Group!")

while True:
    phone = input("Enter Phone Number : ").strip()

    if phone.isdigit() and len(phone) == 10:
        break
    else:
        print("plese enter valid 10 digit phone number.")

student_id = roll.zfill(8)

name_valid = name.replace(" ", "").isalpha()
roll_valid = roll.isdigit(4)
phone_valid = phone.isdigit() and len(phone) == 10

print("\n")
print("=" * 50)
print("           STUDENT SMART ID CARD")
print("=" * 50)
print(f"Student ID     : {student_id}")
print(f"Institute      : {institute}")
print(f"Student Name   : {name}")
print(f"Father Name    : {father}")
print(f"Roll Number    : {roll}")
print(f"Class          : {student_class}")
print(f"Section        : {section}")
print(f"Department     : {department}")
print(f"City           : {city}")
print(f"Blood Group    : {blood}")
print(f"Phone Number   : {phone}")