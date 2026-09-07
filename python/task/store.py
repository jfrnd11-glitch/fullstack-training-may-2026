store=[
{"phone_name":"infinx hot8","price":8000},
{"phone_name":"vivo","price":12000},
{"phone_name":"oppo","price":15000},
{"phone_name":"nothing","price":45000},
{"phone_name":"redmi","price":12300},
{"phone_name":"realme","price":9000},
{"phone_name":"motrola","price":15000},
{"phone_name":"iphone","price":32000}

]

print("\n===== MOBILE STORE =====")

for phone in store:
    if phone["price"]>10000:
     print(phone["phone_name"],"=",phone["price"],)

print("\n----Ander 10000-----")    
    
for phone in store:
   if phone["price"]<=10000:
      print(phone["phone_name"],"=",phone["price"])


