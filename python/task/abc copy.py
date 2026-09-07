print("=" * 70)
print("         PROFESSIONAL RESUME FORMATTER")
print("=" * 70)


while True:
    full_name = input("Enter Full Name : ").strip().title()

    if full_name.replace(" ", "").isalpha():
        break
    else:
        print("Invalid Full Name!")

while True:
    father_name = input("Enter Father Name : ").strip().title()

    if father_name.replace(" ", "").isalpha():
        break
    else:
        print("Invalid Father Name!")

while True:
    email = input("Enter Email ID : ").strip().lower()

    at_count = email.count("@")
    dotcom_count = email.count(".com")

    email_valid = (
        at_count == 1
        and dotcom_count == 1
        and email.index("@") < email.index(".com")
    )

    if email_valid:
        break
    else:
        print("Invalid Email!")

while True:
    phone = input("Enter Phone Number : ").strip()

    if phone.isdigit() and len(phone) == 10:
        break
    else:
        print("plese enter 10 digit phone number.")

while True:
    city = input("Enter City : ").strip().title()

    if city.replace(" ", "").isalpha():
        break
    else:
        print("Invalid City!")

while True:
    country = input("Enter Country : ").strip().upper()

    if country.replace(" ", "").isalpha():
        break
    else:
        print("Invalid Country!")

qualification = input("Enter Qualification : ").strip().title()

university = input("Enter University : ").strip().title()

skills = input("Enter Skills  : ").strip()

languages = input("Enter Languages  : ").strip()

experience = input("Enter Experience : ").strip().title()


formatted_city = city.title()
formatted_country = country.upper()
formatted_qualification = qualification.title()



skill_list = skills.split(",")

formatted_skills = []

for skill in skill_list:
    formatted_skills.append(skill.strip().title())

skills_output = " | ".join(formatted_skills)



language_list = languages.split(",")

formatted_languages = []

for language in language_list:
    formatted_languages.append(language.strip().title())

language_output = ", ".join(formatted_languages)


resume_id = (
    full_name.replace(" ", "").upper()
    + "-"
    + city.upper()
    + "-"
    + qualification.upper().rstrip(",")
)



print("\n")
print("=" * 30)
print("         SMART RESUME")
print("=" * 30)

print("Full Name        :", full_name)
print("Father Name      :", father_name)
print("Email            :", email)
print("Phone Number     :", phone)
print("City             :", formatted_city)
print("Country          :", formatted_country)
print("Qualification    :", formatted_qualification)
print("University       :", university)
print("Skills           :", skills_output)
print("Languages        :", language_output)
print("Experience       :", experience)
print("Resume ID        :", resume_id)


print("\n")
print("=" * 30)
print("EMAIL ANALYSIS")
print("=" * 30)

print("Email ID         :", email)
print("@ Symbol Count   :", at_count)
print(".com Count       :", dotcom_count)
print("Valid Email      :", email_valid)

print("\n")
print("=" * 70)
print("THANK YOU")
print("=" * 70)