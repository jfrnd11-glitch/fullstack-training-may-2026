class Student:

    def __init__(self, student_id, name, age, course):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.course = course

    def display(self):
        print("Student ID:", self.student_id)
        print("Name:", self.name)
        print("Age:", self.age)
        print("Course:", self.course)

    def update(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course


students = {}


def register_student():
    student_id = int(input("Enter Student ID: "))

    if student_id in students:
        print("Student ID already exists.")
        return

    name = input("Enter Name: ")
    age = int(input("Enter Age: "))
    course = input("Enter Course: ")

    student = Student(student_id, name, age, course)

    students[student_id] = student

    print("Student registered successfully.")


def update_student():
    student_id = int(input("Enter Student ID to update: "))

    if student_id not in students:
        print("Student not found.")
        return

    name = input("Enter New Name: ")
    age = int(input("Enter New Age: "))
    course = input("Enter New Course: ")

    students[student_id].update(name, age, course)

    print("Student updated successfully.")


def delete_student():
    student_id = int(input("Enter Student ID to delete: "))

    if student_id not in students:
        print("Student not found.")
        return

    del students[student_id]

    print("Student deleted successfully.")


def show_students():
    if not students:
        print("No students registered.")
        return

    for student in students.values():
        print()
        student.display()


while True:

    print("\n===== Student Management System =====")
    print("1. Student Registration")
    print("2. Update Student")
    print("3. Delete Student")
    print("4. Show Students")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        register_student()

    elif choice == "2":
        update_student()

    elif choice == "3":
        delete_student()

    elif choice == "4":
        show_students()

    elif choice == "5":
        print("Program exited.")
        break

    else:
        print("Invalid choice.")