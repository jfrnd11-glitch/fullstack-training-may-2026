student = {}

student["hindi"] = int(input("enter the hindi marks: "))
student["english"] = int(input("enter the english marks: "))
student["maths"] = int(input("enter the maths marks: "))

total_marks = (
    student["hindi"] +
    student["english"] +
    student["maths"]
)

percentage = (total_marks / 300) * 100

if percentage >= 80:
    grade = "A+"
elif percentage >= 60:
    grade = "A"
elif percentage >= 50:
    grade = "B"
elif percentage >= 30:
    grade = "C"
else:
    grade = "Fail"
print("------------\nfinal touch-------------")
print("Hindi Marks:", student["hindi"])
print("English Marks:", student["english"])
print("Maths Marks:", student["maths"])
print("Total Marks:", total_marks)
print("Percentage:", percentage, "%")
print("Grade:", grade)