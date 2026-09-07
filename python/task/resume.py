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
        print("Phone Number must contain exactly 10 digits.")

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

skills = input("Enter Skills (comma separated) : ").strip()

languages = input("Enter Languages (comma separated) : ").strip()

experience = input("Enter Experience : ").strip().title()

career_objective = input("Create Objective : ").strip().capitalize()

formatted_city = city.title()
formatted_country = country.upper()
formatted_qualification = qualification.title()


at_symbol_count = email.count("@")
dotcom_count = email.count(".com")


skill_list = skills.split(",")

formatted_skills = []

for skill in skill_list:
    formatted_skills.append(skill.strip().title())

skills_output = " | ".join(formatted_skills)


language_list = languages.split(",")

formatted_languages = []

for language in language_list:
    formatted_languages.append(language.strip().title())

formatted_languages.append("Arabic")

language_output = ", ".join(formatted_languages)
resume_id = (
    full_name.replace(" ", "").upper()
    + "-"
    + city.replace(" ", "").upper()
    + "-"
    + qualification.replace(" ", "").upper()
)


print("\n")
print("=" * 70)
print("                     SMART RESUME")
print("=" * 70)

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
print("Career Objective :", career_objective)
print("Resume ID        :", resume_id)
print("\n")
print("=" * 70)
print("EMAIL ANALYSIS")
print("=" * 70)

print("Email ID         :", email)
print("@ Symbol Count   :", at_symbol_count)
print(".com Count       :", dotcom_count)
print("Valid Email      :", email_valid)

print("\n")
print("=" * 70)
print("THANK YOU")
print("=" * 70)