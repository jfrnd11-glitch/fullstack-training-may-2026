users = {} # YE EK KHALI DESNORI HAI JISME BAD ME DATA STORE HOGA 

def registration(): # YE EK REGISTRION FUNCTION HAI 
    print("\n===== REGISTRATION =====")

    while True:# YE KISI V CODICTION ME TRUE HOGA 
        userid = input("Enter User ID: ")#USER SE USER ID MANGTA HAI

        if userid.isdigit() and int(userid) not in users:# HAMNE VALIDATION LAGAYA HAI TAKI USER GALAT INPUT NA LE
            userid = int(userid)
            break # YAHA PAR LOOP KHTAMA HO JATA HAI

        print("User ID must be integer and unique!")

    while True:
        name = input("Enter Name: ").strip()

        if len(name.replace(" ", "")) >= 3 and name.replace(" ", "").isalpha():# YAHA VALIDATION LAGAYA GAYA HAI KI NAME KA LETTER 3 SE JAYDA HO 
            break 

        print("Name must contain at least 3 letters!")

    while True:
        password = input("Enter Password: ")

        if (any(c.isupper() for c in password) 
            
                and any(c.islower() for c in password)
                and any(c.isdigit() for c in password)):
            break
        

        print("enter valid password!")

    users[userid] = {           
        "username": name,      # UPAR JO USER INPUT LEGA WAHI USER NAME AND PASSWORD SE REGITRATION SUCCES FUL HOGA
        "password": password
    }

    print("Registration Successful!")


def login_screen():# YE EK LOGIN FUNCTION HAI JISME HAM USER KA ID AUR PASSWORD DAL KAR LOGIN KARENGE
    print("\n===== LOGIN =====")

    if not users:
        print("Please register first!")
        return

    userid = input("Enter User ID: ")
    password = input("Enter Password: ")

    if userid.isdigit() and int(userid) in users:
        if users[int(userid)]["password"] == password:

            from Dashboard import show_dashboard
            show_dashboard(users[int(userid)]["username"])
            return

    print("Invalid User ID or Password!")


def main_menu():# YE MENU FUNCTION HAI JISKE ANDAR REGISTRION LOGIN AND EXIT KO RAKHA HAI
    while True:
        print("\n===== MAIN MENU =====")
        print("1. Registration")
        print("2. Login")
        print("3. Exit")

        choice = input("Enter Choice: ") # USER CHOICE KAREGA 

        if choice == "1":
            registration() # AGAR WO 1 CHOICE KIYA TO REGISTRION KE LIYE CHALA JAYEGA 

        elif choice == "2":
            login_screen()# USER 2 CHOICE KAREGA TO LOGIN KAREGA AUR WO DASHBOARD KA SHOW KARNE LAGEGA

        elif choice == "3":
            print("Thank you!")
            break

        else:
            print("Invalid Choice!")