students=[
    {"name": "ragni","marks":90},
    {"name": "sandeep","marks":75},
    {"name": "rohit","marks":80},
    {"name": "mohit","marks":45},
    {"name": "golu","marks":30},
    {"name": "sumit","marks":60}
    ]
pass_count = 0
fail_count = 0 
print("\npass student")
for student in students:

    if student["marks"] > 50:
        print(student["name"])

        pass_count = pass_count + 1

print("\nTotal Pass Students =", pass_count)
print("\npass student and marks")
     
for student in students:
     if student["marks"]>= 50:
        print(student["name"],"=",student["marks"],)
        

print("\nfail student")



for student in students:
     if student["marks"]< 50:
     
      print(student["name"],"=",student["marks"],)
      fail_count = fail_count + 1
print("\nTotal fail Students =", fail_count)