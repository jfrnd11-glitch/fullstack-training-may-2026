import stdiomask
class registrion:
    def __init__(self, name, email, id, password):
        self.name = name
        self.email = email
        self.id = id
        self.password = password

class display(registrion):
    def display(self):
        print("\n---------------------------")
        print("Name:", self.name)
        print("Email:", self.email)
        print("ID:", self.id)
        print("password:", "?" * len(self.password))
        print("---------------------------")

class update(display):
    def update(self):
        self.name = input("Enter new name: ")
        self.email = input("Enter new email: ")
        self.password = stdiomask.getpass("Enter new password: ",mask="?")
        print("\n---------------------------")
        print("Update successful")
        print("---------------------------")

class delete(update):
    def delete(self):

        print(self.name)
        print(self.id)
        print("\n---------------------------")
        print("User deleted successfully")
        print("---------------------------")
        del self.email
        del self.password
def registration():
    print("\n========== REGISTRATION ==========")
    name = input("Enter name: ")
    email = input("Enter email: ")
    id = input("Enter ID: ")
    password = stdiomask.getpass("Enter password: ",mask="?")
    obj = delete(name, email, id, password)
    print("\n---------------------------")
    print("Registration successful")
    print("---------------------------")
    return obj

def menu(obj):
    while True:
        print("\n---------- MENU ---------")
        print("1. Display")
        print("2. Update")
        print("3. Delete")
        print("4. Exit")
        print("----------------------------")
        choice = input("Enter your choice: ")
        if choice == "1":
            obj.display()
        elif choice == "2":
            obj.update()
        elif choice == "3":
            obj.delete()
        elif choice == "4":
            print("Program Exit")
            break
        else:
            print("Invalid choice")
obj = registration()
menu(obj)