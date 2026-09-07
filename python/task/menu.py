students=[]
def registration():
    print("\n===== REGISTRATION=====")
    for i in range(5):
        name =input(f"enter student{i+1}name:")
        students. append(name)
def login():
    print("\n=====LOGIN=====")
    name = input("enter student name:")
    if name in students:
        print(" login successful!")
        print("welcome", name)
       
        print("\nRegistered students:")
        for i in range(len(students)):
            print(i + 1, ".", students[i])
        
    else:
        print("invalid student name ")
        print("please register first.")
def menu():
    while True:
        print("\n===== MAIN MENU=====")
        print("1.registration")
        print("2.login")
        print("3.exit")
        choice =input ("enter your choice:")
        if choice == "1": registration()
        elif choice == "2": login()
        elif choice == "3":
             print("\nThank You!")
             break
    else:
        print("\n invalid choice! please enter 1,2,3.")
menu()

        