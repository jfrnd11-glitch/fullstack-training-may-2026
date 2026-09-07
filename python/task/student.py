import os
import uuid
import json
data = []
def registrion():
    print("=====================")
    print("      registrion     ")
    print("=====================")
    one_=int(uuid.uuid4())[:6]
    name =input("enter student name:")
    age = int(input("enter student age:"))
    mobile = int(input("enter student mobile number:"))
    email =input("enter student email id:")
    address = input("enter student address:")
    pincode = int(input("enter student pincode:"))

    registrion{
        "uudi":one_,
        "name":name,
        "age":age,
        "mobile":mobile,
        "email":email,
        "address":address,
        "pincode":pincode

    }

    data.append(registrion)
    with open("student.json","w")as student_registrion:
        json.dump(data,student_registrion,indent=4)
        print("registrion successful!")
def update():
    print("=======================")
    print("        update        ")
    print("=======================")
    