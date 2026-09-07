import os
import json
import re
import uuid
import logging
from datetime import datetime

INPUT_FILE = "students.txt"
UUID_FILE = "students_uuid.txt"
OUTPUT_FILE = "students_output.txt"
JSON_FILE = "students.json"
LOG_FILE = "logs/system.log"

os.makedirs("logs", exist_ok=True)

logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="[%(asctime)s] [%(levelname)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)
accepted_count = 0
rejected_count = 0

def generate_student_id():
    try:
        if not os.path.exists(INPUT_FILE):
            logging.info("Starting with STU001")
            return "STU001"
        with open(INPUT_FILE, "r") as file:            
            count = 0
            for line in file:
                if line.split():
                    count+= 1
        student_id = f"STU{count + 1:03d}"

        logging.info(f"Student ID generated: {student_id}")
        return student_id
    except Exception as error:
        logging.error(f"Student ID generation failed | {error}")
        return "STU001"
    finally:
        logging.info("Student ID generation succesful")

def invalid_data(message):
    global rejected_count
    rejected_count += 1
    logging.error(message)

def get_name():
    while True:
        name = input("Enter Name: ").strip()
        if len(name.replace(" ", "")) >= 3 and name.replace(" ", "").isalpha():
            print("Valid Name")
            return name
        print("Invalid Name, Try Again.")
        invalid_data(f"Invalid name: {name}")

def get_age():
    while True:
        try:
            age = int(input("Enter Age: "))
            if 1 <= age <= 100:
                print("Valid Age")
                return age
            print("Invalid Age, Try Again.")
            invalid_data(f"Invalid age: {age}")
        except ValueError as error:
            print("Age must be a number.")
            invalid_data(f"Invalid age input | {error}")

def get_email():
    while True:
        email = input("Enter Email: ").strip()
        pattern = r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"
        if re.match(pattern, email):
            print("Valid Email")
            return email
        print("Invalid Email, Try Again.")
        invalid_data(f"Invalid email: {email}")

def get_address():
    while True:
        address = input("Enter Address: ").strip()
        if address and "," not in address:
            print("Valid Address")
            return address
        print("Invalid Address, Try Again.")
        invalid_data(f"Invalid address: {address}")

def get_country():
    while True:
        country = input("Enter Country: ").strip()
        if country and country.replace(" ", "").isalpha():
            print("Valid Country")
            return country

        print("Invalid Country, Try Again.")
        invalid_data(f"Invalid country: {country}")

def save_json(student):
    try:
        students = []

        if os.path.exists(JSON_FILE):
            with open(JSON_FILE, "r") as file:
                try:
                    students = json.load(file)
                except :
                    students = []

        students.append(student)
        with open(JSON_FILE, "w") as file:
            json.dump(students, file, indent=4)
        logging.info(f"JSON data saved for {student['student_id']}")

    except Exception as error:
        print("JSON data save nahi hua.")
        logging.error(f"JSON saving failed | {error}")

    finally:
        logging.info("JSON process completed")

def save_student(
    student_id,
    name,
    age,
    email,
    address,
    country,
    unique_id
):
    try:
        now = datetime.now()

        date = now.strftime("%d-%m-%Y")
        time = now.strftime("%I:%M:%S")
        student = {
            "student_id": student_id,
            "name": name,
            "age": age,
            "email": email,
            "address": address,
            "country": country,
            "uuid": unique_id,
            "date": date,
            "time": time
        }

        with open(INPUT_FILE, "a") as file:
            file.write(
                f"{student_id},"
                f"{name},"
                f"{age},"
                f"{email},"
                f"{address},"
                f"{country}\n"
            )

        logging.info(f"Student data saved in {INPUT_FILE}")
        with open(UUID_FILE, "a") as file:
            file.write(f"{student_id},{unique_id}\n")

        logging.info(f"UUID saved for {student_id}")

        with open(OUTPUT_FILE, "a") as file:
            file.write(
                f"ID: {student_id}\n"
                f"Name: {name}\n"
                f"Age: {age}\n"
                f"Email: {email}\n"
                f"Location: {address}, {country}\n"
                f"UUID: {unique_id}\n"
                f"Date: {date}\n"
                f"Time: {time}\n\n"
            )

        logging.info(f"Output data saved for {student_id}")
        save_json(student)
        return True

    except Exception as error:
        print("Student data not saved.")
        logging.error(f"Student data saving failed | {error}")
        return False
    finally:
        logging.info("Student data saving process completed")

def get_student_input():
    global accepted_count
    student_id = generate_student_id()
    print("\nStudent ID:", student_id)
    name = get_name()
    age = get_age()
    email = get_email()
    address = get_address()
    country = get_country()
    unique_id = str(uuid.uuid4())
    logging.info(f"UUID generated for {student_id}: {unique_id}")

    if save_student(
        student_id,
        name,
        age,
        email,
        address,
        country,
        unique_id
    ):
        accepted_count += 1
        logging.info(f"{student_id} accepted and stored")

        print("\n---------------------------------")
        print("       STUDENT REGISTERED")
        print("-----------------------------------")
        print("Student ID :", student_id)
        print("Name       :", name)
        print("Age        :", age)
        print("Email      :", email)
        print("Address    :", address)
        print("Country    :", country)
        print("UUID       :", unique_id)
        print("-------------------------------")

        print("\nStudent data saved successfully.")
    else:
        print("\nStudent data not saved.")
        logging.error(f"{student_id} data was not saved")

print("\n--------------------------------")
print("      STUDENT REGISTRATION")
print("----------------------------------")

try:
    get_student_input()

except KeyboardInterrupt:
    print("\nProgram stopped.")
    logging.warning("Program stopped by user")

except Exception as error:
    print("\nUnexpected error:", error)
    logging.error(f"Program execution failed | {error}")

finally:
    logging.info("Program execution completed")

print("\n--------------------------------")
print("           SUMMARY")
print("----------------------------------")
print("Accepted :", accepted_count)
print("Rejected :", rejected_count)
print("--------------------------------")

logging.info(
    f"Registration Summary | "
    f"Accepted: {accepted_count} | "
    f"Rejected: {rejected_count}"
)