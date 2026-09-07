from datetime import date

print("==============================")
print("       DATE OF BIRTH")
print("==============================")

day = int(input("Enter Birth Day: "))
month = int(input("Enter Birth Month: "))
year = int(input("Enter Birth Year: "))

dob = date(year, month, day)

print("\n===== DOB DETAILS =====")

print("Date of Birth:", dob)
print("Year:", dob.year)
print("Month:", dob.month)
print("Day:", dob.day)

print("Day Name:", dob.strftime("%A"))
