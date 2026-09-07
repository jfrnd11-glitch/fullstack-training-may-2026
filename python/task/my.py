from getpass import getpass
class registrion:
    def __init__(self,name, email,id,password):
        self.name = name
        self.email = email
        self.id = id
        self._password = password
        
        
class display(registrion):
    def display(self):
        print("name:",self.name)
        print("email:",self.email)
        print("id:",self.id)
        print("password:",self.password)

        print("\n====================")
        print("registrion succesfull")
        print("\n====================")

class update(display):
    def update(self):
        self.name = input("enter user new name:")
        self.email = input("enter user new email:")
        self.password = getpass("enter user new password")
        print("\n---------------------------")
        print("     update succesfull"       )
        print("\n---------------------------")
    
class delete(update):
    def delete(self):
        print(self.id)
        print("\n===================")
        print("\n delete succesfull")
        print("\n===================")

def menu(obj):
        while True:            
            print("\n========== MENU ==========")
            print("1. display")
            print("2. Update")
            print("3. Delete")
            print("4. Exit")
            print("==========================")
        
            choice = input("Enter your choice: ")
            if choice == "1":
                name = input("enter your name")
                email = input("enter your email")
                id = int(input("enter your id"))
                password = input("enter your password")
                obj(name,email,id,password)

            
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
menu ()
