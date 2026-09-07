student = {}


subjects = ["Hindi", "English", "Maths", "Science", "Computer"]


for subject in subjects:
    while True:
        marks = int(input(f"{subject} enter the marks (1-100): "))

        if 1 <= marks <= 100:
            student[subject] = marks
            break
        else:
            print(" Invalid Marks")


total_marks = sum(student.values())


percentage = (total_marks / 500) * 100


if percentage >= 80:
    grade = "A+"
elif percentage >= 60:
    grade = "A"
elif percentage >= 50:
    grade = "B"
elif percentage >= 40:
    grade = "C"
else:
    grade = "D"

if percentage >= 40:
    result = "Pass"
else:
    result = "Fail"

print("\n------ STUDENT RESULT ------")

for subject, marks in student.items():
    print(f"{subject}: {marks}")


print("Total Marks:", total_marks, "/ 500")
print("Percentage:", percentage, "%")
print("Grade:", grade)
print("Result:", result)
