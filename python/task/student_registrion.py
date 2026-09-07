import os
import re
import uuid
import logging
from datetime import datetime

INPUT_FILE = "students.txt"
UUID_FILE = "students_uuid.txt"
LOG_FILE = "logs/system.log"

os.makedirs("logs", exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s] [%(levelname)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    handlers=[
        logging.FileHandler(LOG_FILE, encoding="utf-8")
    ]
)


def log_error(error, message=""):
    error_type = type(error).__name__

    logging.error(
        f"{message} | "
        f"Error Type: {error_type} | "
        f"Error: {error}"
    )


def log_validation_error(error_type, message):
    logging.error(f"{message} | "f"Error Type: {error_type}")


def generate_student_id():
    try:
        if not os.path.exists(INPUT_FILE):
            logging.info("Input file not found. Starting with STU001")
            return "STU001"

        with open(INPUT_FILE, "r") as file:
            count = sum(
                1 for line in file if line.strip())

        return f"STU{count + 1:03d}"

    except FileNotFoundError as error:
        log_error(error,"Student ID generation failed")
        return "STU001"

    except PermissionError as error:
        log_error(error,"Permission denied while reading student file")
        return "STU001"

    except Exception as error:
        log_error(error,"Unexpected error while generating Student ID")
        return "STU001"


def get_student_input():
    student_id = generate_student_id()

    print("\nStudent ID:", student_id)

    while True:
        name = input("Enter Name: ").strip()
        clean_name = name.replace(" ", "")

        if len(clean_name) >= 3 and clean_name.isalpha():
            print("Valid Name")
            break

        else:
            print("Not Valid, Try Again.")

            log_validation_error("NameValidationError",f"Invalid name entered: {name}")

    while True:
        age_input = input("Enter Age: ").strip()

        try:
            age = int(age_input)

            if 1 <= age <= 120:
                print("Valid Age")
                break

            else:
                print("Not Valid, Try Again.")

                log_validation_error("AgeValidationError",f"Invalid age entered: {age}")

        except ValueError as error:
            print("Age must be a number.")

            log_error(error,"Age conversion failed")

    while True:
        email = input("Enter Email: ").strip()

        pattern = (r"^[A-Za-z0-9._%+-]+@"r"[A-Za-z0-9.-]+\.[A-Za-z]{2,}$")

        if re.fullmatch(pattern, email):
            print("Valid Email")
            break

        else:
            print("Not Valid Email, Try Again.")

            log_validation_error(
                "EmailValidationError",
                f"Invalid email entered: {email}"
            )

    while True:
        address = input("Enter Address: ").strip()

        if address and "," not in address:
            print("Valid Address")
            break

        else:
            print("Not Valid, Try Again.")

            log_validation_error(
                "AddressValidationError",
                f"Invalid address entered: {address}"
            )

    while True:
        country = input("Enter Country: ").strip()
        clean_country = country.replace(" ", "")

        if country and clean_country.isalpha():
            print("Valid Country")
            break

        else:
            print("Not Valid, Try Again.")

            log_validation_error(
                "CountryValidationError",
                f"Invalid country entered: {country}"
            )

    registration_datetime = datetime.now()

    registration_date = registration_datetime.strftime("%d-%m-%Y")

    registration_time = registration_datetime.strftime("%I:%M:%S")

    unique_id = str(uuid.uuid4())

    try:
        with open(INPUT_FILE, "a") as file:
            file.write(
                f"{student_id},"
                f"{name},"
                f"{age},"
                f"{email},"
                f"{address},"
                f"{country},"
                f"{registration_date},"
                f"{registration_time}\n"
            )

        with open(UUID_FILE, "a") as file:
            file.write(
                f"{student_id},"
                f"{unique_id}\n"
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
        print("Date       :", registration_date)
        print("Time       :", registration_time)
        print("================================")
        print("\nStudent data saved successfully.")
        print("================================")

        logging.info(f"{student_id} registered")

        logging.info(
            f"UUID generated for {student_id}: "
            f"{unique_id}"
        )

        logging.info(
            f"Registration Date: "
            f"{registration_date}, "
            f"Time: {registration_time}"
        )

    except FileNotFoundError as error:
        print("\nFile not found.")

        log_error(error,"Student data saving failed")

    except PermissionError as error:
        print("\nFile permission problem.")

        log_error(error,"Permission denied while saving student data")

    except Exception as error:
        print("\nStudent data not saved.")

        log_error(error,"Unexpected error while saving student data")


print("\n================================")
print("      STUDENT REGISTRATION")
print("================================")

try:
    get_student_input()

except KeyboardInterrupt:
    print("\nProgram stop.")

    logging.warning("Program stopped by user using KeyboardInterrupt")

except Exception as error:
    print("\nUnexpected error.")

    log_error(error,"Program execution failed")