import os
import re
import json
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


def log_error(error, message):
    logging.error(f"{message} | {error}")


def invalid_data(message, error_type):
    global rejected_count
    rejected_count += 1
    logging.error(f"{message} | {error_type}")


def generate_student_id():
    try:
        if not os.path.exists(INPUT_FILE):
            return "STU001"

        with open(INPUT_FILE, "r") as file:
            count = sum(1 for line in file if line.strip())

        return f"STU{count + 1:03d}"

    except Exception as error:
        log_error(error, "Student ID generation failed")
        return "STU001"

    finally:
        logging.info("Student ID generation succesfull")


def get_name(student_id):
    while True:
        name = input("Enter Name: ").strip()
        clean_name = name.replace(" ", "")

        if len(clean_name) >= 3 and clean_name.isalpha():
            print("Valid Name")
            return name

        print("Invalid Name, Try Again.")

        invalid_data(f"Invalid name for {student_id}: {name}","NameValidationError")

def get_age(student_id):
    global rejected_count

    while True:
        age_input = input("Enter Age: ").strip()

        try:
            age = int(age_input)

            if 1 <= age <= 100:
                print("Valid Age")
                return age

            print("Invalid Age, Try Again.")

            invalid_data(f"Invalid age for {student_id}: {age}","AgeValidationError")

        except ValueError as error:
            print("Age must be a number.")
            rejected_count += 1
            log_error(error, f"Invalid age for {student_id}")


def get_email(student_id):
    pattern = r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"

    while True:
        email = input("Enter Email: ").strip()

        if re.fullmatch(pattern, email):
            print("Valid Email")
            return email
        print("Invalid Email, Try Again.")
        invalid_data(f"Invalid email for {student_id}: {email}","EmailValidationError")

def get_address(student_id):
    while True:
        address = input("Enter Address: ").strip()
        if address and "," not in address:
            print("Valid Address")
            return address
        print("Invalid Address, Try Again.")
        invalid_data(f"Invalid address for {student_id}: {address}","AddressValidationError")

def get_country(student_id):
    while True:
        country = input("Enter Country: ").strip()
        clean_country = country.replace(" ", "")
        if country and clean_country.isalpha():
            print("Valid Country")
            return country
        print("Invalid Country, Try Again.")
        invalid_data(f"Invalid country for {student_id}: {country}","CountryValidationError")

def save_json(student):
    try:
        students = []
        if os.path.exists(JSON_FILE):
            with open(JSON_FILE, "r") as file:
                try:
                    students = json.load(file)
                except json.JSONDecodeError:
                    students = []

        students.append(student)
        with open(JSON_FILE, "w") as file:
            json.dump(students, file, indent=4)
    except Exception as error:
        log_error(error, "JSON data saving failed")
        raise
    finally:
        logging.info("JSON saving process completed")

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
        registration_date = now.strftime("%d-%m-%Y")
        registration_time = now.strftime("%I:%M:%S")
        student = {
            "student_id": student_id,
            "name": name,
            "age": age,
            "email": email,
            "address": address,
            "country": country,
            "uuid": unique_id,
            "date": registration_date,
            "time": registration_time
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

        with open(UUID_FILE, "a") as file:
            file.write(f"{student_id},{unique_id}\n")

        with open(OUTPUT_FILE, "a") as file:
            file.write(
                f"ID: {student_id}\n"
                f"Name: {name}\n"
                f"Age: {age}\n"
                f"Email: {email}\n"
                f"Location: {address}, {country}\n"
                f"UUID: {unique_id}\n"
                f"Date: {registration_date}\n"
                f"Time: {registration_time}\n"
            )
        save_json(student)
        return True
    except Exception as error:
        log_error(error, "Student data saving failed")
        return False
    finally:
        logging.info("Student data saving process completed")

def get_student_input():
    global accepted_count
    student_id = generate_student_id()
    print("\nStudent ID:", student_id)
    name = get_name(student_id)
    age = get_age(student_id)
    email = get_email(student_id)
    address = get_address(student_id)
    country = get_country(student_id)

    unique_id = str(uuid.uuid4())

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

        logging.info(
            f"{student_id} accepted and stored"
        )

        logging.info(
            f"UUID generated for {student_id}: {unique_id}"
        )

        print("\n================================")
        print("       STUDENT REGISTERED")
        print("================================")
        print("Student ID :", student_id)
        print("Name       :", name)
        print("Age        :", age)
        print("Email      :", email)
        print("Address    :", address)
        print("Country    :", country)
        print("UUID       :", unique_id)
        print("================================")

        print("\nStudent data saved successfully.")

    else:
        print("\nStudent data not saved.")

    logging.info(
        f"Registration Summary | "
        f"Accepted: {accepted_count} | "
        f"Rejected: {rejected_count}"
    )


print("\n================================")
print("      STUDENT REGISTRATION")
print("================================")

try:
    get_student_input()

except KeyboardInterrupt:
    print("\nProgram stopped.")
    logging.warning("Program stopped by user")

except Exception as error:
    print("\nUnexpected error.")
    log_error(error, "Program execution failed")

finally:
    logging.info("Program execution completed")

print("\n================================")
print("           SUMMARY")
print("================================")
print("Accepted :", accepted_count)
print("Rejected :", rejected_count)
print("================================")