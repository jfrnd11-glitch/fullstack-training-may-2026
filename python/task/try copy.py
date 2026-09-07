menu={
    "burgar": 40,
    "chowming": 20,
    "egg roll": 40,
    "panir chili": 120,
    "chiken roll": 50,
    "franch fry": 60,
    "chiken chili": 140,
    "momo": 50,
}

print("\n-----FAST FOOD WALA----")
print("\n-----menu-----")
 


for item, price in menu.items():
    print(item, "=", price)
       
print("\n----- ORDER -----")
choice = input("Please give me order: ")

if choice in menu:
    quantity = int(input("quantity: "))

    price = menu[choice]
    total = price * quantity
    print("\n----- BILL -----")
    print("Item:", choice)
    print("Price:", price)
    print("Quantity:", quantity)
    print("Total Bill:", total)

else:
    print("this item is not available.")