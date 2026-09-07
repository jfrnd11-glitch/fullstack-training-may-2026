from getpass import getpass
class registrion:
    def __init__(self, name, email, id, password):
        self.name = name
        self.email = email
        self.id = id
        self.password = password

class display(registrion):
    def display(self):
        print("Name:", self.name)
        print("Email:", self.email)
        print("ID:", self.id)

class update(display):
    def update(self):
        self.name = input("Enter new name: ")
        self.email = input("Enter new email: ")
        self.password = getpass("Enter new password: ")

        print("\n---------------------------")
        print("Update successful")
        print("---------------------------")

class delete(update):
    def delete(self):
        print("\n---------------------------")
        print("User deleted successfully")
        print("---------------------------")

obj = delete("jayant kumar","jayant@gmail.com","0004","705097")
def menu(obj):

 while True:
    print("\n========== MENU ==========")
    print("1. Update")
    print("2. Delete")
    print("3. Exit")
    print("==========================")

    choice = input("Enter your choice: ")
    if choice == "1":
        obj.update()
    elif choice == "2":
        obj.delete()
    elif choice == "3":
        print("Program Exit")
        break
    else:
        print("Invalid choice")
menu(obj)