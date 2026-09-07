student={
    "name":input("please enter your name:"),
    "father_name":input("please enter your father name:"),
    "email":input("please enter your email:"),
    "phone_number":int(input("please enter your phone number:")),
    "city":input("please enter your city:"),
    "countary":input("please enter your countary:"),
    "qualification":int(input("please enter your qualification:")),
    "univarcity_name":input("please enter univarcity name:"),
    "skills":input("please enter your skills:"),
    "languages":input("please enter your languages:"),
    "exprince":int(input("please enter your exprince:")),
    "resume_id":input("please enter your resume id:"),
    "carear_object":input("please enter your career object:"),
    "institute_name":input("please enter your institute name:"),
    "id":int(input("please enter id:")),
    "email":"jayant@gmail.com"


}

print("\n" + "="*35)
print("student id card")
print("="*35)

print("Name :",student["name"].isalpha())
print("Father_name:",student["father_name"].isalpha())
print("Email:",student["email"])
print("Phone_number:",student["phone_number"])
print("City:",student["city"])
print("Countary:",student["countary"])
print("Qualification:",student["qualification"])
print("Univarcity_name:",student["univarcity_name"])
print("Skills:",student["skills"])
print("Languages:",student["languages"])
print("Exprince:",student["exprince"])
print("resume_id:",student["resume_id"])
print("carear_object:",student["carear_object"])
print("institute_name:",student["institute_name"])
print("id:",str(student["id"]).zfill(10))
print(student["email"])

print("\n" + "="*35)
print("Name Analysis")
print("="*35)


student["name"].upper()
print("upper Name =", student["name"].upper())

student["name"].lower()
print("lower Name =", student["name"].lower())

student["name"].swapcase()
print("swap case =", student["name"].swapcase())

student["name"].count("a")
print("Letter Count =", student["name"].lower().count("a"))

student["Word Count"] = len(student["name"].split())
print("Word Count :", student["Word Count"])


print("\n" + "="*35)
print("employee exprince")
print("="*35)

print("Exprince:",student["exprince"])

print("\n" + "="*35)
print("RESUME ID")
print("="*35)

print("resume_id:",student["resume_id"])


print("\n" + "="*35)
print("career object")
print("="*35)

print("career-object:",student["career_object"])


print("\n" + "="*35)
print("smart student id card")
print("="*35)

print("institute_name:",student["institute_name"])
print("name:",student["name"])
print("id:",student["id"])


print("\n" + "="*35)
print("email verify")
print("="*35)

correct_email="jayant@gmail.com"
while True:
    email = input("enter your email:")
    if email == correct_email:
        print("this is a valid email")
        break

    else:
        print("enter valid email id")
        print("email:",student["email"])

print("\n","="*35)
print("number verify")
print("="*35)



while True:
    number=input("please 10 digite number:")
    if len(number)==10 and number.isdigit():
        print("this is valid number")
        break


    else:
        print("try aggain")